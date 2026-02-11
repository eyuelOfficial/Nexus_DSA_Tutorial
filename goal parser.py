class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        i = 0
        while i < len(command):
            if command[i:i+2] == "()":
                ans.append("o")
                i += 2
            elif command[i:i+4] == 'al':
                ans.append('al')
                i += 4

            else:
                ans.append('G')
        return ans
        
                
