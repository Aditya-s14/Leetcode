class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        last = {c:i for i,c in enumerate(s)}
        stack = []

        for i,c in enumerate(s):
            
            if c in seen:
                continue
            
            while stack and s[i]<stack[-1] and last[stack[-1]]>i:
                seen.remove(stack.pop())


            stack.append(c)
            seen.add(c)


        return "".join(stack)
        
        