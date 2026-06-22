class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join([x.lower() for x in s if x.isalnum()])

        return string == string[::-1]
        