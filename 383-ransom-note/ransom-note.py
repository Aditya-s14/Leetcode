class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm_ransom = {}
        hm_mag = {}

        for c in ransomNote:
            hm_ransom[c] = hm_ransom.get(c,0)+1

        for c in magazine:
            hm_mag[c] = hm_mag.get(c,0)+1

        for key in hm_ransom:
            if hm_ransom[key]>hm_mag.get(key,0):
                return False
        return True

        