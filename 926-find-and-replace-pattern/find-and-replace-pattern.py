class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if len(word)!=len(pattern):
                continue
            wp = {}
            pw = {}
            for i in range(len(word)):
                char_w = word[i]
                char_p = pattern[i]
                if (char_w in wp and wp[char_w]!=char_p) or (char_p in pw and pw[char_p]!=char_w):
                    break
                
                
                wp[char_w] = char_p
                pw[char_p] = char_w
            else:
                res.append(word)

        return res


        