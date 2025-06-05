key = {
'A': '@', 'B': '#', 'C': '$', 'D': '%', 'E': '&', 'F': '*', 'G': '(',
'H': ')', 'I': '!', 'J': '^', 'K': '_', 'L': '+', 'M': '~', 'N': '`',
'O': '-', 'P': '=', 'Q': '{', 'R': '}', 'S': '[', 'T': ']', 'U': ';',
'V': ':', 'W': '"', 'X': "'", 'Y': '<', 'Z': '>', ' ': ' '
    }
c_message = "[)@++ ! $-~=@}& <-; ]- @ [;~~&} %@<? <-; @}& ~-}& +-:&+< @`% ~-}& ]&~=&}@]&"

def decrypt_without_reverse_key(message, key_dict):
    result = ''
    for symbol in message:
        found = False
        for letter in key_dict:
            if key_dict[letter] == symbol:
                result += letter
                found = True
                break
        if not found:
            result += symbol
    return result

# Розшифровка
decoded = decrypt_without_reverse_key(c_message, key)
print("Розшифровано:", decoded)