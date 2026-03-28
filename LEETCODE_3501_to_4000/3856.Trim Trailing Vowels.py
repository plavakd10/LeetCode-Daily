def trimTrailingVowels(s: str) -> str:
    c = 0
    for letter in s[::-1]:
        if letter in "aeiou":
            c+=1
        else:
            break
    return s[:len(s)-c]