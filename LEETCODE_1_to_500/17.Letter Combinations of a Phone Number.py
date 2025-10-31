from itertools import product    
def letterCombinations(digits: str):
    def combinationTwo(s1,s2):
        return [''.join(p) for p in product(s1, s2)]
    def combinationThree(s1,s2,s3):
        return [''.join(p) for p in product(s1, s2, s3)]
    def combinationFour(s1,s2,s3,s4):
        return [''.join(p) for p in product(s1, s2, s3, s4)]        

    d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    l = len(digits)

    if l==1:
        return list(d[digits])

    if l==2:
        return combinationTwo(d[digits[0]],d[digits[1]])

    if l==3:
        return combinationThree(d[digits[0]],d[digits[1]],d[digits[2]])

    if l==4:
        return combinationFour(d[digits[0]],d[digits[1]],d[digits[2]],d[digits[3]]) 