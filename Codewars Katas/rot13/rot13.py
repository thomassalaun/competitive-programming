def rot13(message):
    def rot_caracter(y):
        if not y.isalpha():
            return y

        BOUND = 65 if y.isupper() else 97
        rot_val = (ord(y) - BOUND + 13) % 26
        
        return chr(BOUND + rot_val)

    return "".join(rot_caracter(y) for y in message)