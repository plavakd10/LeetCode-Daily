from collections import defaultdict, Counter

def wordSubsets(words1,words2):
    counter_2 = defaultdict(int)
    for w in words2:
        count_w = Counter(w)
        for c,count in count_w.items():
            counter_2[c] = max(counter_2[c],count)
    ans = []
    for word in words1:
        count_w = Counter(word)
        flag=True
        for c,count in counter_2.items():
            if count_w[c]<count:
                flag=False
                break
        if flag:
            ans.append(word)
    return ans    