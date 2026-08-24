def isPalindromic(self, s: str) -> bool:
    fin_str  = ""
    for c in s:
        num = ord(c)
        bin_value = bin(num)[2:]
        bin_value = "0"*(8-len(bin_value)) + bin_value
        fin_str += bin_value
    return fin_str == fin_str[::-1]   