class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque

        students = deque(students)
        sandwiches = deque(sandwiches)

        rotations = 0

        while students and rotations < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                rotations = 0  # reset since someone ate
            else:
                students.append(students.popleft())
                rotations += 1

        return len(students)
