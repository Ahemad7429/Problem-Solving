# Foodie
# " There are n food stations along a circular route, where the amount of food at the ith station is food[i].

# You have a body with an unlimited storage capacity for food, and it costs cost[i] of food to travel from the ith station to its next (i + 1)th station. You begin your journey with an empty stomach at one of the food stations.

# Given two integer arrays food and cost, return the starting food station's index if you can travel around the circuit once in the clockwise direction without running out of food, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

# Example 1:

# Input: food = [1,2,3,4,5],  cost = [3,4,5,1,2]

# Output : 3
# Example 2:

# Input :  food = [2,3,4],  cost = [3,4,3]

# Output: -1
# Constraints:

# n == food.length() == cost.length()

# 2 <= n <= 200000

# 0 <= food[i], cost[i] <= 10000

class Solution:
    def canCompleteCircuit(self, food, cost):
        n = len(food)
        
        # Iterate over each station as a potential starting point
        for start_station in range(n):
            remaining_food = 0
            for i in range(n):
                current_station = (start_station + i) % n
                remaining_food += food[current_station] - cost[current_station]
                if remaining_food < 0:
                    break
            # If remaining_food is non-negative after visiting all stations, return start_station
            if remaining_food >= 0:
                return start_station
        return -1