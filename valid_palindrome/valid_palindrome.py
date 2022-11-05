''' valid_palindrome.py - a script that solves the valid palindrome
        algorithm challenge'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = re.sub(r'[^a-zA-Z0-9]', '', str)
        return alpha_num == alpha_num.reversed()