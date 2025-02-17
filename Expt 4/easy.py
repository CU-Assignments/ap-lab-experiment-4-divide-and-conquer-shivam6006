# Longest Nice Substring 

class Solution(object):
    def longestNiceSubstring(self, s):
        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if all(c.lower() in substr and c.upper() in substr for c in substr):
                    if len(substr) > len(longest):
                        longest = substr
        return longest