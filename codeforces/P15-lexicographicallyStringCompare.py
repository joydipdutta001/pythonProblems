def lexicographyComparison(s1,s2):

    if s1>s2:
        return 1
    elif s1 == s2:
        return 0
    else:
        return -1

if __name__ == '__main__':

    string1 = input().lower()
    string2 = input().lower()

    print(lexicographyComparison(string1,string2))