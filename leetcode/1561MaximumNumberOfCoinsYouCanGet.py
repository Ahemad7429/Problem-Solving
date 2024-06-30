# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

def maxCoins(piles):
    piles.sort(reverse=True)
    n = len(piles) // 3
    return sum(piles[i] for i in range(1, 2 * n, 2))
