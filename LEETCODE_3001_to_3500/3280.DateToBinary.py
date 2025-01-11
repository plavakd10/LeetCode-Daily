def convertDateToBinary(date: str) -> str:
    return "-".join(f"{int(d):b}" for d in date.split("-"))

#In Python, the :b format specifier inside an f-string is used to format numbers as binary. It converts an integer to its binary representation.