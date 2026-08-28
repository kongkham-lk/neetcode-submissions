class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_pair = {}
        res = 0
        prev_total_spent = 0

        for i in range(len(position)): pos_speed_pair[position[i]] = speed[i]

        position = sorted(position)
        # print(position, pos_speed_pair)
        for i in range(len(position)-1, -1, -1):
            # print(i)
            p = position[i]
            curr_total_spent = ((target - p) / pos_speed_pair[p])
            # print(p, pos_speed_pair[p], prev_total_spent, curr_total_spent)
            if curr_total_spent > prev_total_spent:
                res += 1
                prev_total_spent = curr_total_spent
        # print(res)
        return res
        #01234567890
        # 1  1  1  1 
        #    4 4 4 4
        #00000000000
        # 1 1 1 1 11            
        #    4 4 4 4      
        #       7777            