def stringCap(s):
    l = len(s)
    s = s[0].upper()+s[1:l]
    return s
string = input()
print(stringCap(string))