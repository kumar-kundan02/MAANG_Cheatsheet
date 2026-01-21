# 📚 DSA Revision Notes

> <span style='color:#cc0000'>**Last Updated:** January 12, 2026</span>

---

## <span style='color:#009900'>📁 1. BST</span>

#### <span style='color:#0066cc'>1.1. Check If BST</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root node of a binary tree. Return true if the given binary tree is a binary search tree(BST) else false.
> A valid BST is defined as follows:
> The left subtree of a node contains only nodes with key strictly less than the node's key.
> The right subtree of a node contains only nodes with key strictly greater than the node's key.
> Both the left and right subtrees must also be binary search trees.
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int data;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.data = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
   public bool IsBST(TreeNode root) {
        return ValidateBST(root, new List<int>());

    }

    private bool ValidateBST(TreeNode root, List<int> lst)
    {
        if(root == null) return true;

        if(!ValidateBST(root.left, lst)) 
        {
            return false;
        }
        if(lst.Count > 0 && root.data <= lst[lst.Count-1])
            return false;
        lst.Add(root.data);
        return ValidateBST(root.right, lst);
    }
}
````

#### <span style='color:#0066cc'>1.2. Find Ceil And Floor</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a root of binary search tree and a key(node) value, find the floor and ceil value for that particular key value.
> 
> Floor Value Node: Node with the greatest data lesser than or equal to the key value. 
> Ceil Value Node: Node with the smallest data larger than or equal to the key value.
> If a particular floor or ceil value is not present then output -1.
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int data;
 *     public TreeNode left;
 *     public TreeNode right;
 *      public TreeNode(int val) {
 *          data = val;
 *          left = null;
 *          right = null;
 *      }
 * };
 **/

public class Solution {
    public List<int> FloorCeilOfBST(TreeNode root, int key) {
        // Approach: I need to find the floor and ceil separately
        // We need to keep moving untill encounter either exactly key or null

        List<int> res = new List<int>();
        int floor = -1, ceil = -1;
        TreeNode currentNode = root;

        // find floor
        while(currentNode != null)
        {
            if(currentNode.data == key)
            {
                floor = currentNode.data;
                break;
            }
            else if(key > currentNode.data)
            {
                floor = currentNode.data;
                currentNode = currentNode.right;
            }
            else
            {
                currentNode = currentNode.left;
            }
        }

        // Finding Ceil
        currentNode = root;
        while(currentNode != null)
        {
            if(currentNode.data == key)
            {
                ceil = currentNode.data;
                break;
            }
            else if(key < currentNode.data)
            {
                ceil = currentNode.data;
                currentNode = currentNode.left;
            }
            else
            {
                currentNode = currentNode.right;
            }
        }

        res.Add(floor);
        res.Add(ceil);

        return res;
    }
}
````

#### <span style='color:#0066cc'>1.3. Insert Node</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root node of a binary search tree (BST) and a value val to insert into the tree. Return the root node of the BST after the insertion.
> It is guaranteed that the new value does not exist in the original BST. Note that the compiler output shows true if the node is added correctly, else false.
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// Using Recursion

public class Solution {
    public TreeNode InsertIntoBST(TreeNode root, int val) {

        if(root == null)
        {
            return new TreeNode(val);
        }

        if(val < root.val)
        {
            root.left = InsertIntoBST(root.left, val);
        }
        else
        {
            root.right = InsertIntoBST(root.right, val);
        }

        return root;
    }
}

// Using Iterative Approach
public class Solution
{
    public TreeNode InsertIntoBST(TreeNode root, int val)
    {
        // Your code goes here

        TreeNode current = root;
        TreeNode lastNode = null;
        TreeNode nodeToAdd = new TreeNode(val);

        while (current != null)
        {
            if (val < current.val)
            {
                lastNode = current;
                current = current.left;
            }
            else if (val > current.val)
            {
                lastNode = current;
                current = current.right;
            }
        }

        if (val > lastNode.val)
        {
            lastNode.right = nodeToAdd;
        }
        else if (val < lastNode.val)
        {
            lastNode.left = nodeToAdd;
        }

        return root;

    }
}
````

#### <span style='color:#0066cc'>1.4. Kth Smallest Largest</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root node of a binary search tree (BST) and an integer k.
> Return the kth smallest and largest value (1-indexed) of all values of the nodes in the tree.
> Return the 1st integer as kth smallest and 2nd integer as kth largest in the returned array.
> </span>

##### 💻 Solution

````csharp
/** Definition for a binary tree node.
* public class TreeNode {
*     public int Data;
*     public TreeNode Left;
*     public TreeNode Right;
*     public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
*       Data = val;
*       Left = left;
*       Right = right;
*   }
*}
*/

public class Solution {
    public List<int> KLargesSmall(TreeNode root, int k) {
        // Do the Inorder traversal to get the sorted Array
        // Find the kth smallest and largest from the array

        List<int> lst = new List<int>();
        Traverse(root, lst);

        List<int> res = new List<int>();
        res.Add(lst[k-1]);
        res.Add(lst[lst.Count - k]);

        return res;
    }

    private void Traverse(TreeNode root, List<int> lst)
    {
        if(root == null)
            return;
        
        Traverse(root.Left, lst);
        lst.Add(root.Data);
        Traverse(root.Right, lst);
    }
}
````

---

## <span style='color:#009900'>📁 2. Dynamic Programming</span>

#### <span style='color:#0066cc'>2.1. 0_1_Knapsack</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two integer arrays, val and wt, each of size N, which represent the values 
> and weights of N items respectively, and an integer W representing the maximum 
> capacity of a knapsack, determine the maximum value achievable by selecting a subset 
> of the items such that the total weight of the selected items does not exceed 
> the knapsack capacity W.
> 
> Each item can either be picked in its entirety or not picked at all (0-1 property). 
> The goal is to maximize the sum of the values of the selected items while keeping 
> the total weight within the knapsack's capacity.
> 
> Examples:
> Input: val = [60, 100, 120], wt = [10, 20, 30], W = 50
> Output: 220
> 
> Explanation: Select items with weights 20 and 30 for a total value of 100 + 120 = 220.
> 
> Input: val = [10, 40, 30, 50], wt = [5, 4, 6, 3], W = 10
> Output: 90
> 
> Explanation: Select items with weights 4 and 3 for a total value of 40 + 50 = 90.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int knapsack01(int[] wt, int[] val, int n, int W)
    {
        int[,] dp = new int[n+1, W+1];

        return Solve(wt, val,W, 0, dp);
    }

    private int Solve(int[] wt, int[] val, int cw, int pos, int[,] dp)
    {
        if(cw <= 0 || pos >= wt.Length)
            return 0;

        if(dp[pos,cw] != 0)
            return dp[pos,cw];

        int p1 = 0;
        if(cw >= wt[pos])
        {
            p1 = val[pos] + Solve(wt, val, cw-wt[pos], pos+1, dp);
        }

        int p2 = Solve(wt, val, cw, pos+1, dp);
        dp[pos, cw] = Math.Max(p1, p2); 

        return dp[pos,cw];
        
    }
}
````

#### <span style='color:#0066cc'>2.2. Ninja Training</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> A ninja has planned a n-day training schedule. Each day he has to perform one of three activities - running, stealth training, or fighting practice. The same activity cannot be done on two consecutive days and the ninja earns a specific number of merit points, based on the activity and the given day.
> 
> Given a n x 3-sized matrix, where matrix[i][0], matrix[i][1], and matrix[i][2], represent the merit points associated with running, stealth and fighting practice, on the (i+1)th day respectively. Return the maximum possible merit points that the ninja can earn.
> 
> Examples:
> Input: matrix = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
> 
> Output: 210
> 
> Explanation:
> 
> Day 1: fighting practice = 70
> 
> Day 2: stealth training = 50
> 
> Day 3: fighting practice = 90
> 
> Total = 70 + 50 + 90 = 210
> 
> This gives the optimal points.
> 
> Input: matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
> 
> Output: 290
> 
> Explanation:
> 
> Day 1: running = 70
> 
> Day 2: stealth training = 20
> 
> Day 3: running = 200
> 
> Total = 70 + 20 + 200 = 290
> 
> This gives the optimal points.
> 
> Input: matrix = [[20, 10, 10], [20, 10, 10], [20, 30, 10]]
> 
> Output:
> 60
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int NinjaTraining(int[][] matrix)
    {
        int m = matrix.Length, n = matrix[0].Length;
        int res = 0;
        int[,] dp = new int[m+1,n];
        
        // Call for all the combinations
        for(int i=0; i<3; i++)
        {
            ResetDpArray(dp, m+1, n);
            res = Math.Max(res, Solve(matrix, 0, i, dp)); 
        }

        return res;
    }

    private void ResetDpArray(int[,] dp, int m, int n)
    {
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i,j] = -1;
            }
        }
    }

    private int Solve(int[][] matrix,  int idx, int j, int[,] dp)
    {
        if(idx == matrix.Length)
        {
            return 0;
        }

        if(dp[idx,j] != -1) return dp[idx,j];

        // explore all the choices
        int p = 0;
        for(int k=0; k<3; k++)
        {
            if(k == j)
                continue;
            p = Math.Max(matrix[idx][j] + Solve(matrix, idx+1, k, dp), p);
        }

        return dp[idx,j] = p;
    }
}
````

### <span style='color:#009900'>📁 2.3. 1 D_DP</span>

##### <span style='color:#0066cc'>2.3.1. Climb Stairs</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an integer n, there is a staircase with n steps, starting from the 0th step.
> 
> 
> 
> Determine the number of unique ways to reach the nth step, given that each move can be either 1 or 2 steps at a time.
> 
> 
> Examples:
> Input: n = 2
> 
> Output: 2
> 
> Explanation:
> 
> There are 2 unique ways to climb to the 2nd step:
> 
> 1) 1 step + 1 step
> 
> 2) 2 steps
> 
> Input: n = 3
> 
> Output: 3
> 
> Explanation:
> 
> There are 3 unique ways to climb to the 3rd step:
> 
> 1) 1 step + 1 step + 1 step
> 
> 2) 2 steps + 1 step
> 
> 3) 1 step + 2 steps
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n+1];
        Array.Fill(dp, -1);
        return dp[n] = Solve(n, dp);
    }

    private int Solve(int n, int[] dp)
    {
        if(n == 0) return 1;

        if(n < 0) return 0;

        if(dp[n] != -1) return dp[n];
        return dp[n] = Solve(n-1, dp) + Solve(n-2, dp);
    }
}
````

##### <span style='color:#0066cc'>2.3.2. Frog Jump</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> A frog wants to climb a staircase with n steps. Given an integer array heights, where heights[i] contains the height of the ith step.
> 
> To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy, where abs() denotes the absolute difference. The frog can jump from any step either one or two steps, provided it exists.
> 
> Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.
> 
> Examples:
> Input: heights = [2, 1, 3, 5, 4]
> 
> Output: 2
> 
> Explanation:
> 
> One possible route can be,
> 
> 0th step -> 2nd Step = abs(2 - 3) = 1
> 
> 2nd step -> 4th step = abs(3 - 4) = 1
> 
> Total = 1 + 1 = 2.
> 
> Input: heights = [7, 5, 1, 2, 6]
> 
> Output: 9
> 
> Explanation:
> 
> One possible route can be,
> 
> 0th step -> 1st Step = abs(7 - 5) = 2
> 
> 1st step -> 3rd step = abs(5 - 2) = 3
> 
> 3rd step -> 4th step = abs(2 - 6) = 4
> 
> Total = 2 + 3 + 4 = 9.
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    public int frogJump(int[] heights)
    {
        int n = heights.Length;
        int[] dp = new int[n];
        Array.Fill(dp, -1);

        return Solve(heights, n-1, dp);
    }

    private int Solve(int[] heights, int step, int[] dp)
    {
        if(step == 0) return 0;

        if(dp[step] != -1) return dp[step];

        int energy1 = Math.Abs(heights[step] - heights[step-1]) + Solve(heights, step-1, dp);
        int energy2 = int.MaxValue;

        if(step > 1)
        {
            energy2 = Math.Abs(heights[step] - heights[step-2]) + Solve(heights, step-2, dp); 
        }
        return dp[step] = Math.Min(energy1, energy2);
    }
}
````

##### <span style='color:#0066cc'>2.3.3. Frog Jump KDistances</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> A frog wants to climb a staircase with n steps. Given an integer array heights, where heights[i] contains the height of the ith step, and an integer k.
> 
> To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy, where abs() denotes the absolute difference. The frog can jump from the ith step to any step in the range [i + 1, i + k], provided it exists.
> 
> Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.
> 
> Examples:
> Input: heights = [10, 5, 20, 0, 15], k = 2
> 
> Output: 15
> 
> Explanation:
> 
> 0th step -> 2nd step, cost = abs(10 - 20) = 10
> 
> 2nd step -> 4th step, cost = abs(20 - 15) = 5
> 
> Total cost = 10 + 5 = 15.
> 
> Input: heights = [15, 4, 1, 14, 15], k = 3
> 
> Output: 2
> 
> Explanation:
> 
> 0th step -> 3rd step, cost = abs(15 - 14) = 1
> 
> 3rd step -> 4th step, cost = abs(14 - 15) = 1
> 
> Total cost = 1 + 1 = 2.
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public int frogJump(int[] heights, int k) {
        int n = heights.Length;
        int[] dp = new int[n];
        Array.Fill(dp, -1);

        return Solve(heights, k, n-1, dp);
    }

    private int Solve(int[] heights, int k, int i, int[] dp)
    {
        if(i == 0) return 0;

        if(dp[i] != -1) return dp[i];

        int res = int.MaxValue;
        for(int m=k; m>0; m--)
        {
            if(i-m >= 0 )
            {
                res = Math.Min(res, Math.Abs(heights[i-m] - heights[i]) + Solve(heights, k, i-m, dp));
            }
        }

        return dp[i] = res;
    }
}
````

##### <span style='color:#0066cc'>2.3.4. House Robber</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> A robber is targeting to rob houses from a street. Each house has security measures that alert the police when two adjacent houses are robbed. The houses are arranged in a circular manner, thus the first and last houses are adjacent to each other.
> 
> Given an integer array money, where money[i] represents the amount of money that can be looted from the (i+1)th house. Return the maximum amount of money that the robber can loot without alerting the police.
> 
> Examples:
> Input: money = [2, 1, 4, 9]
> 
> Output: 10
> 
> Explanation:
> 
> [2, 1, 4, 9] The underlined houses would give the maximum loot.
> 
> Note that we cannot loot the 1st and 4th houses together.
> 
> Input: money = [1, 5, 2, 1, 6]
> 
> Output: 11
> 
> Explanation:
> 
> [1, 5, 2, 1, 6] The underlined houses would give the maximum loot.
> </span>

##### 💻 Solution

