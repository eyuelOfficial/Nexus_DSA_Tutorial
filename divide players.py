class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        team_sum = sum(skill) // (len(skill) // 2)
        ans = 0

        while left < right:
            if skill[left] + skill[right] != team_sum:
                return -1
            ans += skill[left] * skill[right]
            left += 1
            right -= 1

        return ans
