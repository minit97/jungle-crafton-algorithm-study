s = input()

if s[0:2] == "0x":
    print(int(s, 16))
elif s[0] == "0":
    print(int(s, 8))
else:
    print(int(s))

