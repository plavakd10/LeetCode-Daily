def isValid(word: str) -> bool:
    v = ['a','e','i','o','u','A','E','I','O','U']
    a = len(word)>=3
    b = word.isalnum()
    c = False
    d = False
    for i in word:
        if i in v:
            c = True
            break
    for i in word:
        if i not in v and i.isalpha():
            d = True
            break
    return a and b and c and d 