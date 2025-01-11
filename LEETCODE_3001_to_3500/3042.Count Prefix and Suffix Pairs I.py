def countPrefixSuffixPairs(words) -> int:
    count = 0
    for i in range(len(words)-1):
        for j in range(i+1,len(words)):
            count+= words[i]==words[j][:len(words[i])] and words[i]==words[j][-len(words[i]):]
    return count        