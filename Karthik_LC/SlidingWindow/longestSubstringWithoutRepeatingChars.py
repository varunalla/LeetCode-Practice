class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wStart = 0
        maxLength = 0
        charFreq = {}

        for wEnd in range(len(s)):
            rChar = s[wEnd]

            if rChar in charFreq:
                wStart = max(wStart, charFreq[rChar] + 1)
            
            charFreq[rChar] = wEnd

            maxLength = max(maxLength, wEnd - wStart + 1)
        return maxLength
