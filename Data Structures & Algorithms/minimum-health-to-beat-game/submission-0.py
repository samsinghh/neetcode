class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        i, mx = -1, -1
        for idx, d in enumerate(damage):
            if d > mx:
                i = idx
                mx = d
        
        damage[i] = max(0, damage[i] - armor)
        total = sum(damage)
        return total + 1
