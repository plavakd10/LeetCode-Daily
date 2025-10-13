from collections import Counter
from itertools import pairwise
def removeAnagrams(words):
    def is_not_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return True
        char_count = Counter(s)
          
        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return True
          
        return False
      
    result = [words[0]]
    for prev_word, curr_word in pairwise(words):
        if is_not_anagram(prev_word, curr_word):
            result.append(curr_word)
      
    return result 