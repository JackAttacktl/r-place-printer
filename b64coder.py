def ToBase64(byte: int):
    if (byte < 0):
        raise Exception("Byte cannot be less than zero")
    if (byte > 51):
        raise Exception("Byte cannot be greater than 51")
    
    return [*"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"][byte]

def FromBase64(char: str):
    if (len(char) != 1):
        raise Exception("String must be single letter")
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char)