````csharp
class Solution{
    public int HouseRobber(List<int> money) {

        if(money.Count == 1)
            return money[0];
            
        int n = money.Count;
        int[] dp1 = new int[n];
        Array.Fill(dp1, -1);
        int[] dp2 = new int[n];
        Array.Fill(dp2, -1);

        return Math.Max(Solve(money, n-2, 0, dp1), Solve(money, n-1, 1, dp2));
    }

    private int Solve(List<int> money, int end, int idx, int[] dp)
    {
        if(idx == end) return money[idx];

        if(idx > end) return 0;

        if(dp[idx] != -1) return dp[idx];

        // Not Pick
        int res2 = Solve(money, end, idx+1, dp);

        // pick
        int res1 = money[idx] + Solve(money, end, idx+2, dp);
        
        return dp[idx] = Math.Max(res1, res2);
    }
}
````

##### <span style='color:#0066cc'>2.3.5. Max Sum Non Adjacent Elements</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an integer array nums of size n. Return the maximum sum possible using the elements of nums such that no two elements taken are adjacent in nums.
> 
> Examples:
> Input: nums = [1, 2, 4]
> 
> Output: 5
> 
> Explanation:
> 
> [1, 2, 4], the underlined elements are taken to get the maximum sum.
> 
> Input: nums = [2, 1, 4, 9]
> 
> Output: 11
> 
> Explanation:
> 
> [2, 1, 4, 9], the underlined elements are taken to get the maximum sum.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int NonAdjacent(int[] nums)
    {
        int[] dp = new int[nums.Length];
        Array.Fill(dp, -1);

        return Solve(nums, 0, dp);
    }

    private int Solve(int[] nums, int idx, int[] dp)
    {
        if(idx >= nums.Length) return 0;

        if(dp[idx] != -1) return dp[idx];
        // Pick 
        int res1 = nums[idx] + Solve(nums, idx+2, dp);

        // not pick
        int res2 = Solve(nums, idx+1, dp);

        return dp[idx] = Math.Max(res1, res2);
    }
}
````

---

### <span style='color:#009900'>📁 2.4. DP_Grids</span>

##### <span style='color:#0066cc'>2.4.1. Cherry Pick 2</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a n x m 2d integer array called matrix where matrix[i][j] represents the number of cherries you can pick up from the (i, j) cell.Given two robots that can collect cherries, one is located at the top-leftmost (0, 0) cell and the other at the top-rightmost (0, m-1) cell.
> 
> Return the maximum number of cherries that can be picked by the two robots in total, following these rules:
> 
> Robots that are standing on (i, j) cell can only move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1), if it exists in the matrix.
> 
> A robot will pick up all the cherries in a given cell when it passes through that cell.
> 
> If both robots come to the same cell at the same time, only one robot takes the cherries.
> 
> Both robots must reach the bottom row in matrix.
> 
> Examples:
> Input: matrix = [[2, 1, 3], [4, 2, 5], [1, 6, 2], [7, 2, 8]]
> 
> Output: 37
> 
> Explanation:
> 
> Possible left robot path:-
> 
> Start at 0th cell (2) -> down (4) -> down-right (6) ->down-left (7)
> 
> Possible right robot path:-
> 
> Start at 2nd cell (3) -> down (5) -> down (2) -> down (8)
> 
> Input: matrix = [[1, 4, 4, 1], [1, 2, 2, 1], [5, 6, 10, 11], [8, 1, 1, 1]]
> 
> Output: 32
> 
> Explanation:
> 
> Possible left robot path:-
> 
> Start at 0th cell (1) -> down-right (2) -> down (6) ->down-left (8)
> 
> Possible right robot path:-
> 
> Start at 3rd cell (1) -> down-left (2) -> down-right (11) -> down (1)
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    public int CherryPickup(int[][] matrix)
    {
        int m = matrix.Length, n = matrix[0].Length;

        int[,,] dp = new int[m,n,n];

        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                for(int k=0; k<n; k++)
                {
                    dp[i,j,k] = -1;
                }
            }
        }

        return Solve(matrix, 0, 0, n-1, dp);

    }

    private int Solve(int[][] matrix, int i, int j, int k, int[,,] dp)
    {
        if(matrix[0].Length <= j || j < 0 || k < 0 || matrix[0].Length <= k) return int.MinValue;

        
        if(matrix.Length-1 == i) 
        {
            if(j == k)
                return matrix[i][j];
            else
                return matrix[i][k] + matrix[i][j];
        }

        if(dp[i,j,k] != -1) return dp[i,j,k];

        int maxVal = int.MinValue;
        int ans = 0;

        // Explore all the paths direction => 3 * 3 = 9 directions
        for(int m =- 1; m <= 1; m++)
        {
            for(int n = -1; n <= 1; n++)
            {
                if(j == k)
                {
                    ans = matrix[i][j] + Solve(matrix, i+1, j+m, k+n, dp);
                }
                else
                {
                    ans = matrix[i][j] + matrix[i][k] + Solve(matrix, i+1, j+m, k+n, dp);
                }

                maxVal = Math.Max(ans, maxVal);
            }
        }

        return dp[i,j,k] = maxVal;
        
    }
}
````

##### <span style='color:#0066cc'>2.4.2. Grid Unique Paths</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two integers m and n, representing the number of rows and columns of a 2d array named matrix. Return the number of unique ways to go from the top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).
> 
> Movement is allowed only in two directions from a cell: right and bottom.
> 
> Examples:
> Input: m = 3, n = 2
> 
> Output: 3
> 
> Explanation:
> 
> There are 3 unique ways to go from the top left to the bottom right cell.
> 
> 1) right -> down -> down
> 
> 2) down -> right -> down
> 
> 3) down -> down -> right
> 
> Input: m = 2, n = 4
> 
> Output: 4
> 
> Explanation:
> 
> There are 4 unique ways to go from the top left to the bottom right cell.
> 
> 1) down -> right -> right -> right
> 
> 2) right -> down -> right -> right
> 
> 3) right -> right -> down -> right
> 
> 4) right -> right -> right -> down
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public int uniquePaths(int m, int n) {
        int[,] dp = new int[m,n];
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i,j] = -1;
            }
        }
        return Solve(m, n, 0, 0, dp);
    }

    private int Solve(int m, int n, int i, int j, int[,] dp)
    {
        if(i >= m || j >= n) return 0;

        if(i == m-1 && j == n-1) return 1;

        if(dp[i,j] != -1) return dp[i,j];

        return dp[i,j] = Solve(m, n, i+1, j, dp) + Solve(m, n, i, j+1, dp);
    }
}
````

##### <span style='color:#0066cc'>2.4.3. Minimum Falling Path Sum</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a 2d array called matrix consisting of integer values. Return the minimum path sum that can be obtained by starting at any cell in the first row and ending at any cell in the last row.
> 
> 
> 
> Movement is allowed only to the bottom, bottom-right, or bottom-left cell of the current cell.
> 
> 
> Examples:
> Input: matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
> 
> Output: 6
> 
> Explanation:
> 
> One optimal route can be:-
> 
> Start at 1st cell of 1st row -> bottom-right -> bottom -> bottom-left.
> 
> Input: matrix = [[1, 4, 3, 1], [2, 3, -1, -1], [1, 1, -1, 8]]
> 
> Output: -1
> 
> Explanation:
> 
> One optimal route can be:-
> 
> Start at 4th cell of 1st row -> bottom-left -> bottom.
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public int MinFallingPathSum(int[][] matrix) {
        int m = matrix.Length, n = matrix[0].Length;

        int[,] dp = new int[m,n];

        int res = int.MaxValue;

        // There is no need of doing Reset DP at each step. As it's not gonna disturb other solutions
        ResetDP(dp, m, n);

        for(int j=0; j<n; j++)
        {         
            res = Math.Min(res, Solve(matrix, 0, j, dp));
        }

        return res;
    }

    private int Solve(int[][] matrix, int i, int j, int[,] dp)
    {
        // Here return int.MaxValue it's output should be discarded. 
        // Since we are looking for minimum so, we will assign max value to discard it
        if(i >= matrix.Length || j >= matrix[0].Length || j < 0) return int.MaxValue;

        if(matrix.Length-1 == i) return matrix[i][j];

        if(dp[i,j] != -1) return dp[i,j];

        return dp[i,j] = matrix[i][j] + Math.Min(Solve(matrix, i+1,j, dp), Math.Min(Solve(matrix, i+1, j+1, dp), Solve(matrix, i+1, j-1, dp)));
    }

    private void ResetDP(int[,] dp, int m, int n)
    {
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i,j] = -1;
            }
        }
    }
}
````

##### <span style='color:#0066cc'>2.4.4. Triangle Falling Path</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a 2d integer array named triangle with n rows. Its first row has 1 element and each succeeding row has one more element in it than the row above it.
> 
> Return the minimum falling path sum from the first row to the last.
> 
> Movement is allowed only to the bottom or bottom-right cell from the current cell.
> 
> 
> Examples:
> Input: triangle = [[1], [1, 2], [1, 2, 4]]
> 
> Output: 3
> 
> Explanation:
> 
> One possible route can be:
> 
> Start at 1st row -> bottom -> bottom.
> 
> Input: triangle = [[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]
> 
> Output: -42
> 
> Explanation:
> 
> One possible route can be:
> 
> Start at 1st row -> bottom-right -> bottom-right -> bottom-right
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int MinTriangleSum(List<List<int>> triangle)
    {
        int m = triangle.Count, n = triangle.Count;

        int[,] dp = new int[m,n];

        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i,j] = -1;
            }
        }

        return Solve(triangle, 0, 0, dp); 
    }

    private int Solve(List<List<int>> triangle, int i, int j, int[,] dp)
    {
        if(triangle.Count <= i || j > i) return int.MaxValue;

        if(triangle.Count-1 == i) return triangle[i][j];

        if(dp[i,j] != -1) return dp[i,j];

        return dp[i,j] = triangle[i][j] + Math.Min(Solve(triangle, i+1, j, dp), Solve(triangle, i+1, j+1, dp));
    }
}
````

##### <span style='color:#0066cc'>2.4.5. Unique Paths With Obstacles</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an m x n 2d array named matrix, where each cell is either 0 or 1. Return the number of unique ways to go from the top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]). A cell is blocked if its value is 1, and no path is possible through that cell.
> 
> 
> 
> Movement is allowed in only two directions from a cell - right and bottom.
> 
> 
> Examples:
> Input: matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
> 
> Output: 2
> 
> Explanation:
> 
> The two possible paths are:
> 
> 1) down -> down-> right -> right
> 
> 2) right -> right -> down -> down
> 
> Input: matrix = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
> 
> Output: 0
> 
> Explanation:
> 
> There is no way to reach the bottom-right cell.
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public int UniquePathsWithObstacles(int[][] matrix) {
        int m = matrix.Length, n = matrix[0].Length;

        // Junt ensure that whether destination cell is rechable or not
        if(matrix[m-1][n-1] == 1) return 0;

        int[,] dp = new int[m,n];

        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i,j] = -1;
            }
        }

        return Solve(matrix, 0, 0, dp);
    }

    private int Solve(int[][] matrix, int i, int j, int[,] dp)
    {
        if(matrix.Length <= i || matrix[0].Length <= j) return 0;

        if(matrix.Length-1 == i && matrix[0].Length-1 == j) return 1;

        if(matrix[i][j] == 1) return dp[i,j] = 0;

        if(dp[i,j] != -1) return dp[i,j];

        return dp[i,j] = Solve(matrix, i+1, j, dp) + Solve(matrix, i, j+1, dp);
    }
}
````

---

### <span style='color:#009900'>📁 2.5. LCS</span>

##### <span style='color:#0066cc'>2.5.1. Distinct Subsequences_Bottom Up</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two strings s and t, return the number of distinct subsequences of s that equal t.
> 
> A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.
> 
> The task is to count how many different ways we can form t from s by deleting some (or no) characters from s. Return the result modulo 109+7.
> 
> Examples:
> Input: s = "axbxax", t = "axa"
> 
> Output: 2
> 
> Explanation: In the string "axbxax", there are two distinct subsequences "axa":
> 
> (a)(x)bx(a)x
> 
> (a)xb(x)(a)x
> 
> Input: s = "babgbag", t = "bag"
> Output: 5
> 
> Explanation: In the string "babgbag", there are five distinct subsequences "bag":
> 
> (ba)(b)(ga)(g)
> 
> (ba)(bg)(ag)
> 
> (bab)(ga)(g)
> 
> (bab)(g)(ag)
> 
> (babg)(a)(g)
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    private const int MOD = 1000000007;
    public int DistinctSubsequences(string s, string t)
    {
        int m = s.Length, n = t.Length;
        int[,] dp = new int[m+1, n+1];

        // Initialize Base case
        // if "t" is empty then there will be only one subsequence length i.e empty
        // if "s" is empty it means there is zero subsequence possible
        // i.e if len(s) == 0 then dp[0,j] = 0
        // if len(t) == 0 then dp[i,0] = 1. considering empty case

        for(int i=0; i<=m; i++)
        {
            dp[i,0] = 1;
        }

        // No need of this initialization as by default its zero only
        // Need to start with 1 as if both are of zero length then empty should be common to both so, it won't be zero  but one
        for(int j=1; j<=n; j++)
        {
            dp[0,j] = 0;
        }

        for(int i=1; i<=m; i++)
        {
            for(int j=1; j<=n; j++)
            {
                if(s[i-1] == t[j-1])
                {
                    dp[i,j] = (dp[i-1, j-1] % MOD + dp[i-1, j] % MOD) % MOD;
                }
                else
                {
                    dp[i,j] = dp[i-1, j] % MOD;
                }
            }
        } 

        return dp[m,n];
    }
}
````

##### <span style='color:#0066cc'>2.5.2. Distinct Subsequences_Recrusive</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two strings s and t, return the number of distinct subsequences of s that equal t.
> 
> A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.
> 
> The task is to count how many different ways we can form t from s by deleting some (or no) characters from s. Return the result modulo 109+7.
> 
> Examples:
> Input: s = "axbxax", t = "axa"
> 
> Output: 2
> 
> Explanation: In the string "axbxax", there are two distinct subsequences "axa":
> 
> (a)(x)bx(a)x
> 
> (a)xb(x)(a)x
> 
> Input: s = "babgbag", t = "bag"
> 
> Output: 5
> 
> Explanation: In the string "babgbag", there are five distinct subsequences "bag":
> 
> (ba)(b)(ga)(g)
> 
> (ba)(bg)(ag)
> 
> (bab)(ga)(g)
> 
> (bab)(g)(ag)
> 
> (babg)(a)(g)
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    private const int MOD = 1000000007;
    public int DistinctSubsequences(string s, string t)
    {
      int m = s.Length, n = t.Length;
        int[,] dp = new int[m, n];

        for(int i=0; i<m; i++)
        {
          for(int j=0; j<n; j++)
          {
            dp[i,j] = -1;
          }
        }
        return Solve(s, t, 0, 0, dp);
    }

    private int Solve(string s, string t, int i, int j, int[,] dp)
    {
       if(t.Length == j)
       {
          return 1;
       }

       if(s.Length == i)
       {
          return 0;
       }

       if(dp[i,j] != -1) return dp[i,j];

        if(s[i] == t[j])
        {
          // Need to add both the condition pick and not pick as we need to find all the subsequences
          return dp[i,j] = (Solve(s, t, i+1, j+1, dp) % MOD + Solve(s, t, i+1, j, dp) % MOD) % MOD;
        }
        else
        {
          return dp[i,j] = Solve(s, t, i+1, j, dp) % MOD;
        }
    }
}
````

