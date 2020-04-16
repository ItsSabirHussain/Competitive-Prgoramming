class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        finalres = 0
        i = 0
        while (i < len(s)):
            res = 0
            tmp = i + 1
            chk = len(s)
            while not tmp == len(s) and not chk > len(s):
                for j in range(len(s[:i])):
                    if s[i] == s[j]:
                        chk = j
                    else:
                        res += 1
                tmp +=1
            if res > finalres:
                finalres = res
            i = chk

        return finalres

if __name__ == '__main__':
    test = Solution()
    test.lengthOfLongestSubstring("abcabcbb")