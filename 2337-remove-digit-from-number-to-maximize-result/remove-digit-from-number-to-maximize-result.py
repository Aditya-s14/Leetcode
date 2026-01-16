class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxres = ""

        for i in range(len(number)):
            if number[i] == digit:
                res = number[:i] + number[i+1:]
                if res > maxres:
                    maxres = res

        return maxres