##### <span style='color:#0066cc'>2.5.3. Edit Distance_Bottom Up</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two strings start and target, you need to determine the minimum number of operations required to convert the string start into the string target. The operations you can use are:
> 
> Insert a character: Add any single character at any position in the string.
> 
> Delete a character: Remove any single character from the string.
> 
> Replace a character: Change any single character in the string to another character.
> 
> The goal is to transform start into target using the fewest number of these operations.
> 
> Examples:
> Input: start = "planet", target = "plan"
> 
> Output: 2
> 
> Explanation: 
> 
> To transform "planet" into "plan", the following operations are required:
> 
> 1. Delete the character 'e': "planet" -> "plan"
> 
> 2. Delete the character 't': "plan" -> "plan"
> 
> Thus, a total of 2 operations are needed.
> 
> Input: start = "abcdefg", target = "azced"
> 
> Output: 4
> 
> Explanation: 
> 
> To transform "abcdefg" into "azced", the following operations are required:
> 
> 1. Replace 'b' with 'z': "abcdefg" -> "azcdefg"
> 
> 2. Delete 'd': "azcdefg" -> "azcefg"
> 
> 3. Delete 'f': "azcefg" -> "azceg"
> 
> 4. Replace 'g' with 'd': "azceg" -> "azced"
> 
> Thus, a total of 4 operations are needed.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int editDistance(string start, string target)
    {
        // Wrong Approach: Find LCS count
        // Now apply formula : ans = (start.Length - lcs) - (target.Length - lcs) XXXXX (Noooo, it won't work)

        // Correct Approach
        // Consider all the operations and then take minimum
        // No need to do the actual changes like insert/update/delete
        // But just simulate the scenarios and update the index values

        int m = start.Length, n = target.Length;
        int[,] dp = new int[m+1, n+1];

        // Initialize as if target.Length == 0 then need to remove all chars in start. hence dp[i,0] = i
        for(int i=0; i<=m; i++) {
            dp[i,0] = i;
        }

        // Initialize as if start.Length == 0 then need to remove all chars in target. hence dp[0,i] = i
        for(int i=1; i<=n; i++) {
            dp[0,i] = i;
        }

        for(int i=1; i<=m; i++)
        {
            for(int j=1; j<=n; j++)
            {
                if(start[i-1] == target[j-1])
                {
                    dp[i,j] = dp[i-1, j-1];
                }
                else
                {
                    dp[i,j] = 1 + Math.Min(dp[i,j-1], Math.Min(dp[i-1, j], dp[i-1, j-1]));
                } 
            }
        }

        return dp[m,n];
    }
}
````

##### <span style='color:#0066cc'>2.5.4. LCSubsequence</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two strings str1 and str2, find the length of their longest common subsequence.
> 
> A subsequence is a sequence that appears in the same relative order but not necessarily contiguous and a common subsequence of two strings is a subsequence that is common to both strings.
> 
> Examples:
> Input: str1 = "bdefg", str2 = "bfg"
> 
> Output: 3
> 
> Explanation: The longest common subsequence is "bfg", which has a length of 3.
> 
> Input: str1 = "mnop", str2 = "mnq"
> 
> Output: 2
> 
> Explanation: The longest common subsequence is "mn", which has a length of 2.
> </span>

##### 💻 Solution

````csharp
class Solution {
    public int Lcs(string str1, string str2)
    {
        int[,] dp = new int[str1.Length, str2.Length];
        for(int i=0; i<str1.Length; i++)
        {
            for(int j=0; j<str2.Length; j++)
            {
                dp[i,j] = -1;
            }
        }
        return LCS(str1, str2, 0, 0, dp);
    }

    private int LCS(string s1, string s2, int i, int j, int[,] dp)
    {
        if(s1.Length == i || s2.Length == j)
        {
            return 0;
        }

        if(dp[i,j] != -1)
            return dp[i,j];

        int res1 = 0, res2 = 0;
        if(s1[i] == s2[j])
        {
            res1 = 1 + LCS(s1, s2, i+1, j+1, dp);
        }
        else
        {
            res2 = Math.Max(LCS(s1, s2, i+1, j, dp), LCS(s1, s2, i, j+1, dp));
        }

        return dp[i,j] = Math.Max(res1, res2);
    }
}
````

##### <span style='color:#0066cc'>2.5.5. LCSubstring_Bottom UP</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two strings str1 and str2, find the length of their longest common substring.
> 
> A substring is a contiguous sequence of characters within a string.
> 
> Examples:
> Input: str1 = "abcde", str2 = "abfce"
> 
> Output: 2
> 
> Explanation: The longest common substring is "ab", which has a length of 2.
> 
> Input: str1 = "abcdxyz", str2 = "xyzabcd"
> 
> Output: 4
> 
> Explanation: The longest common substring is "abcd", which has a length of 4.
> 
> Input: str1 = "abcdef", str2 = "ghijkl"
> 
> Output:
> 0
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int longestCommonSubstr(string str1, string str2)
    {
        int m = str1.Length;
        int n = str2.Length;

        int[,] dp = new int [m+1,n+1];
        int maxLength = 0;

        // Here in indexes we are considering the length of substring 
        // That's why we are taking the startin index for i and j as "1"
        // But while comparing the string taking "i-1 and j-1" as in string it will work on Array based index
        for(int i=1; i<=m; i++)
        {
            for(int j=1; j<=n; j++)
            {
                if(str1[i-1] == str2[j-1])
                {
                    dp[i,j] = 1 + dp[i-1,j-1];
                }
                else
                {
                    dp[i,j] = 0;
                }

                maxLength = Math.Max(maxLength, dp[i,j]);
            }
        }

        return maxLength;
    }
}
````

##### <span style='color:#0066cc'>2.5.6. LCSubstring_Recursive</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two strings str1 and str2, find the length of their longest common substring.
> 
> A substring is a contiguous sequence of characters within a string.
> 
> Examples:
> Input: str1 = "abcde", str2 = "abfce"
> 
> Output: 2
> 
> Explanation: The longest common substring is "ab", which has a length of 2.
> 
> Input: str1 = "abcdxyz", str2 = "xyzabcd"
> 
> Output: 4
> 
> Explanation: The longest common substring is "abcd", which has a length of 4.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int longestCommonSubstr(string str1, string str2)
    {
        int[,,] dp = new int[str1.Length+1, str2.Length+1, Math.Min(str1.Length, str2.Length)+1];

        for(int i=0; i<=str1.Length; i++)
        {
            for(int j=0; j<=str2.Length; j++)
            {
                for(int k=0; k<= Math.Min(str1.Length, str2.Length); k++)
                {
                    dp[i,j,k] = -1;
                }
            }
        }
        return Solve(str1, str2, str1.Length-1, str2.Length-1, 0, dp);
    }

    private int Solve(string s1, string s2, int i, int j, int count, int[,,] dp)
    {
        if(i < 0 || j < 0)
        {
            return count;
        }

        if(dp[i,j,count] != -1) return dp[i,j,count];

        int res1 = 0;
        if(s1[i] == s2[j])
        {
            // Since we need to reset the sum if s[i] != s[j] so,
            // we are passing the count and incrementing in Param as
            // if I would have done it like "res1 = 1 + Solve(s1, s2, i-1, j-1)" then,
            // It will try to find the other solution there onwards with existing length
            // However it would work for Subsequence but not for substring
            // As for Substring we always need to reset the length if chars are not same
            res1 = Solve(s1, s2, i-1, j-1, count+1, dp); 
        }

        int res2 = Math.Max(Solve(s1, s2, i, j-1, 0, dp), Solve(s1, s2, i-1, j, 0, dp));
        return dp[i,j,count] = Math.Max(count, Math.Max(res1, res2));
    }
}
````

##### <span style='color:#0066cc'>2.5.7. Longest Palindrome</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a string, Find the longest palindromic subsequence length in given string.
> 
> A palindrome is a sequence that reads the same backwards as forward.
> 
> A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
> 
> 
> Examples:
> Input: s = "eeeme"
> 
> Output: 4
> 
> Explanation: The longest palindromic subsequence is "eeee", which has a length of 4.
> 
> Input: s = "annb"
> 
> Output: 2
> 
> Explanation: The longest palindromic subsequence is "nn", which has a length of 2.
> </span>

##### 💻 Solution

````csharp
class Solution {
    public int LongestPalinSubseq(string s) {
      
      // We just need to reverse the string and then apply LCS 
      // It will give longest Palindrome as after reversal it should be same only
      
      char[] rev_arr = s.ToCharArray();
      Array.Reverse(rev_arr);
      string rev_s = new string(rev_arr);

      return LCS(s, rev_s);
    }

    private int LCS(string s1, string s2)
    {
        int m = s1.Length, n = s2.Length;
        int[,] dp = new int[m+1, n+1];

        int maxLength = 0;

        for(int i=1; i<=m; i++)
        {
            for(int j=1; j<=n; j++)
            {
                if(s1[i-1] == s2[j-1])
                {
                    dp[i,j] = 1 + dp[i-1, j-1];
                }
                else
                {
                    dp[i,j] = Math.Max(dp[i, j-1], dp[i-1, j]);
                }

                maxLength = Math.Max(dp[i,j], maxLength);
            }
        }
        return maxLength;
    }
}
````

##### <span style='color:#0066cc'>2.5.8. Min Insert Delete To Convert</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two strings str1 and str2, find the minimum number of insertions and deletions in string str1 required to transform str1 into str2.
> 
> Insertion and deletion of characters can take place at any position in the string.
> 
> Examples:
> Input: str1 = "kitten", str2 = "sitting"
> 
> Output: 5
> 
> Explanation: To transform "kitten" to "sitting", delete "k" and insert "s" to get "sitten", then insert "i" to get "sittin", and insert "g" at the end to get "sitting".
> 
> Input: str1 = "flaw", str2 = "lawn"
> 
> Output: 2
> 
> Explanation: To transform "flaw" to "lawn", delete "f" and insert "n" at the end. Hence minimum number of operations required is 2".
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int minOperations(string str1, string str2)
    {
        int lcs = LCS(str1, str2);

        // if we take the difference of lcs with str1.Length and str2.Length and Add them
        // It will give total insert/delete count as these are extra elements other than LCS
        // So, To convert we need to do all these insert and delete operations
        return str1.Length - lcs + str2.Length - lcs;
    }

    private int LCS(string str1, string str2)
    {
        int m = str1.Length, n = str2.Length;
        int[,] dp = new int[m+1, n+1];

        for(int i=1; i<=m; i++)
        {
            for(int j=1; j<=n; j++)
            {
                if(str1[i-1] == str2[j-1])
                {
                    dp[i,j] = 1 + dp[i-1, j-1];
                }
                else
                {
                    dp[i,j] = Math.Max(dp[i,j-1], dp[i-1, j]);
                }
            }
        }

        return dp[m,n];
    }
}
````

##### <span style='color:#0066cc'>2.5.9. Min Insertion To Make Palindrome</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a string s, find the minimum number of insertions needed to make it a palindrome. A palindrome is a sequence that reads the same backward as forward. You can insert characters at any position in the string.
> 
> Examples:
> Input: s = "abcaa"
> 
> Output: 2
> 
> Explanation: Insert 2 characters "c", and "b" to make "abcacba", which is a palindrome.
> 
> Input: s = "ba"
> 
> Output: 1
> 
> Explanation: Insert "a" at the beginning to make "aba", which is a palindrome.
> </span>

##### 💻 Solution

````csharp
class Solution
{

    // If we Subtract the length of longest common subsequence from 
    // Actual string length then we will get the minimum count of insertions
    // Intution : Keep the Exixting palindromic Sequence intact and then for existing which are not part of 
    // Palindromic subsequence then these needs to be added at other places to make the complete string Palindrome

    public int minInsertion(string s)
    {
        char[] rev_arr = s.ToCharArray();
        Array.Reverse(rev_arr);
        string s_rev = new string(rev_arr);

        return s.Length - LCS(s, s_rev);
    }

    private int LCS(string s1, string s2)
    {
        int m = s1.Length;

        int[,] dp = new int[m+1, m+1];

        for(int i=1; i<=m; i++)
        {
            for(int j=1; j<=m; j++)
            {
                if(s1[i-1] == s2[j-1])
                {
                    dp[i,j] = 1 + dp[i-1, j-1];
                }
                else
                {
                    dp[i,j] = Math.Max(dp[i-1, j], dp[i, j-1]);
                }
            }
        }

        return dp[m,m];
    }
}
````

##### <span style='color:#0066cc'>2.5.10. Wild Card Matching</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a string str and a pattern pat, implement a pattern matching function that supports the following special characters:
> 
> '?' Matches any single character.
> 
> '*' Matches any sequence of characters (including the empty sequence).
> 
> The pattern must match the entire string.
> 
> Examples:
> Input: str = "xaylmz", pat = "x?y*z"
> 
> Output: true
> 
> Explanation: 
> 
> The pattern "x?y*z" matches the string "xaylmz":
> 
> - '?' matches 'a'
> 
> - '*' matches "lm"
> 
> - 'z' matches 'z'
> 
> Input: str = "xyza", pat = "x*z"
> 
> Output: false
> 
> Explanation: 
> 
> The pattern "x*z" does not match the string "xyza" because there is an extra 'a' at the end of the string that is not matched by the pattern.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public bool WildCard(string str, string pat)
    {
        int m = str.Length, n = pat.Length;
        int[,] dp = new int[m,n];

        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i,j] = -1;
            }
        }
        return Solve(str, pat, 0, 0, dp);
    }

    private bool Solve(string s, string p, int i, int j, int[,] dp)
    {
        // if both pattern and string reached till end or exhausted
        if(s.Length == i && p.Length == j)
        {
            return true;
        }

        // if pattern exhausted but not the string
        if(p.Length == j)
        {
            return false;
        }

        // if string exhausted but not the pattern
        if(s.Length == i)
        {
            // just validate if in pattern there is * in remianing pattern
            for(int k=j; k<p.Length; k++)
            {
                if(p[k] != '*')
                    return false;
            }

            return true;
        }

        if(dp[i,j] != -1) return dp[i,j] == 1;

        bool res = false;

        // If there is a match of chars
        if(s[i] == p[j] || p[j] == '?')
        {
            dp[i,j] = Solve(s, p, i+1, j+1, dp) ? 1 : 0;
        }

        else if(p[j] == '*')
        {
            // considering that in pattern there is * but it could be skipped 
            // as in string it might not be required to match with any char
            dp[i,j] = (Solve(s, p, i+1, j, dp) || Solve(s, p, i, j+1, dp)) ? 1 : 0;
        }

        return dp[i,j] == 1;
    }
}
````

