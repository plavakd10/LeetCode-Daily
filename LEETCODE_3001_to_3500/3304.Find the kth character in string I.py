def kthCharacter(self, k: int) -> str:
    word = 'a'
    def rec(word,k):
        for i in word:
            if 97<=ord(i)<122:
                word+=chr(ord(i)+1)
            else:
                word+=chr((ord(i)%122)+97)
        if k>len(word):
            return rec(word,k)
        else:
            return word[k-1]
    return rec(word,k)