def vowelRemoval(string):
    vowels = "aoyeui"
    c=""
    string1 = string.lower()
    for i in string1:
        if i not in vowels:
            c +=("."+i)
    return c

if __name__ == '__main__':

    string = input()

    print(vowelRemoval(string))