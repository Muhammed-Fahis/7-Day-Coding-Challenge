class Solution:
    def reverseVowels(self, s: str) -> str:
        #twopointer
        left = 0
        right = len(s) - 1
        vowels = "aeiouAEIOU"
        s = list(s)

        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)
