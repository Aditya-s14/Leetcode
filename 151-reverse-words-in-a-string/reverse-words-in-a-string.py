class Solution:
    def reverseWords(self, s: str) -> str:
        """ s = s.strip()
        s = s.split()[::-1]
        new_str = " ".join(s)
        return new_str """
        res = ""
        s = s.strip()
        count = 0        # initialize space counter
        word = ""        # to build one word at a time

        # traverse from right to left
        for i in range(len(s) - 1, -1, -1):

            # if character is not space, build the word
            if s[i] != " ":
                word = s[i] + word
                count = 0

            # if space is found
            else:
                count += 1

            # when we hit first space after a word, add word to result
            if count == 1 and word:
                res += word + " "
                word = ""

            # skip extra spaces
            if count > 1:
                continue

        # add the last word (first word in original string)
        if word:
            res += word

        # remove trailing space if any
        return res.strip()



        