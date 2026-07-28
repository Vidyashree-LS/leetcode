class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        cus = []
        for i in range(len(accounts)):
            cus.append(sum(accounts[i]))
        return max(cus)
        
