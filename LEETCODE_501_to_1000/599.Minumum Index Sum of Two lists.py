from collections import Counter
def findRestaurant(list1,list2):
    set1 = set(list1)
    set2 = set(list2)

    c = Counter(set1.intersection(set2))
    min_dict = {} 
    ans = []
    for k,v in c.items():
        min_dict[k] = list1.index(k) + list2.index(k)
    m = min(min_dict.values())
    for k,v in min_dict.items():
        if v==m:
            ans.append(k)
    return ans 