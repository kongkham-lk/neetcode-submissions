class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_pair = []
        res, prev_total_spent = 0, 0

        for i in range(len(position)): 
            pos_speed_pair.append((position[i],speed[i]))

        pos_speed_pair.sort(reverse=True)
        for i in range(len(position)):
            curr_total_spent = ((target - pos_speed_pair[i][0]) / pos_speed_pair[i][1])
            if curr_total_spent > prev_total_spent:
                res += 1
                prev_total_spent = curr_total_spent
        return res