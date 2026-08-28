class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_pair = []
        res = []

        for i in range(len(position)): 
            pos_speed_pair.append((position[i],speed[i]))

        pos_speed_pair.sort(reverse=True)
        for i in range(len(position)):
            curr_total_spent = ((target - pos_speed_pair[i][0]) / pos_speed_pair[i][1])
            # print(res, curr_total_spent)
            if not res or curr_total_spent > res[-1]: res.append(curr_total_spent)
        return len(res)