from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            count = [0] * 26  # frequency of each character

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            if key not in result:
                result[key] = []
            result[key].append(s)

        return list(result.values())
