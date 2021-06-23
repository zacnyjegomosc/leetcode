# licence-key-formatting

You are given a license key represented as a string `s` that consists of only alphanumeric characters and dashes. The string is separated into `n + 1` groups by `n` dashes. You are also given an integer `k`.

We want to reformat the string s such that each group contains exactly `k` characters, except for the first group, which could be shorter than `k` but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Input: `s = "2-5g-3-J", k = 2`

Output: `"2-5G-3J"`

More about this problem: https://leetcode.com/problems/license-key-formatting/

## Performance of my solution

LeetCode says:

> - Your runtime beats 91.39 % of python3 submissions.
> - Your memory usage beats 95.72 % of python3 submissions.

