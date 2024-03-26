class Solution:
    def interpret(self, command: str) -> str:
        replace=""
        for i in range(0,len(command)):
            if command[i]=="G":
                replace=replace+"G"
                continue
            elif command[i]=="(":
                if command[i+1]==")":
                    replace=replace+"o"
                    i+=1
                elif command[i+1]=="a":
                    replace=replace+"al"
                else:
                    continue
            else:
                continue
        return replace