---

### <span style='color:#009900'>📁 2.6. LIS</span>

##### <span style='color:#0066cc'>2.6.1. Count Total LIS</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an integer array nums, find the number of Longest Increasing Subsequences (LIS) in the array.
> 
> Examples:
> Input: nums = [1, 3, 5, 4, 7]
> 
> Output: 2
> 
> Explanation: There are two LIS of length 4:
> 
> [1, 3, 4, 7]
> 
> [1, 3, 5, 7].
> 
> Input: nums = [2, 2, 2, 2, 2]
> 
> Output: 5
> 
> Explanation: All elements are the same, so every single element can form an LIS of length 1. There are 5 such subsequences.
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    public int NumberOfLIS(int[] nums)
    {
        int[] dp = new int[nums.Length];

        // Need one count array to store the possible ways to create the same subsequences Length
        int[] count = new int[nums.Length];

        int maxLength = 0;

        for(int i=0; i<nums.Length; i++)
        {
            dp[i] = 1;
            count[i] = 1;

            for(int j=0; j<i; j++)
            {
                // if nums[i] > nums[j] then we Need to consider the scenarios 
                // when current subsequnce length is equal or less than previous
                
                if(nums[i] > nums[j])
                {
                    if(dp[i] < 1 + dp[j])
                    {
                        dp[i] = 1 + dp[j];
                        // Count will be just updated if it reaches for the first time with prev Index count
                        count[i] = count[j];
                    }
                    else if(dp[i] == 1 + dp[j])
                    {
                        // Going further we need to add the count for previous index 
                        count[i] += count[j];
                    }
                }
                
            }

            if(dp[i] > maxLength)
                maxLength = dp[i];
        }

        int subsetCount = 0;

        for(int i=0; i<dp.Length; i++)
        {
            if(dp[i] == maxLength)
            {
                subsetCount += count[i];
            }
        }

        return subsetCount;
    }
}
````

##### <span style='color:#0066cc'>2.6.2. LIS+Binary Search</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an integer array nums, return the length of the longest strictly increasing subsequence.
> 
> A subsequence is a sequence derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3, 6, 2, 7] is a subsequence of [0, 3, 1, 6, 2, 2, 7].
> 
> The task is to find the length of the longest subsequence in which every element is greater than the previous one.
> 
> Examples:
> Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
> 
> Output: 4
> 
> Explanation: The longest increasing subsequence is [2, 3, 7, 101], and its length is 4.
> 
> Input: nums = [0, 1, 0, 3, 2, 3]
> 
> Output: 4
> 
> Explanation: The longest increasing subsequence is [0, 1, 2, 3], and its length is 4
> 
> Input: nums = [7, 7, 7, 7, 7, 7, 7]
> 
> Output:
> 1
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    public int LIS(int[] nums)
    {
        // This list gets updated whenever subsequence count gets updated
        List<int> tails = new List<int>();
        tails.Add(nums[0]);

        for(int i=1; i<nums.Length; i++)
        {
            if(nums[i] > tails.Last())
            {
                tails.Add(nums[i]);
            }
            else
            {
                int idx = tails.BinarySearch(nums[i]);
                if(idx < 0)
                {
                    tails[~idx] = nums[i]; // It gives immediate next greater number
                }
            }
        }

        return tails.Count;
    }
}
````

##### <span style='color:#0066cc'>2.6.3. LIS_Print_Lexicographically</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array of n integers arr, return the Longest Increasing Subsequence (LIS) that is Index-wise Lexicographically Smallest.
> 
> The Longest Increasing Subsequence (LIS) is the longest subsequence where all elements are in strictly increasing order.
> 
> A subsequence A1 is Index-wise Lexicographically Smaller than another subsequence A2 if, at the first position where A1 and A2 differ, the element in A1 appears earlier in the array arr than corresponding element in S2.
> 
> Your task is to return the LIS that is Index-wise Lexicographically Smallest from the given array.
> 
> Examples:
> Input: arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
> 
> Output: [10, 22, 33, 50, 60, 80]
> 
> Explanation: The LIS is [10, 22, 33, 50, 60, 80] and it is the lexicographically smallest.
> 
> Input: arr = [1, 3, 2, 4, 6, 5]
> 
> Output: [1, 3, 4, 6]
> 
> Explanation: Possible LIS sequences are [1, 3, 4, 6] and [1, 2, 4, 6]. Since [1, 3, 4, 6] is Index-wise Lexicographically Smaller, it is the result.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public List<int> LongestIncreasingSubsequence(int[] arr)
    {
        int[] dp = new int[arr.Length];
        int[] backTrack = new int[arr.Length];

        /* 
        Not required as it can be done in below loop only
        Array.Fill(dp, 1);
        for(int i=0;i<arr.Length; i++)
        {
                backTrack[i] = i;
        }
       */

        int maxIndex = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            // Initializing the dp array and backtrack Array in this loop only 
            dp[i] = 1;
            backTrack[i] = i;

            for (int j = 0; j <= i; j++)
            {
                if (arr[i] > arr[j] && dp[j] + 1 > dp[i])
                {
                    dp[i] = 1 + dp[j];
                    backTrack[i] = j;
                }
            }

            // Updating the index having Max Subsequence Length
            if (dp[i] > dp[maxIndex])
            {
                maxIndex = i;
            }
        }

        /* Not required as already done in the above loop only
            int maxIndex = 0;
            for(int i=1; i<arr.Length; i++)
            {
                if(dp[i] > dp[maxIndex])
                    maxIndex = i;
            }
        */

        // Constructing the subsequence using backtracking
        List<int> subsequence = new List<int>();

        while (maxIndex != backTrack[maxIndex])
        {
            subsequence.Add(arr[maxIndex]);
            maxIndex = backTrack[maxIndex];
        }

        subsequence.Add(arr[maxIndex]);

        subsequence.Reverse();
        return subsequence;
    }
}
````

##### <span style='color:#0066cc'>2.6.4. Longest Bitionic Sequence</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array arr of n integers, the task is to find the length of the longest bitonic sequence. A sequence is considered bitonic if it first increases, then decreases. The sequence does not have to be contiguous.
> 
> Examples:
> Input: arr = [5, 1, 4, 2, 3, 6, 8, 7]
> 
> Output: 6
> 
> Explanation: The longest bitonic sequence is [1, 2, 3, 6, 8, 7] with length 6.
> 
> Input: arr = [10, 20, 30, 40, 50, 40, 30, 20]
> 
> Output: 8
> 
> Explanation: The entire array is bitonic, increasing up to 50 and then decreasing.
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public int LongestBitonicSequence(List<int> arr) {
        int maxLength = 0;

        int[] dp1 = GetLIS(arr); // LIS: Left - > Right
        int[] dp2 = GetLDS(arr); // LDS: Right -> Left

        // At the same index If we take sum of both the longest Seqence
        // one with LIS Left->right, and other with LDS Right->Left
        // It will consider current element as peak element where direction of sequence is getting reversed
        // Since in both sequence this element considered twice so, will subtract 1 from sum
        for (int i = 0; i < dp1.Length; i++)
        {
            maxLength = Math.Max(maxLength, dp1[i] + dp2[i] - 1);
        }

        return maxLength;
    }

    private int[] GetLIS(List<int> arr)
    {
        int[] dp = new int[arr.Count];

        for(int i=0; i<arr.Count; i++)
        {
            dp[i] = 1;
            for(int j=0; j<i; j++)
            {
                if(arr[i] > arr[j] && dp[i] < 1+dp[j])
                {
                    dp[i] = 1 + dp[j];
                }
            }
        }

        return dp;
    }
    
    private int[] GetLDS(List<int> arr)
    {
        int n = arr.Count;
        int[] dp = new int[n];

        for(int i=n-1; i >= 0 ; i--)
        {
            dp[i] = 1;
            for(int j=n-1; j>i; j--)
            {
                if(arr[i] > arr[j] && dp[i] < 1+dp[j])
                {
                    dp[i] = 1 + dp[j];
                }
            }
        }

        return dp;
    }
}
````

##### <span style='color:#0066cc'>2.6.5. Longest Divisible Subset</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array nums of positive integers, the task is to find the largest subset such that every pair (a, b) of elements in the subset satisfies a % b == 0 or b % a == 0.
> 
> Return the subset in any order. If there are multiple solutions, return any one of them.
> 
> Note: As there can be multiple correct answers, the compiler returns 1 if the answer is valid, else 0.
> 
> Examples:
> Input: nums = [3, 5, 10, 20]
> 
> Output: [5, 10, 20]
> 
> Explanation:
> 
> The subset [5, 10, 20] satisfies the divisibility condition: 10 % 5 == 0 and 20 % 10 == 0.
> 
> Input: nums = [16, 8, 2, 4, 32]
> 
> Output: [2, 4, 8, 16, 32]
> 
> Explanation:
> 
> The entire array forms a divisible subset since 32 % 16 == 0, 16 % 8 == 0, and so on.
> </span>

##### 💻 Solution

````csharp
// After Sorting the Array this problem has been converted into kind of problem where
// we need to find the longest chain which the divisible by previous element
public class Solution
{
    public List<int> LargestDivisibleSubset(int[] nums)
    {
        // Need to Sort Array as we need to make use of logic that
        // if element which can divide the current element should also be divisibe by
        // the elements which devides the current element which is dividing

        Array.Sort(nums);
        int[] dp = new int[nums.Length];
        int[] backtrack = new int[nums.Length];

        int maxIndex = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            dp[i] = 1;
            backtrack[i] = i;

            for (int j = 0; j < i; j++)
            {
                // Adjusted the logic here to check if % operation is giving "Zero"
                if (nums[i] % nums[j] == 0 && dp[i] < dp[j] + 1)
                {
                    dp[i] = 1 + dp[j];
                    backtrack[i] = j;
                }
            }

            if (dp[i] > dp[maxIndex])
                maxIndex = i;
        }

        List<int> res = new List<int>();

        while (backtrack[maxIndex] != maxIndex)
        {
            res.Add(nums[maxIndex]);
            maxIndex = backtrack[maxIndex];
        }

        res.Add(nums[maxIndex]);

        return res;
    }
}
````

##### <span style='color:#0066cc'>2.6.6. Longest Increasing Subsequence</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an integer array nums, return the length of the longest strictly increasing subsequence.
> 
> A subsequence is a sequence derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3, 6, 2, 7] is a subsequence of [0, 3, 1, 6, 2, 2, 7].
> 
> The task is to find the length of the longest subsequence in which every element is greater than the previous one.
> 
> Examples:
> Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
> 
> Output: 4
> 
> Explanation: The longest increasing subsequence is [2, 3, 7, 101], and its length is 4.
> 
> Input: nums = [0, 1, 0, 3, 2, 3]
> 
> Output: 4
> 
> Explanation: The longest increasing subsequence is [0, 1, 2, 3], and its length is 4
> </span>

##### 💻 Solution

````csharp
// Recursion + Memoization
// TC: O(N^2)
// SC: O(N^2) + O(N)
public class Solution
{
    public int LIS(int[] nums)
    {
        int n = nums.Length;
        int[,] dp = new int[nums.Length, nums.Length];
        return Solve(nums, 0, -1, dp);
    }

    private int Solve(int[] nums, int index, int prev_index, int[,] dp)
    {
        if (index == nums.Length - 1)
        {
            if (prev_index == -1 || nums[index] > nums[prev_index])
                return 1;
            return 0;
        }

        if (dp[index, prev_index + 1] != 0)
            return dp[index, prev_index + 1];

        // Exclude
        int res1 = Solve(nums, index + 1, prev_index, dp);

        // Include
        int res2 = 0;

        if (prev_index == -1 || nums[index] > nums[prev_index])
        {
            res2 = 1 + Solve(nums, index + 1, index, dp);
        }

        return dp[index, prev_index + 1] = Math.Max(res1, res2);
    }
}
````

##### <span style='color:#0066cc'>2.6.7. Longest String Chain</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> You are given an array of words where each word consists of lowercase English letters.
> 
> wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
> 
> For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
> 
> A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
> 
> Return the length of the longest possible word chain with words chosen from the given list of words.
> 
> 
> Examples:
> Input: words = ["a", "ab", "abc", "abcd", "abcde"]
> 
> Output: 5
> 
> Explanation: The longest chain is ["a", "ab", "abc", "abcd", "abcde"].
> 
> Each word in the chain is formed by adding exactly one character to the previous word.
> 
> Input: words = ["dog", "dogs", "dots", "dot", "d", "do"]
> 
> Output: 4
> 
> Explanation: The longest chain is ["d", "do", "dot", "dots"].
> 
> Each word is formed by inserting one character into the previous word.
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    public int LongestStringChain(string[] words)
    {
        Array.Sort(words, Compare); // Using custom comparer to sort based on string length

        int[] dp = new int[words.Length];

        int maxLength = 0;

        for(int i=0; i<words.Length; i++)
        {
            dp[i] = 1;
            for(int j=0; j<i; j++)
            {
                if(IsValiPredecessror(words[i], words[j]) && dp[i] < dp[j] + 1)
                {
                    dp[i] = 1 + dp[j];
                }
            }

            if(dp[i] > maxLength)
            {
                maxLength = dp[i];
            }
        }

        return maxLength;
    }

    // Custom comparator function 
    private static int Compare(string s, string t)
    {
        return s.Length.CompareTo(t.Length);
    }

    private bool IsValiPredecessror(string s, string t)
    {
        if(s.Length - t.Length != 1) return false;

        int i=0, j=0;

        while(i < s.Length)
        {
            if(j < t.Length && s[i] == t[j])
            {
                i++;
                j++;
            }
            else
            {
                i++;
            }
        }

        if(i == s.Length && j == t.Length)
            return true;
        return false;
    }
}
````

---

### <span style='color:#009900'>📁 2.7. MCM</span>

##### <span style='color:#0066cc'>2.7.1. Matrix Chain Multiplication</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses to minimize the number of multiplications.
> 
> Given an array nums of size n. Dimension of matrix Ai ( 0 < i < n ) is nums[i - 1] x nums[i].Find a minimum number of multiplications needed to multiply the chain.
> 
> Examples:
> Input : nums = [10, 15, 20, 25]
> 
> Output : 8000
> 
> Explanation : There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
> 
> If we multiply in order- A1*(A2*A3), then number of multiplications required are 11250.
> 
> If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
> 
> Thus minimum number of multiplications required is 8000.
> 
> Input : nums = [4, 2, 3]
> 
> Output : 24
> 
> Explanation : There is only one way to multiply the chain - A1*A2.
> 
> Thus minimum number of multiplications required is 24.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int MatrixMultiplication(int[] nums)
    {
        //your code goes here
        int n = nums.Length;
        int[,] dp = new int[n, n];

        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i,j] = -1;
            }
        }

        return MCM(nums, 1, n-1, dp);
    }

    private int MCM(int[] nums, int i, int j, int[,] dp)
    {
        if(i == j)
        {
            return 0;
        }        

        if(dp[i,j] != -1)
            return dp[i,j];

        int min = int.MaxValue;

        for(int k=i; k<j; k++)
        {
            // consider the case for partition from i to k then k+1 to j-1. Where j = nums.Length-1
            int ans = nums[i-1] * nums[k] * nums[j] + MCM(nums, i, k, dp) + MCM(nums, k+1, j, dp);
            min = Math.Min(min, ans);
        }

        return dp[i,j] = min;
    }
}
````

