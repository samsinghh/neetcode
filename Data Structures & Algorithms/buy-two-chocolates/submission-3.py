class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sm1, sm2 = prices[0], prices[1]
        if sm1 > sm2:
            sm1, sm2 = sm2, sm1

        for i in range(2, len(prices)):
            if prices[i] < sm1:
                sm2 = sm1
                sm1 = prices[i]
                continue
            if prices[i] < sm2:
                sm2 = prices[i]
        
        if sm1 + sm2 <= money:
            return money - (sm1 + sm2)
        else:
            return money