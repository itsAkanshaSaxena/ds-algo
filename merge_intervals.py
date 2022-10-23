class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        stack = []
        if intervals:
            stack.append(intervals[0])
        for i in range(1, len(intervals)):
            print(intervals[i])
            if intervals[i][0] > stack[-1][1]:
                stack.append(intervals[i])
            else:
                stack[-1][1] = max(intervals[i][1], stack[-1][1])

        return stack
