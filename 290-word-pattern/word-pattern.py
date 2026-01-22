class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        hm_ps = {}
        hm_sp = {}
        s_list = s.split()
        if len(pattern)!=len(s_list):
            return False

        for i in range(len(pattern)):
            char_p = pattern[i]
            word_s = s_list[i]

            if (char_p in hm_ps and hm_ps[char_p]!=word_s) or (word_s in hm_sp and hm_sp[word_s]!=char_p):
                return False
            hm_ps[char_p] = word_s
            hm_sp[word_s] = char_p
        return True
        