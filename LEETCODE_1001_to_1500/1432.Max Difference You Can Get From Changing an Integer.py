def maxDiff(num: int) -> int:
    return firstInstance(str(num))

def firstInstance(s):
    index_one, index_nine = 0,0
    replacement = "1"
    for i, v in enumerate(s):
        if i==0 and v!="1":
            index_one = i
            break
        if i>0 and v!="0" and v!="1":
            replacement = "0"
            index_one = i
            break
    for i,v in enumerate(s):
        if v!="9":
            index_nine = i
            break        
    min_arr = s.replace(s[index_one],replacement)
    max_arr = s.replace(s[index_nine],"9")

    return int(max_arr)-int(min_arr)