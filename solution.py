class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs and len(strs) > 1:
            sorted_list = sorted(strs)
            first = sorted_list[0]
            last = sorted_list[-1]
            for i in range(len(first)):
                if len(last) > i and last[i] == first[i]:
                    prefix += last[i]
                else:
                    return prefix
        elif len(strs) == 1:
            return strs[0]
        else:
            return ""
        return prefix
