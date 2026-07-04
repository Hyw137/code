class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            char = s[end]

            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1

            last_seen[char] = end
            max_length = max(max_length, end - start + 1)

        return max_length