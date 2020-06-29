def words(s):

    ucount=0
    lcount=0
    for i in s:
        if i.isupper():
            ucount+=1
        if i.islower():
            lcount+=1
    if ucount>lcount:
        return s.upper()
    else:
        return s.lower()
if __name__ == '__main__':
    string = input()
    print(words(string))