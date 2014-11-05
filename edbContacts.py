

with open("testFiles/contacts.edb", "rb") as f:
    byte = f.read(1)
    byteCount = 0
    while byte != b"":
        print(byte)
        byteCount += 1
        if byteCount % 0xf == 0 :
            print(end)
        byte = f.read()
