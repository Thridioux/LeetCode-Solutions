from bisect import bisect_left, insort

class Solution:
    def maxTaskAssign(self, tasks, workers, pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def check(k):
            task_list = tasks[:k]  # k easiest tasks
            available_workers = workers[-k:]  # k strongest workers
            available_workers.sort()
            pills_left = pills

            for i in range(k - 1, -1, -1):
                task = task_list[i]

                # If strongest worker can do it, use them
                if available_workers[-1] >= task:
                    available_workers.pop()
                else:
                    # Use pill: find leftmost worker who can do task with pill
                    idx = bisect_left(available_workers, task - strength)
                    if idx >= len(available_workers):
                        return False  # no one can do it even with pill
                    available_workers.pop(idx)
                    pills_left -= 1
                    if pills_left < 0:
                        return False
            return True

        # Binary search
        low, high, ans = 0, min(len(tasks), len(workers)), 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
