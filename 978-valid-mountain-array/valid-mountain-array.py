class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        largest = float('-inf')
        for i in range(len(arr)):
            largest = max(largest, arr[i])

        if largest == arr[0]:
            return False

        i = 0
        while i < len(arr):
            if i > 0 and arr[i] == arr[i-1]:
                return False
            elif i > 0 and arr[i] < arr[i-1]:
                break
            else:
                i += 1

        if i == len(arr):  # never decreased
            return False

        for k in range(i, len(arr)):
            if arr[k] >= arr[k-1]:
                return False

        return True
