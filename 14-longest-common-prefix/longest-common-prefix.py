class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: empty list
        if not strs:
            return ""

        # Compare characters column-wise
        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs:
                # If index out of bounds OR mismatch
                if i == len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]
