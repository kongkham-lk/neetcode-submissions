class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_pair = {}
        res, prev_total_spent = 0, 0

        for i in range(len(position)): pos_speed_pair[position[i]] = speed[i]

        position = sorted(position)
        for i in range(len(position)-1, -1, -1):
            p = position[i]
            curr_total_spent = ((target - p) / pos_speed_pair[p])
            if curr_total_spent > prev_total_spent:
                res += 1
                prev_total_spent = curr_total_spent
        return res