def helpfulMaths(string1):
    s =sorted(string1)
    finalstring = ""

    for i in range(len(s)):
        finalstring+=s[i]+"+"
    return finalstring[:len(finalstring)-1]


if __name__ == '__main__':
    string = input().split("+")
    print(helpfulMaths(string))

