class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        times = collections.Counter(tasks)
        time_value = times.values()
        max_time = max(times.values())
        max_value_times = collections.Counter(time_value)
        max_time_time = max_value_times[max_time]

        if max_time_time > n:
            return len(tasks)
        kong = (n+1-max_time_time)*(max_time-1)
        if len(tasks) > max_time*max_time_time+kong:
            return len(tasks)
        else:
            return max_time*max_time_time+kong