---

### <span style='color:#009900'>📁 2.8. Stocks</span>

##### <span style='color:#0066cc'>2.8.1. Max Profit Best Time Buy Sell Stock</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. Determine the maximum profit achievable by buying and selling the stock at most once. 
> 
> 
> 
> The stock should be purchased before selling it, and both actions cannot occur on the same day.
> 
> 
> Examples:
> Input: arr = [10, 7, 5, 8, 11, 9]
> 
> Output: 6
> 
> Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.
> 
> Input: arr = [5, 4, 3, 2, 1]
> 
> Output: 0
> 
> Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int stockBuySell(int[] arr, int n)
    {
        if(arr.Length == 1)
            return 0;
       int buy = arr[0], sell = arr[1], profit = Math.Max(0, sell-buy);

       for(int i=1; i<n; i++)
       {
            if(arr[i] < buy)
            {
                buy = arr[i];
                sell = buy;
            }
            else if(arr[i] > sell)
            {
                sell = arr[i];
            }

            profit = Math.Max(profit, sell - buy);
       }

       return profit;
    }
}
````

##### <span style='color:#0066cc'>2.8.2. Max Profit With 2 Transactions</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array, arr, of n integers, where arr[i] represents the price of the stock on an ith day, determine the maximum profit achievable by completing at most two transactions in total.
> 
> 
> 
> Holding at most one share of the stock at any time is allowed, meaning buying and selling the stock twice is permitted, but the stock must be sold before buying it again. Buying and selling the stock on the same day is allowed.
> 
> 
> Examples:
> Input: arr = [4, 2, 7, 1, 11, 5]
> 
> Output: 15
> 
> Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 7), profit = 7 - 2 = 5. Then buy on day 4 (price = 1) and sell on day 5 (price = 11), profit = 11 - 1 = 10. Total profit is 5 + 10 = 15.
> 
> Input: arr = [1, 3, 2, 8, 4, 9]
> 
> Output: 12
> 
> Explanation: Buy on day 1 (price = 1) and sell on day 4 (price = 8), profit = 8 - 1 = 7. Then buy on day 5 (price = 4) and sell on day 6 (price = 9), profit = 9 - 4 = 5. Total profit is 7 + 5 = 12.
> 
> Input: arr = [5, 7, 2, 10, 6, 9]
> 
> Output:
> 11
> </span>

##### 💻 Solution

````csharp
class Solution {
    public int StockBuySell(int[] arr, int n)
    {
        int[,] dp = new int[n+1, 5];

        for(int i=0; i<n+1; i++)
        {
            for(int j=0; j<5; j++)
            {
                dp[i,j] = -1;
            }
        }
        return Solve(arr, 0, 0, dp);
    }

    private int Solve(int[] arr, int j, int c, int[,] dp)
    {
        if(c == 4 || j == arr.Length)
        {
          return 0;
        }

        if(dp[j,c] != -1) return dp[j,c];

        if(c % 2 == 0) // Buy
        {
            return dp[j,c] = Math.Max(-arr[j] + Solve(arr, j+1, c+1, dp), Solve(arr, j+1, c, dp));
        }
        else // Sell
        {
            return dp[j,c] = Math.Max(arr[j] + Solve(arr, j, c+1, dp), Solve(arr, j+1, c, dp));
        }
        
    }
}
````

##### <span style='color:#0066cc'>2.8.3. Max Profit With KTransaction</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array, arr, of n integers, where arr[i] represents the price of the stock on an ith day, determine the maximum profit achievable by completing at most k transactions in total. Holding at most one share of the stock at any given time is allowed, meaning buying and selling the stock k times is permitted, but the stock must be sold before buying it again. Buying and selling the stock on the same day is allowed.
> 
> Examples:
> Input: arr = [3, 2, 6, 5, 0, 3], k = 2
> 
> Output: 7
> 
> Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6 - 2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3 - 0 = 3. Total profit is 4 + 3 = 7.
> 
> Input: arr = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], k = 3
> 
> Output: 15
> 
> Explanation: Buy on day 1 (price = 1) and sell on day 3 (price = 4), profit = 4 - 1 = 3. Then buy on day 4 (price = 2) and sell on day 6 (price = 7), profit = 7 - 2 = 5. Then buy on day 7 (price = 2) and sell on day 9 (price = 9), profit = 9 - 2 = 7. Total profit is 3 + 5 + 7 = 15.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int StockBuySell(int[] arr, int n, int k)
    {
       int[,] dp = new int[n+1, 2*k+1];

       for(int i=0; i<n+1; i++)
       {
            for(int j=0; j<2*k+1; j++)
            {
                dp[i,j] = -1;
            }
       }

       return Solve(arr, 0, 2*k, dp);
    }

    private int Solve(int[] arr, int i, int k, int[,] dp)
    {
        if(k == 0 || i == arr.Length)
        {
            return 0;
        }

        if(dp[i,k] != -1) return dp[i,k];

        // Buy
        if(k % 2 == 0)
        {
            return dp[i,k] = Math.Max(-arr[i] + Solve(arr, i+1, k-1, dp), Solve(arr, i+1, k, dp)); 
        }
        else
        {
            return dp[i,k] = Math.Max(arr[i] + Solve(arr, i+1, k-1, dp), Solve(arr, i+1, k, dp));
        }

    }
}
````

##### <span style='color:#0066cc'>2.8.4. Max Profit With Transaction Fee</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array arr where arr[i] represents the price of a given stock on the ith day. Additionally, you are given an integer fee representing a transaction fee for each trade. The task is to determine the maximum profit you can achieve such that you need to pay a transaction fee for each buy and sell transaction. The Transaction Fee is applied when you sell a stock.
> 
> You may complete as many transactions. You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before buying again).
> 
> 
> Examples:
> Input: arr = [1, 3, 4, 0, 2], fee = 1
> 
> Output: 3
> 
> Explanation: Buy at day 1, sell at day 3, then, buy at day 4, sell at day 5.
> 
> Profit calculation: ((4 - 1) - 1) + ((2 - 0) - 1) = 2 + 1 = 3.
> 
> Input: arr = [1, 3, 2, 8, 4, 9], fee = 2
> 
> Output: 8
> 
> Explanation: Buy at day 1 (price = 1), sell at day 4 (price = 8), then Buy at day 5 (price = 4), sell at day 6 (price = 9),
> 
> Profit calculation: ((9 - 4) - 2) + ((8 - 1) - 2)= 8.
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    public int stockBuySell(int[] arr, int n, int fee)
    {
        // Your code goes here
        int[,] dp = new int[n, 2];

        for(int i=0; i<n; i++)
        {
            dp[i,0] = -1;
            dp[i,1] = -1;
        }
        return Solve(arr, fee, 0, 0, dp);
    }

    private int Solve(int[] arr, int fee, int buy, int i, int[,] dp)
    {
        if(i == arr.Length)
        {
            return 0;
        }

        if(dp[i,buy] != -1) return dp[i,buy];

        if(buy  == 0)
        {
            return dp[i, buy] = Math.Max(-arr[i] + Solve(arr, fee, 1, i+1, dp), Solve(arr, fee, 0, i+1, dp));
        }
        else
        {
            return dp[i,buy] = Math.Max(arr[i]-fee + Solve(arr, fee, 0, i, dp), Solve(arr, fee, 1, i+1, dp));
        }
    }
}
````

##### <span style='color:#0066cc'>2.8.5. Total Profit Buy Sell Stock</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. Determine the maximum profit achievable by buying and selling the stock any number of times.
> 
> 
> 
> Holding at most one share of the stock at any given time is allowed, meaning buying and selling the stock can be done any number of times, but the stock must be sold before buying it again. Buying and selling the stock on the same day is permitted.
> 
> 
> Examples:
> Input: arr = [9, 2, 6, 4, 7, 3]
> 
> Output: 7
> 
> Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6 - 2 = 4. Then buy on day 4 (price = 4) and sell on day 5 (price = 7), profit = 7 - 4 = 3. Total profit is 4 + 3 = 7.
> 
> Input: arr = [2, 3, 4, 5, 6]
> 
> Output: 4
> 
> Explanation: Buy on day 1 (price = 2) and sell on day 5 (price = 6), profit = 6 - 2 = 4. Total profit is 4.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int StockBuySell(int[] arr, int n)
    {
        if(arr.Length == 1)
            return 0;

        int profit = 0;
        int buy = arr[0], sell = arr[1];

        for(int i=1; i<n; i++)
        {
            if(arr[i] > buy)
            {
                profit += arr[i] - buy;
                buy = arr[i];
            }
            else
            {
                buy = arr[i];
            }
        }

        return profit;
    }
}
````

---

### <span style='color:#009900'>📁 2.9. Subset Subsequences</span>

##### <span style='color:#0066cc'>2.9.1. Subset Partition Minimun Sum</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array arr of n integers, partition the array into two subsets such that 
> the absolute difference between their sums is minimized.
> 
> Examples:
> Input: arr = [1, 7, 14, 5]
> Output: 1
> 
> Explanation: The array can be partitioned as [1, 7, 5] and [14], with an absolute difference of 1.
> 
> Input: arr = [3, 1, 6, 2, 2]
> Output: 0
> 
> Explanation: The array can be partitioned as [3, 2, 2] and [6, 1], with an absolute difference of 0.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int minDifference(int[] arr, int n)
    {
        int sum = 0;

        for (int i = 0; i < n; i++)
        {
            sum += arr[i];
        }

        int[,] dp = new int[n, sum + 1];
        return Solve2(arr, n, sum, 0, 0, dp);

    }

    private int Solve2(int[] arr, int n, int totalSum, int s, int index, int[,] dp)
    {
        if (n == index)
        {
            return Math.Abs(totalSum - s - s);
        }

        if (dp[index, s] != 0)
            return dp[index, s];

        // Include
        int sum1 = Solve2(arr, n, totalSum, s + arr[index], index + 1, dp);
        // Exclude
        int sum2 = Solve2(arr, n, totalSum, s, index + 1, dp);

        dp[index, s] = Math.Min(sum1, sum2);

        return dp[index, s];
    }

}
````

##### <span style='color:#0066cc'>2.9.2. Subset Sum Equal Partition</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array arr of n integers, return true if the array can be partitioned into 
> two subsets such that the sum of elements in both subsets is equal else return false.
> 
> Examples:
> Input: arr = [1, 10, 21, 10]
> Output: True
> 
> Explanation: The array can be partitioned as [1, 10, 10] and [21].
> 
> Input: arr = [1, 2, 3, 5]
> Output: False
> 
> Explanation: The array cannot be partitioned into equal sum subsets.
> </span>

##### 💻 Solution

````csharp
class Solution {

    public bool EqualPartition(int n, int[] arr) {
        int sum = 0;

        for(int i=0; i<arr.Length; i++)
        {
            sum += arr[i];
        }

        if(sum % 2 != 0)
            return false;
        
        int target = sum / 2;
        int[,] dp = new int[n, target+1];
        return Solve(arr, target, 0, dp);
    }

    private bool Solve(int[] arr, int target, int index, int[,] dp)
    {
        if( index >= arr.Length || target < 0)
        {
            return false;
        }

        if(target == 0)
        {
            return true;
        }

        if(dp[index, target] != 0)
            return dp[index, target] == 1;

        dp[index, target] = Solve(arr, target - arr[index], index+1, dp);
        if(dp[index, target] == 1)
        {
            return true;
        }
        else
        {
            dp[index, target] = -1;
        }
        
        return Solve(arr, target, index+1, dp);
    }
}
````

##### <span style='color:#0066cc'>2.9.3. Sub Set Sum Equal To Target</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array arr of n integers and an integer target, determine if there is a subset 
> of the given array with a sum equal to the given target.
> 
> Examples:
> Input: arr = [1, 2, 7, 3], target = 6
> Output: True
> 
> Explanation: There is a subset (1, 2, 3) with sum 6.
> 
> Input: arr = [2, 3, 5], target = 6
> Output: False
> 
> Explanation: There is no subset with sum 6.
> </span>

##### 💻 Solution

````csharp
// Here even without using the memoization it was able to pass all the Test cases
class Solution
{
    public bool IsSubsetSum(int[] arr, int target)
    {
        return Solve(arr, target, 0);
    }

    private bool Solve(int[] arr, int target, int index)
    {
        if (target == 0) return true;

        if (index >= arr.Length || target < 0)
            return false;

        if (target >= arr[index])
        {
            if (Solve(arr, target - arr[index], index + 1)) return true;
        }

        return Solve(arr, target, index + 1);
    }
}
````

##### <span style='color:#0066cc'>2.9.4. Subset Sum To Target Count</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array arr of n integers and an integer K, count the number of subsets of the given array that have a sum equal to K. Return the result modulo (109 + 7).
> 
> 
> Examples:
> Input: arr = [2, 3, 5, 16, 8, 10], K = 10
> 
> Output: 3
> 
> Explanation: The subsets are [2, 8], [10], and [2, 3, 5].
> 
> Input: arr = [1, 2, 3, 4, 5], K = 5
> 
> Output: 3
> 
> Explanation: The subsets are [5], [2, 3], and [1, 4].
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int perfectSum(int[] arr, int K)
    {
        int[,] dp = new int[arr.Length, K+1];
        return Solve(arr, K, arr.Length-1, dp);
    }

    private int Solve(int[] arr, int K, int index, int[,] dp)
    {
        if(K == 0)
        {
            return 1;
        }

        if(index < 0)
        {
            return 0;
        }

        if(dp[index, K] != 0)
            return dp[index, K];

        // Exclude
        int res1 = Solve(arr, K, index-1, dp);

        // Include
        int res2 = 0;

        if(arr[index] <= K)
        {
            res2 = Solve(arr, K - arr[index], index-1, dp);
        }

        dp[index, K] = (res1 % 1000000007 + res2 % 1000000007) % 1000000007;

        return dp[index, K];
    }
}
````

