from typing import List


class LogSystem:

    def __init__(self):
        self.vals = []
        self.mp = {"Year": 4, "Month": 7, "Day": 10,
                   "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id: int, timestamp: str) -> None:
        self.vals.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        k = self.mp[granularity]
        ans = []
        for id, timestamp in self.vals:
            if start[:k] <= timestamp[:k] <= end[:k]:
                ans.append(id)
        return ans

        # Your LogSystem object will be instantiated and called as such:
        # obj = LogSystem()
        # obj.put(id,timestamp)
        # param_2 = obj.retrieve(start,end,granularity)
