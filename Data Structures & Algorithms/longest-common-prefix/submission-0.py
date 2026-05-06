class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(word) for word in strs)
        prefix = ""

        for i in range(min_len):
            check = strs[0][i]
            for word in strs:
                if word[i] != check:
                    return prefix
            prefix += strs[0][i]

        return prefix
