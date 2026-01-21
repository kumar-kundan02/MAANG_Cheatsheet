import os
import re
from pathlib import Path

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

def process_folder_tree(folder_path, markdown_content="", heading_level=2, counters=None, parent_number=""):
    """Recursively process folder structure and generate markdown"""
    
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
            markdown_content += f"{'#' * (heading_level + 1)} <span style='color:#0066cc'>{current_number} {readable_name}</span>\n\n"
            
            # Extract and add problem statement
            comment_block = extract_comment_block(str(cs_file))
            if comment_block:
                markdown_content += "##### 📋 Problem Statement\n\n"
                markdown_content += "> <span style='color:#555555'>\n"
                # Don't use backticks, just plain text with proper formatting
                markdown_content += "> " + comment_block.replace("\n", "\n> ") + "\n"
                markdown_content += "> </span>\n\n"
            
            # Extract and add code
            code = extract_code(str(cs_file))
            if code:
                markdown_content += "##### 💻 Solution\n\n"
                markdown_content += "````csharp\n"
                markdown_content += code + "\n"
                markdown_content += "````\n\n"
    
    # Process subfolders recursively
    for subfolder in subfolders:
        counters[heading_level] += 1
        subfolder_name = subfolder.name
        # Convert camelCase to readable format
        readable_name = camel_to_space(subfolder_name)
        
        # Create numbering
        current_number = f"{parent_number}{counters[heading_level]}." if parent_number else f"{counters[heading_level]}."
        
        # Add folder heading with color (green)
        markdown_content += f"{'#' * heading_level} <span style='color:#009900'>📁 {current_number} {readable_name}</span>\n\n"
        
        # Recursively process subfolder
        # Reset counter for next level
        if (heading_level + 1) in counters:
            del counters[heading_level + 1]
        
        markdown_content = process_folder_tree(subfolder, markdown_content, heading_level + 1, counters, current_number)
        
        markdown_content += "---\n\n"
    
    return markdown_content

def generate_markdown(dsa_folder_path, output_file_path):
    """Generate markdown file from DSA folder structure"""
    
    markdown_content = """# 📚 DSA Revision Notes

> <span style='color:#cc0000'>**Last Updated:** January 12, 2026</span>

---

"""
    
    dsa_path = Path(dsa_folder_path)
    
    if not dsa_path.exists():
        print(f"Error: DSA folder not found at {dsa_folder_path}")
        return
    
    # Process the folder tree starting from Code subfolder
    code_folder = dsa_path / "Code"
    if code_folder.exists():
        markdown_content = process_folder_tree(code_folder, markdown_content, heading_level=2)
    else:
        print(f"Warning: 'Code' subfolder not found in {dsa_folder_path}")
        markdown_content = process_folder_tree(dsa_path, markdown_content, heading_level=2)
    
    # Write to output file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✓ Markdown file generated successfully at: {output_file_path}")
    except Exception as e:
        print(f"Error writing to {output_file_path}: {e}")

# Usage
dsa_folder = r"d:\Kundan\Study\MAANG\DSA"
output_file = r"d:\Kundan\Study\MAANG\DSA\RevisionNotes.md"

generate_markdown(dsa_folder, output_file)