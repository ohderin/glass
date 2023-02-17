compressedString = "4A1B2C" # input compressed string here

def decompress(compressedString):
    decompressedString = ""
    i = 0
    while i < len(compressedString):
        count = ""
        while compressedString[i].isdigit():
            count += compressedString[i]
            i += 1
        count = int(count)
        char = compressedString[i]
        decompressedString += char * count
        i += 1
    return decompressedString
decompressedString = decompress(compressedString)
print("Decompressed string: \n" + decompressedString) 
