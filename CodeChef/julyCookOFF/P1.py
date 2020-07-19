def firstNonRepeating(str1):
    a =[a for a in str1 if str1.count(a) == 1]
    if len(a)==0:
        return 1
    else:
        return len(a)


if __name__ == '__main__':
    if __name__ == '__main__':
        testCases = int(input())
        if 1 <= testCases <= 200:
            while testCases:
                testCases -= 1
                n = input()
                G = input()

                if firstNonRepeating(G) == 1:
                    print("YES")
                else:
                    print("NO")