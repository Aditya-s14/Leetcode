class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                    break
                else: # if asteroid is smaller than the last element of stack
                    break # we break out of the while loop and move to next asteroid(curr ast breaks)

            else:    # this else gets executed if break from while loop is not executed
                stack.append(ast)

        return stack
