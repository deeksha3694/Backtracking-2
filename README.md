# Backtracking-2

## Problem1 
Subsets (https://leetcode.com/problems/subsets/)

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

solution: solved using backtracking

1) An empty array ditinct is initialized.
2) Inside subset method another temporary array is initialized to add each element and then backtrack function is called.
3) Inside the backtrack for loop is started from the 0th element added to list and recurisvely next element is called and added into the list.  
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]

Time complexity:O(N * 2^N) to generate all subsets and copy them in to lists
Space Complexity: O(2^N) exactly the subsets formed 

## Problem2

Palindrome Partitioning(https://leetcode.com/problems/palindrome-partitioning/)

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

