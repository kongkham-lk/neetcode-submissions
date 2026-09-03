class TimeMap:

    def __init__(self):
        self.people = {}

    def set(self, name: str, mood: str, time: int) -> None:
        # print("0:",self.people)
        self.people[name] = self.people.get(name, {})
        # print("1:",self.people)
        self.people[name][time] = self.people[name].get(time, [])
        # print("2:",self.people)
        self.people[name][time].append(mood)
        # print("3:",self.people)

    def get(self, name: str, time: int) -> str:
        tar_p = self.people.get(name, {})
        # print(name, time, self.people)
        for t in range(time, -1, -1):
            if t in tar_p: return tar_p[t][-1]
        return ""
        
