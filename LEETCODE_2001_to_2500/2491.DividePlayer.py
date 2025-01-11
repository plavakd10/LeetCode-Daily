def dividePlayers(skill) -> int:
    skill.sort()
    twosum = skill[0]+skill[-1]
    ans = 0
    for i in range(len(skill)//2):
        if skill[i]+skill[-i-1]!=twosum:
            return -1
        ans+=skill[i]*skill[-i-1]    
    return ans 

