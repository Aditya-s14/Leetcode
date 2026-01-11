class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        Example:
        Input  : " ( ( ) ( ) ) ( ( ) )"
        Depth  : 0 1 2 1 2 1 0 1 2 1 0

        Observation:
        1) Add '(' only if nesting depth (check) > 1
        2) Add ')' only if nesting depth (check) > 0
        """

        check = 0              # keeps track of current nesting depth
        res = []               # list to efficiently build the result string

        for c in s:
            # If opening parenthesis is found
            if c == '(':
                check += 1     # increase nesting depth

                # Ignore the outermost '(' (depth == 1)
                if check > 1:
                    res.append(c)

            # If closing parenthesis is found
            elif c == ')':
                check -= 1     # decrease nesting depth

                # Ignore the outermost ')' (depth == 0 after decrement)
                if check > 0:
                    res.append(c)

        # Convert list of characters back to string
        return "".join(res)