##### <span style='color:#0066cc'>2.9.5. Target Sum</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an array nums of n integers and an integer target, build an expression using the integers from nums where each integer can be prefixed with either a '+' or '-' sign.
> 
> The goal is to achieve the target sum by evaluating all possible combinations of these signs.
> 
> Determine the number of ways to achieve the target sum and return your answer with modulo 10^9+7.
> 
> Examples:
> Input: nums = [1, 2, 7, 1, 5], target = 4
> 
> Output: 2
> 
> Explanation: There are 2 ways to assign symbols to make the sum of nums be target 4.
> 
> +1 + 2 + 7 - 1 - 5 = 4
> 
> -1 + 2 + 7 + 1 - 5 = 4
> 
> Input: nums = [1], target = 1
> 
> Output: 1
> 
> Explanation: There is only one way to assign symbols to make the sum of nums be target 1.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int targetSum(int n, int target, int[] nums)
    {
        Dictionary<(int,int), int> dp = new Dictionary<(int,int), int>();
        return Solve(nums, target, n, 0, dp);
    }

    private int Solve(int[] nums, int target, int n, int index, Dictionary<(int,int), int> dp)
    {
        if(index == n)
        {
            if(target == 0)
            {
                return 1;
            }
            return 0;
        }

        if(dp.ContainsKey((index, target)))
            return dp[(index, target)];

        int res = Solve(nums, target - nums[index], n , index+1, dp) % 1000000007+ Solve(nums, target+nums[index], n, index+1, dp) % 1000000007;

        dp.Add((index, target), res % 1000000007);
        return dp[(index, target)];
    }
}
````

---

### <span style='color:#009900'>📁 2.10. Unbounded Knapsack</span>

##### <span style='color:#0066cc'>2.10.1. Coin Change</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an integer array of coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that are needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. There are infinite numbers of coins of each type
> 
> Examples:
> Input: coins = [1, 2, 5], amount = 11
> 
> Output: 3
> 
> Explanation: 11 = 5 + 5 + 1. We need 3 coins to make up the amount 11.
> 
> Input: coins = [2, 5], amount = 3
> 
> Output: -1
> 
> Explanation: It's not possible to make amount 3 with coins 2 and 5. Since we can't combine the coin 2 and 5 to make the amount 3, the output is -1.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int MinimumCoins(int[] coins, int amount)
    {
        int[,] dp = new int[coins.Length, amount + 1];
        int res = Solve(coins, amount, coins.Length-1, dp);
        if(res < 0 || res == int.MaxValue)
        {
            return -1;
        }

        return res;
    }

    public int Solve(int[] coins, int amount, int index, int[,] dp)
    {
        if(index == 0)
        {
            if(amount % coins[index] == 0)
                return amount/coins[index];
            else
                return int.MaxValue;
        }

        if(amount == 0)
            return 0;
        
        if(dp[index, amount] != 0)
            return dp[index, amount];

        // exclude corrent coin
        int res1 = Solve(coins, amount, index-1, dp);

        int res2 = int.MaxValue;
        
        // include current Coin
        // Including the coin one by one and not by formula 
        // amount/coins[index] : it becomes Greedy and doesn't give the optimal solution
        // So, better try all the possible combinations to get optimized output
        if(coins[index] <= amount)
        {
            res2 = Solve(coins, amount - coins[index], index, dp);
            if(res2 != int.MaxValue)
            {
                res2 += 1;
            }
        }

        dp[index, amount] = Math.Min(res1, res2);
        return dp[index, amount];
    }
}
````

##### <span style='color:#0066cc'>2.10.2. Coin Change 2</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Give an array coins of n integers representing coin denominations. Your task is to find the number of distinct combinations that sum up to a specified amount of money. If it's impossible to achieve the exact amount with any combination of coins, return 0.
> 
> Single coin can be used any number of times.
> 
> Return your answer with modulo 109+7.
> 
> Examples:
> Input: coins = [2, 4,10], amount = 10
> Output: 4
> 
> Explanation: The four combinations are:
> 10 = 10
> 10 = 4 + 4 + 2
> 10 = 4 + 2 + 2 + 2
> 10 = 2 + 2 + 2 + 2 + 2
> 
> Input: coins = [5], amount = 5
> Output: 1
> Explanation: There is one combination: 5 = 5.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    private static int MOD = (int)1e9 + 7;

    public int count(int[] coins, int N, int amount)
    {

      int[,] dp = new int[N, amount + 1];

      for(int i=0; i<N; i++)
      {
        for(int j=0; j <= amount; j++)
        {
            dp[i,j] = -1;
        }
      }

      return Solve(coins, amount, N-1, dp);
    }

    private int Solve(int[] coins, int amount, int index, int[,] dp)
    {
        if(amount == 0)
        {
            return 1;
        }

        if(index == -1)
        {
            return 0;
        }

        if(dp[index, amount] != -1)
        {
            return dp[index, amount];
        }

        // Exclude
        int res1 = Solve(coins, amount, index-1, dp);

        // Include
        int res2 = 0;
        if(coins[index] <= amount)
        {
            res2 = Solve(coins, amount - coins[index], index, dp);
        } 

        dp[index, amount] = (res1 % MOD + res2 % MOD) % MOD;
        return dp[index, amount];
    }
}
````

##### <span style='color:#0066cc'>2.10.3. Rod Cutting Problem</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a rod of length N inches and an array price[] where price[i] denotes the value of a piece of rod of length i inches (1-based indexing). Determine the maximum value obtainable by cutting up the rod and selling the pieces. Make any number of cuts, or none at all, and sell the resulting pieces.
> 
> Examples:
> Input: price = [1, 6, 8, 9, 10, 19, 7, 20], N = 8
> 
> Output: 25
> 
> Explanation: Cut the rod into lengths of 2 and 6 for a total price of 6 + 19= 25.
> 
> Input: price = [1, 5, 8, 9], N = 4
> 
> Output: 10
> 
> Explanation: Cut the rod into lengths of 2 and 2 for a total price of 5 + 5 = 10.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public int RodCutting(int[] price, int n)
    {
        // Initialize with "price.Length+1" instead of just "price.Length"
        // As we need to deal with "1" based index for price Array
        int[,] dp = new int[price.Length+1, n+1];

        for(int i=0; i <= price.Length; i++)
        {
            for(int j=0; j<=n; j++)
            {
                dp[i,j] = -1;
            }
        }

        return Solve(price, n, price.Length, dp);
    }

    private int Solve(int[] price, int n, int index, int[,] dp)
    {
        if(n == 0 || index == 0)
            return 0;

        if(dp[index, n] != -1)
            return dp[index, n];

        // Exclude
        int res1 = Solve(price, n, index-1, dp);

        // include

        // Note: Considering the 1 based index for Price Array but in actual it always stars from zero
        // So, To get actual price just use "price[index-1]" instead of price[index]
        // Index will refer "1" based as need to compute with "n" but price will refer "0" based as C# array are Zero based
        int res2 = 0;
        if(index <= n)
        {
            res2 = price[index-1] + Solve(price, n-index, index, dp);
        }

        dp[index, n] = Math.Max(res1, res2);
        return dp[index, n];
    }
}
````

##### <span style='color:#0066cc'>2.10.4. Unbounded Knapsack</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given two integer arrays, val and wt, each of size N, representing the values and weights of N items respectively, and an integer W, representing the maximum capacity of a knapsack, determine the maximum value achievable by selecting a subset of the items such that the total weight of the selected items does not exceed the knapsack capacity W. The goal is to maximize the sum of the values of the selected items while keeping the total weight within the knapsack's capacity.
> 
> An infinite supply of each item can be assumed.
> 
> Examples:
> Input: val = [5, 11, 13], wt = [2, 4, 6], W = 10
> 
> Output: 27
> 
> Explanation: Select 2 items with weights 4 and 1 item with weight 2 for a total value of 11+11+5 = 27.
> 
> Input: val = [10, 40, 50, 70], wt = [1, 3, 4, 5], W = 8
> 
> Output: 110
> 
> Explanation: Select items with weights 3 and 5 for a total value of 40 + 70 = 110.
> </span>

##### 💻 Solution

````csharp
class Solution {
    public int UnboundedKnapsack(int[] wt, int[] val, int n, int W) {
        int[,] dp = new int[n, W+1];

        for(int i=0; i<n; i++)
        {
            for(int j=0; j<=W; j++)
            {
                dp[i,j] = -1;
            }
        }
            
        return Solve(wt, val, n-1, W, dp);
    }

    private int Solve(int[] wt, int[] val, int index, int W, int[,] dp)
    {
        if(W == 0 || index == -1)
            return 0;

        if(dp[index, W] != -1)
        {
            return dp[index, W];
        }

        // Exclude
        int res1 = Solve(wt, val, index-1, W, dp);

        // Include
        int res2 = 0;
        if(wt[index] <= W)
        {
            res2 = val[index] + Solve(wt, val, index, W - wt[index], dp);
        }
        
        dp[index, W] = Math.Max(res1, res2);
        return dp[index, W];
    }
}
````

---

---

## <span style='color:#009900'>📁 3. Graph</span>

#### <span style='color:#0066cc'>3.1. BFS</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> BFS Implementation for graph with 'n' nodes
> </span>

##### 💻 Solution

````csharp
class Graph
{
    void BFS(GraphNode root, int n)
    {
        int[] visited = new int[n];
        Queue<int> q = new Queue<int>();

        q.Enqueue(root.Value);
        visited[root.Value] = 1;

        while (q.Count != 0)
        {
            var currentNode = q.Dequeue();
            Console.WriteLine(currentNode.Value);

            foreach (var neighbor in currentNode.Neighbors)
            {
                if (visited[neighbor.Value] == 0)
                {
                    q.Enqueue(neighbor.Value);
                    visited[neighbor.Value] = 1;
                }  
            }
        }
    }
}
````

#### <span style='color:#0066cc'>3.2. Clone Graph</span>

##### 💻 Solution

````csharp
public class Solution {
    public Node CloneGraph(Node node) {
        if(node == null)
            return node;
        Dictionary<int, Node> map = new Dictionary<int, Node>();
        CloneNodes(node, map);
        return map[1];
        
    }
    
    private void CloneNodes(Node node, Dictionary<int, Node> map)
    {
        Node newNode = new Node(node.val);
        newNode.neighbors = new List<Node>();
        
        map.Add(newNode.val, newNode);
        foreach(Node n in node.neighbors)
        {
            if(!map.ContainsKey(n.val))
                CloneNodes(n,map);
            newNode.neighbors.Add(map[n.val]);
            
        }
    }
}
````

#### <span style='color:#0066cc'>3.3. DFS</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Using DFS to traverse a graph using recursion(in-built call stack)
> </span>

##### 💻 Solution

````csharp
public class Graph
{
    HashSet<int> visited = new HashSet<int>();
    public void DFS(GraphNode node, HashSet<int> visited)
    {
        if (node == null || visited.Contains(node.Value))
            return;

        Console.WriteLine(node.Value);
        visited.Add(node.Value);

        foreach (var neighbor in node.Neighbors)
        {
            if (!visited.Contains(neighbor.Value))
            {
                DFS(neighbor, visited);
            }
        }
    }
}

// Using DFS to traverse a graph using an explicit stack
public class GraphIterative
{
    public void DFS(GraphNode root, int n)
    {
        int[] visited = new int[n];
        Stack<GraphNode> stack = new Stack<GraphNode>();

        stack.Push(root);

        while (stack.Count != 0)
        {
            var currentNode = stack.Pop();

            if (visited[currentNode.Value] == 1)
                continue;

            Console.WriteLine(currentNode.Value);
            visited[currentNode.Value] = 1;

            foreach (var neighbor in currentNode.Neighbors)
            {
                if (visited[neighbor.Value] == 0)
                {
                    stack.Push(neighbor);
                }
            }
        }
    }
}
````

#### <span style='color:#0066cc'>3.4. Graph Node</span>

##### 💻 Solution

````csharp
public class GraphNode
{
    public int Value { get; private set; }
    public List<GraphNode> Neighbors;

    public GraphNode(int value)
    {
        Value = value;
        Neighbors = new List<GraphNode>();
    }
}
````

#### <span style='color:#0066cc'>3.5. Num Islands</span>

##### 💻 Solution

````csharp
public class Solution {
	
    public int NumIslands(char[][] grid) {
		int islandCount =0;
		bool[,] visitorMatirx = new bool[grid.Length, grid[0].Length];
		
		for(int row=0; row < grid.Length; row++)
		{
			for(int col=0; col < grid[0].Length; col++)
			{
				visitorMatirx[row,col] = false;
			}
		}
		
        for(int row=0; row < grid.Length; row++)
		{
			for(int col=0; col < grid[0].Length; col++)
			{
				if(grid[row][col] == '1' && visitorMatirx[row,col] == false)
				{
					DFS(grid,row,col,visitorMatirx);
					islandCount++;
				}					
			}
		}
		
		return islandCount;
    }
	
	private void DFS(char[][] grid, int i, int j, bool[,] visitorMatirx)
	{
        
		if(i < grid.Length && j < grid[0].Length && i >= 0 && j >= 0 && grid[i][j] != '0' && !visitorMatirx[i,j])	
		{
			visitorMatirx[i,j] = true;
			DFS(grid, i+1,j, visitorMatirx);
            DFS(grid, i-1,j, visitorMatirx);
			DFS(grid, i,j+1, visitorMatirx);
			DFS(grid, i,j-1, visitorMatirx);
		}
	}
}
````

#### <span style='color:#0066cc'>3.6. Rotting Oranges</span>

##### 💻 Solution

````csharp
public class Solution {
    public int OrangesRotting(int[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        bool[,] visited = new bool[rows, cols];
        Queue<(int, int)> queue = new Queue<(int, int)>();
        int freshCount = 0;
        int minutes = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) {
                    queue.Enqueue((r, c));
                    visited[r, c] = true;
                } else if (grid[r][c] == 1) {
                    freshCount++;
                }
            }
        }

        int[][] directions = new int[][] {
            new int[] {1, 0},
            new int[] {-1, 0},
            new int[] {0, 1},
            new int[] {0, -1}
        };

        while (queue.Count > 0 && freshCount > 0) {
            int size = queue.Count;
            for (int i = 0; i < size; i++) {
                var (r, c) = queue.Dequeue();
                foreach (var dir in directions) {
                    int newRow = r + dir[0];
                    int newCol = c + dir[1];
                    if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols &&
                        grid[newRow][newCol] == 1 && !visited[newRow, newCol]) {
                        visited[newRow, newCol] = true;
                        grid[newRow][newCol] = 2;
                        freshCount--;
                        queue.Enqueue((newRow, newCol));
                    }
                }
            }
            minutes++;
        }

        return freshCount == 0 ? minutes : -1;
    }
}
````

#### <span style='color:#0066cc'>3.7. SCC_Kosaraju_Algorithm</span>

##### 💻 Solution

````csharp
public class SCC_Kosaraju_Algorithm
{
    private List<List<int>> FindSCCs(int vertices, List<List<int>> adj)
    {
        // Step 1: Perform DFS and store the finish order
        Stack<int> finishStack = new Stack<int>();
        bool[] visited = new bool[vertices];

        for (int i = 0; i < vertices; i++)
        {
            if (!visited[i])
            {
                DFS(i, adj, visited, finishStack);
            }
        }

        // Step 2: Transpose the graph
        List<List<int>> transposedAdj = TransposeGraph(vertices, adj);

        // Step 3: Perform DFS on transposed graph in finish order
        visited = new bool[vertices];
        List<List<int>> sccs = new List<List<int>>();
        while (finishStack.Count > 0)
        {
            int node = finishStack.Pop();
            if (!visited[node])
            {
                List<int> currentSCC = new List<int>();
                DFS_Transpose(node, transposedAdj, visited, currentSCC);
                sccs.Add(currentSCC);
            }
        }
        return sccs;
    }

