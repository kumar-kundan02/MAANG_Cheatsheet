"""
Direct PDF Generator from DSA Folder Structure
Generates a PDF file directly from folder structure with professional styling
No external dependencies - uses HTML rendering with native CSS styling
"""

import os
import re
from pathlib import Path
import html
import base64

# C# Syntax Highlighting
def highlight_csharp(code):
    """Apply C# syntax highlighting using HTML spans"""
    # First escape HTML
    code = html.escape(code)
    
    # Store all protected regions (comments and strings)
    protected_regions = []
    
    # Function to protect content
    def protect_region(content):
        protected_regions.append(content)
        return f"___PROTECTED_{len(protected_regions) - 1}___"
    
    # Extract and protect multi-line comments
    code = re.sub(r'/\*[\s\S]*?\*/', lambda m: protect_region(m.group(0)), code)
    
    # Extract and protect single-line comments
    code = re.sub(r'//[^\n]*', lambda m: protect_region(m.group(0)), code)
    
    # Extract and protect strings
    code = re.sub(r'"(?:[^"\\]|\\.)*"', lambda m: protect_region(m.group(0)), code)
    
    # Now apply syntax highlighting to unprotected code
    # Keywords
    keywords = ['class', 'public', 'private', 'protected', 'static', 'void', 'int', 'string', 'bool', 'double', 
                'float', 'long', 'using', 'namespace', 'if', 'else', 'for', 'while', 'foreach', 'in', 'return',
                'new', 'this', 'base', 'virtual', 'override', 'abstract', 'interface', 'struct', 'enum', 'const',
                'readonly', 'var', 'ref', 'out', 'params', 'async', 'await', 'try', 'catch', 'finally', 'throw']
    
    # Types
    types = ['List', 'Dictionary', 'Queue', 'Stack', 'TreeNode', 'Node', 'Array', 'LinkedList', 'HashSet', 'IEnumerable', 'IList', 'ICollection']
    
    # Highlight keywords
    for keyword in keywords:
        code = re.sub(r'\b' + keyword + r'\b', 
                     r'<span style="color:#0066cc;font-weight:bold;">' + keyword + r'</span>', code)
    
    # Highlight types
    for type_name in types:
        code = re.sub(r'\b' + type_name + r'\b', 
                     r'<span style="color:#008000;font-weight:bold;">' + type_name + r'</span>', code)
    
    # Highlight numbers (but not inside HTML tags or protected regions)
    # Use negative lookbehind and lookahead to avoid matching numbers inside style attributes
    code = re.sub(r'(?<![#\w])(\d+)(?![a-f0-9])', r'<span style="color:#098658;">\1</span>', code)
    
    # Restore protected regions with appropriate colors
    for i, region in enumerate(protected_regions):
        placeholder = f"___PROTECTED_{i}___"
        if region.startswith('//') or region.startswith('/*'):
            # Comment - green
            colored = f'<span style="color:#008000;">{region}</span>'
        else:
            # String - pink
            colored = f'<span style="color:#d63384;">{region}</span>'
        code = code.replace(placeholder, colored)
    
    return code

def camel_to_space(name):
    """Convert camelCase to space-separated string"""
    # Insert space before uppercase letters
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    # Insert space before numbers
    result = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', result)
    # Insert space after numbers
    result = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', result)
    return result.strip()

def extract_comment_block(file_path):
    """Extract the initial comment block from a C# file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match /* */ or // comments at the start
        match = re.match(r'(/\*[\s\S]*?\*/|//.*(\n//.*)*)', content)
        if match:
            comment = match.group(0)
            # Clean up comment markers
            comment = re.sub(r'/\*\s*|\s*\*/', '', comment)
            comment = re.sub(r'^\s*//\s?', '', comment, flags=re.MULTILINE)
            # Remove data-source-line attributes and other similar artifacts
            comment = re.sub(r'\{data-source-line=["\']?\d+["\']?\}\s*', '', comment)
            # Remove any remaining curly brace patterns
            comment = re.sub(r'\{[^}]*\}', '', comment)
            return comment.strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def extract_code(file_path):
    """Extract code from C# file (remove leading comments)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove initial comment block
        content = re.sub(r'^(/\*[\s\S]*?\*/|//.*(\n//.*)*)\n*', '', content)
        return content.strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def escape_html(text):
    """Escape HTML special characters"""
    return html.escape(text)

