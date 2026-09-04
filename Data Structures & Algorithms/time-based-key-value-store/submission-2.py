class TimeMap:

    def __init__(self):
        self.people = {}

    # # this jus use simple dict of dict for fast lookup
    # def set(self, name: str, mood: str, time: int) -> None:
    #     self.people[name] = self.people.get(name, {})
    #     self.people[name][time] = self.people[name].get(time, [])
    #     self.people[name][time].append(mood)

    # def get(self, name: str, time: int) -> str:
    #     tar_p = self.people.get(name, {})
    #     for t in range(time, -1, -1):
    #         if t in tar_p: return tar_p[t][-1]
    #     return ""

    # Use Binary Search
    def set(self, name: str, mood: str, time: int) -> None:
        self.people[name] = self.people.get(name, [])
        self.people[name].append([time, mood])

    def get(self, name: str, time: int) -> str:
        res, tar_p = "", self.people.get(name, [])
        l, r = 0, len(tar_p)-1
        while l <= r:
            mid = (l+r)//2
            if tar_p[mid][0] <= time:
                res = tar_p[mid][1]
                l = mid+1
            else: r = mid-1
        return res
        
