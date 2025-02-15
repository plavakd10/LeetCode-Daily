def punishmentNumber(n) -> int:
    def partition(i,cur,target,string):
        if i==len(string) and cur==target:
            return True
        for j in range(i, len(string)):
            if partition(j+1,cur+int(string[i:j+1]),target,string):
                return True
        return False
    ans = 0
    for i in range(1,n+1):
        if partition(0,0,i,str(i*i)):
            ans+=i*i
    return ans                        
        