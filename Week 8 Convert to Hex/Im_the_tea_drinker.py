x = input("Text to convert: ")

def convert_to_hex(txt):
    txt = list(txt)
    hex_list = []
    for i in txt:
        hex_list.append(hex(ord(i)).lstrip("0x"))
    
    txt = " ".join(hex_list)
    return txt
        
    
    


print(convert_to_hex(x))