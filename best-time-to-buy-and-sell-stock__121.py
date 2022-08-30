class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_index = max_index = profit = 0
        
        for i in range(len(prices)):
            if prices[i] > prices[max_index] and min_index <= max_index:
                max_index = i
                profit = max(profit, prices[max_index] - prices[min_index])
            if prices[i] < prices[min_index]:
                min_index = max_index = i
    
        return profit
    
    
if __name__ == "__main__":
    print(Solution().maxProfit([7,6,4,3,1]))