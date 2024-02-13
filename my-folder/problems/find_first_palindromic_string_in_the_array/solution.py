class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(word):
            i = 0
            j = len(word) - 1

            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True
        for word in words:
            if is_palindrome(word):
                return word
        return ""