def process_folder_tree(folder_path, html_content="", heading_level=2, counters=None, parent_number=""):
    """Recursively process folder structure and generate HTML"""
    
    if counters is None:
        counters = {}
    
    folder_path = Path(folder_path)
    items = sorted(folder_path.iterdir())
    
    # Separate folders and files
    subfolders = [item for item in items if item.is_dir()]
    cs_files = sorted([item for item in items if item.is_file() and item.suffix == '.cs'])
    
    # Initialize counter for current level if not exists
    if heading_level not in counters:
        counters[heading_level] = 0
    
    # Process C# files in current folder
    if cs_files:
        for cs_file in cs_files:
            counters[heading_level] += 1
            file_name = cs_file.stem
            # Convert camelCase to readable format
            readable_name = camel_to_space(file_name)
            
            # Create numbering
            current_number = f"{parent_number}{counters[heading_level]}." if parent_number else f"{counters[heading_level]}."
            
            # Add file heading with color (blue)
            heading_tag = f"h{min(6, heading_level + 1)}"
            html_content += f"<{heading_tag} style='color:#0066cc; margin-top:20px; margin-bottom:10px;'>{current_number} {readable_name}</{heading_tag}>\n"
            
            # Extract and add problem statement
            comment_block = extract_comment_block(str(cs_file))
            if comment_block:
                html_content += "<h5 style='color:#333; margin-top:15px; margin-bottom:8px;'>📋 Problem Statement</h5>\n"
                html_content += f"<blockquote style='color:#555; font-style:italic; border-left:4px solid #0066cc; padding-left:15px; margin:10px 0; line-height:1.6;'>\n"
                html_content += f"{escape_html(comment_block)}\n"
                html_content += "</blockquote>\n"
            
            # Extract and add code
            code = extract_code(str(cs_file))
            if code:
                html_content += "<h5 style='color:#333; margin-top:15px; margin-bottom:8px;'>💻 Solution</h5>\n"
                highlighted_code = highlight_csharp(code)
                html_content += f"<pre style='background-color:#f5f5f5; border:1px solid #ddd; border-radius:4px; padding:12px; overflow-x:auto; font-family:\"Courier New\", monospace; font-size:12px; line-height:1.4;'>{highlighted_code}</pre>\n"
    
    # Process subfolders recursively
    for subfolder in subfolders:
        counters[heading_level] += 1
        subfolder_name = subfolder.name
        # Convert camelCase to readable format
        readable_name = camel_to_space(subfolder_name)
        
        # Create numbering
        current_number = f"{parent_number}{counters[heading_level]}." if parent_number else f"{counters[heading_level]}."
        
        # Add folder heading with color (green)
        heading_tag = f"h{min(6, heading_level)}"
        html_content += f"<{heading_tag} style='color:#009900; margin-top:25px; margin-bottom:12px; border-bottom:2px solid #009900; padding-bottom:8px;'>📁 {current_number} {readable_name}</{heading_tag}>\n"
        
        # Recursively process subfolder
        # Reset counter for next level
        if (heading_level + 1) in counters:
            del counters[heading_level + 1]
        
        html_content = process_folder_tree(subfolder, html_content, heading_level + 1, counters, current_number)
        
        html_content += "<hr style='border:none; border-top:1px solid #ddd; margin:20px 0;'>\n"
    
    return html_content

def generate_pdf(dsa_folder_path, output_file_path):
    """Generate PDF file from DSA folder structure"""
    
    # HTML header with styling
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DSA Revision Notes</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #fff;
            padding: 40px;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        h1 {
            color: #1a1a1a;
            font-size: 2.5em;
            margin-bottom: 10px;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 15px;
        }
        
        .header-subtitle {
            color: #cc0000;
            font-weight: bold;
            margin-bottom: 30px;
            font-size: 0.9em;
        }
        
        h2, h3, h4, h5, h6 {
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        h2 {
            font-size: 1.8em;
        }
        
        h3 {
            font-size: 1.5em;
        }
        
        h4 {
            font-size: 1.3em;
        }
        
        h5 {
            font-size: 1.1em;
            margin: 10px 0 5px 0;
        }
        
        blockquote {
            border-left: 4px solid #0066cc;
            padding-left: 15px;
            margin: 5px 0 10px 0;
            color: #555;
            font-style: italic;
            background-color: #f9f9f9;
            padding: 10px 15px;
        }
        
        pre {
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 12px;
            overflow-x: auto;
            margin: 0 0 15px 0;
            font-size: 12px;
            line-height: 1.4;
        }
        
        code {
            font-family: "Courier New", Courier, monospace;
            background-color: #f5f5f5;
            padding: 2px 6px;
            border-radius: 3px;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
        }
        
        hr {
            border: none;
            border-top: 1px solid #ddd;
            margin: 30px 0;
        }
        
        @media print {
            body {
                padding: 20px;
            }
            
            h1 {
                page-break-after: avoid;
            }
            
            h2 {
                page-break-after: avoid;
            }
            
            h3, h4 {
                page-break-before: always;
                page-break-after: avoid;
            }
            
            h5 {
                page-break-inside: avoid;
                page-break-after: avoid;
                margin: 0 0 5px 0;
            }
            
            blockquote {
                page-break-inside: avoid;
                margin: 0 0 10px 0;
                padding: 10px 15px;
            }
            
            pre {
                page-break-inside: avoid;
                margin: 0 0 20px 0;
            }
            
            hr {
                page-break-after: avoid;
            }
        }
    </style>
</head>
<body>
    <h1>📚 DSA Revision Notes</h1>
    <div class="header-subtitle">Last Updated: January 12, 2026</div>
    <hr>
    
"""
    
    dsa_path = Path(dsa_folder_path)
    
    if not dsa_path.exists():
        print(f"Error: DSA folder not found at {dsa_folder_path}")
        return
    
    # Process the folder tree starting from Code subfolder
    code_folder = dsa_path / "Code"
    if code_folder.exists():
        html_content += process_folder_tree(code_folder, "", heading_level=2)
    else:
        print(f"Warning: 'Code' subfolder not found in {dsa_folder_path}")
        html_content += process_folder_tree(dsa_path, "", heading_level=2)
    
    # HTML footer
    html_content += """
</body>
</html>
"""
    
    # Write to output file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✓ PDF file generated successfully at: {output_file_path}")
        print(f"\n📖 To view the PDF:")
        print(f"   1. Open the file in your browser: {output_file_path}")
        print(f"   2. Press Ctrl+P to open the print dialog")
        print(f"   3. Select 'Save as PDF' as the printer")
        print(f"   4. Click 'Save' to save the PDF")
    except Exception as e:
        print(f"Error writing to {output_file_path}: {e}")

# Usage
if __name__ == "__main__":
    dsa_folder = r"d:\Kundan\Study\MAANG\DSA"
    output_file = r"d:\Kundan\Study\MAANG\DSA\RevisionNotes.html"
    
    generate_pdf(dsa_folder, output_file)
