class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # we are given the array [3,2,2,1]
        people.sort()
        r = len(people) - 1
        l = 0 
        ans = 0 

        while l <= r:
            remain = limit - people[r]
            r -= 1
            ans += 1 
            if l <= r and remain >= people [l]:
                l += 1
        return ans