    private void DFS(int node, List<List<int>> adj, bool[] visited, Stack<int> finishStack)
    {
        visited[node] = true;
        foreach (var neighbor in adj[node])
        {
            if (!visited[neighbor])
            {
                DFS(neighbor, adj, visited, finishStack);
            }
        }
        finishStack.Push(node);
    }

    private List<List<int>> TransposeGraph(int vertices, List<List<int>> adj)
    {
        List<List<int>> transposedAdj = new List<List<int>>();
        for (int i = 0; i < vertices; i++)
        {
            transposedAdj.Add(new List<int>());
        }

        for (int i = 0; i < vertices; i++)
        {
            foreach (var neighbor in adj[i])
            {
                transposedAdj[neighbor].Add(i);
            }
        }
        return transposedAdj;
    }

    private void DFS_Transpose(int node, List<List<int>> transposedAdj, bool[] visited, List<int> currentSCC)
    {
        visited[node] = true;
        currentSCC.Add(node);
        foreach (var neighbor in transposedAdj[node])
        {
            if (!visited[neighbor])
            {
                DFS_Transpose(neighbor, transposedAdj, visited, currentSCC);
            }
        }
    }
}
````

---

## <span style='color:#009900'>📁 4. String Problems</span>

#### <span style='color:#0066cc'>4.1. Count And Say</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
> 
> countAndSay(1) = "1"
> countAndSay(n) is the run-length encoding of countAndSay(n - 1).
> Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
> 
> Given a positive integer n, return the nth element of the count-and-say sequence.
> 
>  
> 
> Example 1:
> 
> Input: n = 4
> 
> Output: "1211"
> 
> Explanation:
> 
> countAndSay(1) = "1"
> countAndSay(2) = RLE of "1" = "11"
> countAndSay(3) = RLE of "11" = "21"
> countAndSay(4) = RLE of "21" = "1211"
> Example 2:
> 
> Input: n = 1
> 
> Output: "1"
> 
> Explanation:
> 
> This is the base case.
> 
>  
> 
> Constraints:
> 
> 1 <= n <= 30
> </span>

##### 💻 Solution

````csharp
// LeetCode: 38. Count and Say

class Solution {
    public string CountAndSay(int n) {

        string ans = "1";
        for(int i=2; i<=n; i++)
        {
            ans = Solve(ans);
        }

        return ans;
    }

    private string Solve(string s)
    {
        int count = 0;
        char current = s[0];
        int i=0;

        StringBuilder sb = new StringBuilder();

        while(i < s.Length)
        {
            if(s[i] == current)
            {
                count++;
            }
            else
            {
                sb.Append($"{count}{s[i-1]}");
                current = s[i];
                count = 1;
            }
            i++;
        }

        sb.Append($"{count}{s[i-1]}");

        return sb.ToString();
    }
}
````

#### <span style='color:#0066cc'>4.2. Pattern Match Index</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a string text and a string pattern, implement the Rabin-Karp algorithm to find the starting index of all occurrences of pattern in text. If pattern is not found, return an empty list.
> 
> Examples:
> Input: text = "ababcabcababc", pattern = "abc"
> 
> 
> Output: [2, 5, 10]
> 
> Expalanation : The pattern "abc" is found at indices 2, 5, and 10 in the text.
> 
> Input: text = "hello", pattern = "ll"
> 
> Output: [2]
> 
> Explanation: The pattern "ll" is found at index 2 in the text.
> </span>

##### 💻 Solution

````csharp
class Solution
{
    public List<int> search(string pat, string txt)
    {
        List<int> res = new List<int>();

        if(pat.Length > txt.Length) return res;

        for(int i=0; i<txt.Length; i++)
        {
            if(txt[i] == pat[0])
            {
                int k =0;
                while(k < pat.Length && i+k < txt.Length && txt[i+k] == pat[k])
                {
                    k++;
                }
                if(k == pat.Length) res.Add(i);
            }
        }

        return res;
    }
}
````

#### <span style='color:#0066cc'>4.3. Reverse Every Word In String</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.
> 
> Return a string with the words in reverse order, concatenated by a single space.
> 
> Examples:
> Input: s = "welcome to the jungle"
> 
> Output: "jungle the to welcome"
> 
> Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output string should have exactly one space between each word.
> 
> Input: s = " amazing coding skills "
> 
> Output: "skills coding amazing"
> 
> Explanation: The input string has leading and trailing spaces, as well as multiple spaces between the words "amazing", "coding", and "skills". After trimming the leading and trailing spaces and reducing the multiple spaces between words to a single space, the words are "amazing", "coding", and "skills". Reversing the order of these words gives "skills", "coding", and "amazing". The output string should not have any leading or trailing spaces and should have exactly one space between each word.
> </span>

##### 💻 Solution

````csharp
using System.Text;

public class Solution
{
    public string ReverseWords(string s)
    {
        Stack<string> stk = new Stack<string>();
        StringBuilder sb = new StringBuilder();

        bool shouldPush = false;

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] != ' ')
            {
                if (shouldPush)
                {
                    stk.Push(sb.ToString());
                    sb = new StringBuilder();
                    shouldPush = false;
                }
                sb.Append(s[i]);

            }
            else if (s[i] == ' ')
            {
                shouldPush = true;
            }
        }

        stk.Push(sb.ToString());
        sb = new StringBuilder();

        while (stk.Count > 0)
        {
            sb.Append(stk.Pop());
            sb.Append(" ");
        }

        return sb.ToString();
    }
}

// In-Place reversal without using much extra Space

public class Solution {
    public string ReverseWords(string s) {
        Stack<char> stk = new Stack<char>();
        StringBuilder sb = new StringBuilder();

        int n = s.Length-1;
        while(n >= 0)
        {
            if(s[n] != ' ')
            {
                stk.Push(s[n]);
            }
            else if(s[n] == ' ' && stk.Count > 0)
            {
                while(stk.Count > 0)
                {
                    sb.Append(stk.Pop());
                }
                sb.Append(" ");
            }
            n--;
        }

        while(stk.Count > 0)
        {
            sb.Append(stk.Pop());
        }

        return sb.ToString();
    }
}
````

#### <span style='color:#0066cc'>4.4. Shortest Palindrome</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> You are given a string s. You can convert s to a palindrome by adding characters in front of it.
> 
> Return the shortest palindrome you can find by performing this transformation.
> 
> Example 1:
> 
> Input: s = "aacecaaa"
> Output: "aaacecaaa"
> Example 2:
> 
> Input: s = "abcd"
> Output: "dcbabcd"
>  
> 
> Constraints:
> 
> 0 <= s.length <= 5 * 104
> s consists of lowercase English letters only.
> </span>

##### 💻 Solution

````csharp
// TODO: Need to write the Code
````

---

## <span style='color:#009900'>📁 5. Tree</span>

#### <span style='color:#0066cc'>5.1. Count Nodes</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Return the number of nodes in a binary tree given its root.
> Every level in a complete binary tree possibly with the exception of the final one is fully filled, and every node in the final level is as far to the left as it can be. At the last level h, it can have 1 to 2h nodes inclusive.
> </span>

##### 💻 Solution

````csharp
/*
 // Definition for a binary tree node.
 public class TreeNode {
     public int val;
     public TreeNode left;
     public TreeNode right;

     public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }
*/

public class Solution {
    public int CountNodes(TreeNode root) {

        if(root == null) return 0;

        return 1 + CountNodes(root.left) + CountNodes(root.right);
    }
}
````

#### <span style='color:#0066cc'>5.2. Diameter Of Tree</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root of a binary tree, return the length of the diameter of the tree.
> The diameter of a binary tree is the length of the longest path between any two nodes in the tree. It may or may not pass through the root.
> </span>

##### 💻 Solution

````csharp
public class Solution {
    int diameter = 0;

    public int DiameterOfBinaryTree(TreeNode root) {
        //your code goes here
        Solve(root);
        return diameter;
    }

    private int Solve(TreeNode root)
    {
        if(root == null) return 0;

        int lh = Solve(root.left);

        int rh = Solve(root.right);

        diameter = Math.Max(diameter, lh+rh);    
        return Math.Max(lh, rh) + 1;
    }
}
````

#### <span style='color:#0066cc'>5.3. Height Balanced Tree</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a binary tree root, find if it is height-balanced or not.
> A tree is height-balanced if the difference between the heights of left and right subtrees is not more than one for all nodes of the tree.
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    public bool IsBalanced(TreeNode root)
    {
        return Height(root) != -1;
    }

    // Returns height if balanced, -1 if not
    private int Height(TreeNode node)
    {
        if(node == null) return 0;

        int leftHeight = Height(node.left);
        if(leftHeight == -1) return -1;

        int rightHeight = Height(node.right);
        if(rightHeight == -1) return -1;

        if(Math.Abs(leftHeight - rightHeight) > 1) return -1;

        return Math.Max(leftHeight, rightHeight) + 1;
    }
}
````

#### <span style='color:#0066cc'>5.4. Identical Tree</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the roots of two binary trees p and q, write a function to check if they are the same or not.
> Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public bool IsSameTree(TreeNode p, TreeNode q) {
        //your code goes here
        if(p == null && q == null) return true;
        if(p == null || q == null) return false;
        if(p.val != q.val) return false;

        return p.val == q.val && IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);
    }
}
````

#### <span style='color:#0066cc'>5.5. Longest Common Ancestor</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a root of binary tree, find the lowest common ancestor (LCA) of two given nodes (p, q) in the tree.
> The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // your code goes here
        if(root == null) return root;

        if(root.val == p.val || root.val == q.val) return root;

        TreeNode left = LowestCommonAncestor(root.left, p, q);
        TreeNode right = LowestCommonAncestor(root.right, p, q);

        if(left == null) return right; // both nodes can be in right side and this node is the parent
        if(right == null) return left; // both nodes can be in left side and this node is the parent
        
        return root; // This root is the parent as both side is not null
    }
}
````

#### <span style='color:#0066cc'>5.6. Max Depth</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given root of the binary tree, return its maximum depth.
> A binary tree's maximum depth is number of nodes along the longest path from root node down to the farthest node.
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public int maxDepth(TreeNode root) {
        //your code goes here

        if(root == null) return 0;

        int lh = 1 + maxDepth(root.left);
        int rh = 1 + maxDepth(root.right);

        return Math.Max(lh, rh);
    }
}
````

#### <span style='color:#0066cc'>5.7. Max Path Sum</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> In a binary tree, a path is a list of nodes where there is an edge between every pair of neighbouring nodes. A node may only make a single appearance in the sequence.
> 
> The total of each node's values along a path is its path sum. Return the largest path sum of all non-empty paths given the root of a binary tree.
> 
> Note: The path does not have to go via the root.
> </span>

##### 💻 Solution

````csharp
public class Solution {

    int maxPathVal = int.MinValue;
    public int MaxPathSum(TreeNode root) {
        //your code goes here

        Solve(root);
        return maxPathVal;
    }

    private int Solve(TreeNode root)
    {
        if(root == null) return 0;

        // If Path Length is -ve then just ignore as it won't contribute in maxPath Length
        // and should be discarded
        int leftSum = Math.Max(0, Solve(root.left));
        int rightSum = Math.Max(0, Solve(root.right));

        // Total path length needs to be calculated as
        // path length => leftPath + RightPath + currentNode
        int pathSum = root.val + leftSum + rightSum;

        // Updating maxPathLength
        maxPathVal = Math.Max(maxPathVal, pathSum);

        // Returnig single path as at a time either left or right needs to be picked
        // To contribute in current Node path. whichever is maximum
        return Math.Max(leftSum, rightSum) + root.val;
    }
}
````

#### <span style='color:#0066cc'>5.8. Max Width Binary Tree</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root of a binary tree, return the maximum width of the given tree.
> 
> The maximum width of a tree is the maximum width among all levels. The width of a level is determined by measuring the distance between its end nodes, which are the leftmost and rightmost non-null nodes. The length calculation additionally takes into account the null nodes that would be present between the end nodes if a full binary tree were to stretch down to that level.
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int data;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int val) { data = val; left = null, right = null }
 * }
 **/

public class Solution
{
    public int widthOfBinaryTree(TreeNode root)
    {
        // Approach: we will be using the Level Order Traversal
        // Then apply the Indexing formula to identify the child index position in Level order as if it was a complete binary tree
        // for 1 based index: leftChild pos = 2*ParentIndex, rightChild = 2*ParentIndex+1

        int res = 0;

        if(root == null) return res;

        Queue<Tuple<TreeNode,int>> q = new Queue<Tuple<TreeNode, int>>();
        q.Enqueue(Tuple.Create(root, 0));

        while(q.Count > 0)
        {
            int size = q.Count;
            int first = 0;
            int last = 0;

            for(int i=0; i<size; i++)
            {
                var curr = q.Dequeue();
                int idx = curr.Item2;
                var node = curr.Item1;

                if(i == 0) first = idx;
                if(i == size-1) last = idx;

                if(node.left != null)
                {
                    q.Enqueue(Tuple.Create(node.left, idx*2));
                }

                if(node.right != null)
                {
                    q.Enqueue(Tuple.Create(node.right, idx*2+1));
                }
                
            }

            res = Math.Max(res, last - first + 1);
        }

        return res;
    }
}
````

#### <span style='color:#0066cc'>5.9. Min Time To Burn BTFrom Target</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a target node data and a root of binary tree. If the target is set on fire, determine the shortest amount of time needed to burn the entire binary tree.
> 
> It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.
> </span>

##### 💻 Solution

````csharp
/*
 // Definition for a binary tree node.
 public class TreeNode {
     public int val;
     public TreeNode left;
     public TreeNode right;

     public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }
*/

public class Solution {
    public int TimeToBurnTree(TreeNode root, int start) {
       // Approach: Store the parent from target till the root node
       // now start buring the node fron target 
       // Traverse in all the directions(left, right, parent)
       // the longest direction means till the BFS queue is not empty keep iterating

       // 1. BFS to Store the parent
       Dictionary<TreeNode, TreeNode> parentMap = new Dictionary<TreeNode, TreeNode>();
       Queue<TreeNode> q = new Queue<TreeNode>();
       TreeNode startNode = null;

       if(root != null)
       {
            q.Enqueue(root);
       }

       while(q.Count > 0)
       {
            var curr = q.Dequeue();
            if(curr.data == start)
            {
                startNode = curr;
            } 
            
            if(curr.left != null)
            {
                parentMap[curr.left] = curr;
                q.Enqueue(curr.left);
            }

            if(curr.right != null)
            {
                parentMap[curr.right] = curr;
                q.Enqueue(curr.right);
            }
       }

       // Clear the Queue to Reuse the existing Queue
       // BFS to calculate the burning time
       q.Clear();
       int time = 0;
       HashSet<TreeNode> visited = new HashSet<TreeNode>();

        if(startNode != null)
        {
            q.Enqueue(startNode);
            visited.Add(startNode);
        }

        while(q.Count > 0)
        {
            int size = q.Count;
            // This condition is required to track if any new node is burned or not ?
            bool burned = false;

            for(int i=0; i< size; i++)
            {
                var curr = q.Dequeue();

                if(curr.left != null && !visited.Contains(curr.left))
                {
                    q.Enqueue(curr.left);
                    visited.Add(curr.left);
                    burned = true;
                }

                if(curr.right != null && !visited.Contains(curr.right))
                {
                    q.Enqueue(curr.right);
                    visited.Add(curr.right);
                    burned = true;
                }

                if(parentMap.ContainsKey(curr) && !visited.Contains(parentMap[curr]))
                {
                    q.Enqueue(parentMap[curr]);
                    visited.Add(parentMap[curr]);
                    burned = true;
                }
            }

            if(burned)
                time++;
        }
       
        return time;
    }
}
````

