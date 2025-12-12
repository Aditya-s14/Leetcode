class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # function to return first element of interval
        def get_first(i):
            return i[0]

        # sort intervals by starting value
        intervals.sort(key=get_first)

        # start result with first interval
        res = [intervals[0]]

        # iterate through remaining intervals
        for start, end in intervals[1:]:
            lastend = res[-1][1]

            # if overlapping: merge
            if start <= lastend:
                res[-1][1] = max(lastend, end)

            # if not overlapping: add new interval
            else:
                res.append([start, end])

        return res
