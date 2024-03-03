class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue=deque(students)
        stack=list(reversed(sandwiches))
        while queue and stack:
            if queue[0]==stack[-1]:
                queue.popleft()
                stack.pop()
            else:
                temp=queue.popleft()
                queue.append(temp)
            if 0 not in queue:
                if stack and stack[-1]==0:
                    return len(queue)
            if 1 not in queue:
                if stack and stack[-1]==1:
                    return len(queue)

        return 0
        