#### <span style='color:#0066cc'>5.10. Print Nodes At KDistance From Target</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root of a binary tree, the value of a target node target, and an integer k. Return an array of the values of all nodes that have a distance k from the target node.
> 
> The answer can be returned in any order (N represents null).
> 
> Note: Although input shows target as a value, internally it refers to the TreeNode with that value.
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int data;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int val) { data = val; left = null, right = null }
 * }
 */

public class Solution
{
    public IList<int> distanceK(TreeNode root, TreeNode target, int k)
    {
        Dictionary<int, TreeNode> parentMap = new Dictionary<int, TreeNode>();

        Queue<TreeNode> q = new Queue<TreeNode>();
        if(root != null)
            q.Enqueue(root);

        while(q.Count > 0)
        {
            var node = q.Dequeue();
            if(node.left != null) 
            {
                q.Enqueue(node.left);
                parentMap[node.left.data] = node;
            }
            if(node.right != null) 
            {
                q.Enqueue(node.right);
                parentMap[node.right.data] = node;
            }

            // if(node.data == target.data) break;
        }
        
        // Now start from the target node and traverse its neighbours(leftChild, rightChild, parent)
        // User BFS traversal using queue
        // Maintain visited nodes as it will again revisit the parent node and then again its child

        q.Clear();
        List<int> nodesToPrint = new List<int>();
        int distance = 0;
        HashSet<int> visited = new HashSet<int>();

        if(target != null)
        {
            q.Enqueue(target);
            visited.Add(target.data);
        }

        while(q.Count > 0)
        {
            if(distance == k)
            {
                while(q.Count > 0)
                {
                    nodesToPrint.Add(q.Dequeue().data);
                }
                return nodesToPrint;
            }

            int size = q.Count;

            for(int i=0; i<size; i++)
            {
                var curr = q.Dequeue();

                if(parentMap.ContainsKey(curr.data) && !visited.Contains(parentMap[curr.data].data))
                {
                    q.Enqueue(parentMap[curr.data]);
                    visited.Add(parentMap[curr.data].data);
                }

                if(curr.left != null && !visited.Contains(curr.left.data))
                {
                    q.Enqueue(curr.left);
                    visited.Add(curr.left.data);
                }

                if(curr.right != null && !visited.Contains(curr.right.data))
                {
                    q.Enqueue(curr.right);
                    visited.Add(curr.right.data);
                }
            }
            distance++;
        }

        return nodesToPrint;
    }
}
````

#### <span style='color:#0066cc'>5.11. Print Root To Leaf BT</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root of a binary tree. Return all the root-to-leaf paths in the binary tree.
> 
> A leaf node of a binary tree is the node which does not have a left and right child.
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int data;
 *     public TreeNode left;
 *     public TreeNode right;
 *      public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
 *          this.data = val;
 *          this.left = left;
 *          this.right = right;
 *      }
 * }
 */

public class Solution {
    public List<List<int>> AllRootToLeaf(TreeNode root) {
        // Your code goes here

        List<List<int>> res = new List<List<int>>();

        if(root == null) return res;
        Traverse(root, res, new List<int>());
        return res;
    }

    private void Traverse(TreeNode root, List<List<int>> res, List<int> path)
    {
        if(root == null) return;

        // Adding the node data here as if it is the leaf node it should be included
        path.Add(root.data);

        // Checking if its a leaf node then add the current Path
        if(root.left == null && root.right == null)
        {
            var lst = new List<int>(path);
            res.Add(lst);

            // Once Path is added then leaf node is the one which should be removed in the 1st place during backtracking
            path.RemoveAt(path.Count-1);
            return;
        }
        
        Traverse(root.left, res, path);
        Traverse(root.right, res, path);
        path.RemoveAt(path.Count-1);
    }
}
````

#### <span style='color:#0066cc'>5.12. Symmetrical BT</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public bool IsSymmetric(TreeNode root) {
        return Solve(root.left, root.right);
    }

    private bool Solve(TreeNode root1, TreeNode root2)
    {
        if(root1 == null && root2 == null) return true;

        if(root1 == null || root2 == null) return false;

        if(root1.data != root2.data) return false;

        return Solve(root1.left, root2.right) && Solve(root1.right, root2.left);
    }
}
````

### <span style='color:#009900'>📁 5.13. Traversal</span>

##### <span style='color:#0066cc'>5.13.1. Boundary Traversal</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given a root of Binary Tree, perform the boundary traversal of the tree. 
> 
> The boundary traversal is the process of visiting the boundary nodes of the binary tree in the anticlockwise direction, starting from the root.
> 
> The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.
> 
> The left boundary is the set of nodes defined by the following:
> 
> The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
> 
> If a node in the left boundary and has a left child, then the left child is in the left boundary.
> 
> If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
> 
> The leftmost leaf is not in the left boundary.
> 
> The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public List<int> Boundary(TreeNode root) {
        // 1. Add LeftBoundary
        // 2. Add Leaf Nodes for left subtree
        // 3. Add Leaf Nodes for right subtree
        // 4. Add RightBoundary

        List<int> res = new List<int>();

        // Checking if given root node is null then simply return empty list
        if(root == null) return res;

        res.Add(root.data);
        // Checking if rootNode is leafNode then we need to return the rootNode value only
        if(root.left == null && root.right == null) return res;

        AddLeftBoundary(root, res);
        AddLeafNodes(root, res);
        AddRightBoundary(root, res);

        return res;
    }

    private void AddLeafNodes(TreeNode root, List<int> res)
    {
        if(root.left == null && root.right == null)
        {
            res.Add(root.data);
            return;
        }

        if(root.left != null)
            AddLeafNodes(root.left, res);
        if(root.right != null)
            AddLeafNodes(root.right, res);
    }

    private void AddLeftBoundary(TreeNode root, List<int> res)
    {
        if(root.left == null) return;

        TreeNode curr = root.left;
        // res.Add(curr.data);

        while(curr.left != null || curr.right != null)
        {
            if(curr.left != null)
            {
                res.Add(curr.data);
                curr = curr.left;
            }
            else if(curr.right != null)
            {
                res.Add(curr.data);
                curr = curr.right;
            }
        }
    }

    private void AddRightBoundary(TreeNode root, List<int> res)
    {
        if(root.right == null) return;

        TreeNode curr = root.right;
        List<int> temp = new List<int>();

        while(curr.left != null || curr.right != null)
        {
            if(curr.right != null)
            {
                temp.Add(curr.data);
                curr = curr.right;
            }
            else if(curr.left != null)
            {
                temp.Add(curr.data);
                curr = curr.left;          
            }
        }

        for(int i=temp.Count-1; i>=0; i--)
        {
            res.Add(temp[i]);
        }

    }
}
````

##### <span style='color:#0066cc'>5.13.2. In Order Traversal</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> *
>  * Definition for a binary tree node.
>  * public class TreeNode 
>  * }
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public List<int> Inorder(TreeNode root) {
        //your code goes here
        List<int> res = new List<int>();

        Traverse(root, res);
        return res;
    }

    private void Traverse(TreeNode root, List<int> res)
    {
        if(root == null) return;

        Traverse(root.left, res);
        res.Add(root.data);
        Traverse(root.right, res);
    }
}
````

##### <span style='color:#0066cc'>5.13.3. Level Order Traversal</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Approach 1: Using BFS and Tuple (level, Node) in Queue
> </span>

##### 💻 Solution

````csharp
public class Solution
{
    public IList<IList<int>> levelOrder(TreeNode root)
    {
        //your code goes here

        IList<IList<int>> res = new List<IList<int>>();

        if (root == null) return res;

        Queue<(int, TreeNode)> q = new Queue<(int, TreeNode)>();

        q.Enqueue((0, root));


        while (q.Count > 0)
        {
            var node = q.Dequeue();

            if (node.Item1 >= res.Count)
            {
                res.Add(new List<int>());
            }

            res[node.Item1].Add(node.Item2.data);

            if (node.Item2.left != null)
            {
                q.Enqueue((node.Item1 + 1, node.Item2.left));
                // res[node.item1].Add(node.item2.left.data);
            }

            if (node.Item2.right != null)
            {
                q.Enqueue((node.Item1 + 1, node.Item2.right));
                // res[node.item1].Add(node.item2.right.data);
            }
        }

        return res;
    }
}

// Approach 2: Recursive 

public class Solution {
    public IList<IList<int>> LevelOrder(TreeNode root) {
        
        IList<IList<int>> res = new List<IList<int>>();
        Traverse(root, res, 1);
        return res;
    }

    private void Traverse(TreeNode node, IList<IList<int>> result, int level)
    {
        if(node == null)
            return;
        
        if(result.Count < level)
        {
            result.Add(new List<int>());
        }
        result[level-1].Add(node.data);
        Traverse(node.left, result, level+1);
        Traverse(node.right, result, level+1);
    }
}
````

##### <span style='color:#0066cc'>5.13.4. Post Order Traversal</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> *
>  * Definition for a binary tree node.
>  * public class TreeNode 
>  * }
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public List<int> postorder(TreeNode root) {
        // Your code goes here

        List<int> res = new List<int>();
        Traverse(root, res);

        return res;
    }

    private void Traverse(TreeNode root, List<int> res)
    {
        if(root == null) return;

        Traverse(root.left, res);
        Traverse(root.right, res);
        res.Add(root.data);
    }
}
````

##### <span style='color:#0066cc'>5.13.5. Pre Order Traversal</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> *
>  * Definition for a binary tree node.
>  * public class TreeNode 
>  * }
> </span>

##### 💻 Solution

````csharp
public class Solution {
    public List<int> Preorder(TreeNode root) {
        //your code goes here
        List<int> res = new List<int>();

        Traverse(root, res);

        return res;
    }

    private void Traverse(TreeNode root, List<int> res)
    {
        if(root == null) return;

        res.Add(root.data);
        Traverse(root.left, res);
        Traverse(root.right, res);
    }
}
````

##### <span style='color:#0066cc'>5.13.6. Top View DFS</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root of a binary tree, return the top view of the binary tree.
> 
> Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. Return nodes from the leftmost node to the rightmost node. Also if 2 nodes are outside the shadow of the tree and are at the same position then consider the left ones only(i.e. leftmost).
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int data;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int val) { data = val; left = null, right = null }
 * }
 **/

public class Solution
{
    public List<int> TopView(TreeNode root)
    {
        SortedDictionary<int, int> dict = new SortedDictionary<int, int>();

        Traverse(root, dict, 0, 0);

        return dict.Values.ToList();

    }

    private void Traverse(TreeNode root, SortedDictionary<int,int> dict, int row, int col)
    {
        if(root == null) return;

        if(!dict.ContainsKey(col))
        {
            dict.Add(col, root.data);
        }

        Traverse(root.left, dict, row+1, col-1);
        Traverse(root.right, dict, row+1, col+1);
    }
}
````

##### <span style='color:#0066cc'>5.13.7. Vertical Order Traversal</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Compute the binary tree's vertical order traversal given its root.
> 
> The left and right children of a node at location (row, col) will be at (row + 1, col - 1) and (row + 1, col + 1), respectively. The tree's root is located at (0, 0).
> 
> The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values. Return the binary tree's vertical order traversal.
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution
{
    public IList<IList<int>> VerticalTraversal(TreeNode root)
    {
         var res = new List<IList<int>>();
        if (root == null) return res;

        // SortedDictionary: column -> List of (row, value) as Tuple<int, int>
        var dict = new SortedDictionary<int, List<Tuple<int, int>>>();

        Traverse(root, 0, 0, dict);

        foreach (var key in dict.Keys)
        {
            // Sort by row, then value
            var sorted = dict[key]
                .OrderBy(x => x.Item1) // Item1 is row
                .ThenBy(x => x.Item2)  // Item2 is value
                .Select(x => x.Item2)  // Select the value
                .ToList();
            res.Add(sorted);
        }

        return res;
    }

    private void Traverse(TreeNode node, int row, int col, SortedDictionary<int, List<Tuple<int, int>>> dict)
    {
        if (node == null) return;
        if (!dict.ContainsKey(col))
        {
            dict[col] = new List<Tuple<int, int>>();
        }
        dict[col].Add(Tuple.Create(row, node.val));

        Traverse(node.left, row + 1, col - 1, dict);
        Traverse(node.right, row + 1, col + 1, dict);
    }
}
````

##### <span style='color:#0066cc'>5.13.8. Zig Zag Or Spiral Traversal</span>

##### 📋 Problem Statement

> <span style='color:#555555'>
> Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
> (i.e., from left to right, then right to left for the next level and alternate between).
> </span>

##### 💻 Solution

````csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int data;
 *     public TreeNode left;
 *     public TreeNode right;
 *     TreeNode(int val) { data = val; left = null, right = null }
 * }
 */

public class Solution {
    public IList<IList<int>> ZigzagLevelOrder(TreeNode root) {
        //your code goes here
        IList<IList<int>> result = new List<IList<int>>();
        if(root == null) return result;

        return Traverse(root, result, true);
    }

    private IList<IList<int>> Traverse(TreeNode root, IList<IList<int>> res, bool isLeftToRight)
    {
        Queue<TreeNode> q = new Queue<TreeNode>();
        q.Enqueue(root);

        while(q.Count > 0)
        {
            // This is something which is helping to maintain same queue and still able to distingues level nodes
            int size = q.Count;

            // Maintain an array to store the level nodes values to add in result List
            int[] levelArray = new int[size];
            
            for(int i=0; i<size; i++)
            {
                var node = q.Dequeue();

                if(isLeftToRight)
                {
                    levelArray[i] = node.data;
                }
                else
                {
                    levelArray[size-i-1] = node.data;
                }

                if(node.left != null)
                {
                    q.Enqueue(node.left);
                }
                if(node.right != null)
                {
                    q.Enqueue(node.right);
                }
            }

            isLeftToRight = !isLeftToRight;
            // Now one level has been completed. Add all the traversed array in the result list
            res.Add(levelArray.ToList());
        }

        return res;
    }
}
````

---

---

