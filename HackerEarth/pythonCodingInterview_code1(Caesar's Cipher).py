def encrypt(text, text2):

    s=""

    # traverse text 
    for i in range(len(text)):

        char = text[i]
        char2 = text2[i]

        # Encrypt uppercase characters
        if (char.isupper() and char2.isupper()):
            # result += chr((ord(char) + s - 65) % 26 + 65)
            s = s+ str(abs(ord(char) - ord(char2)))
    if len(set(s)) == 1:
        return s[0]
    else:
        return -1

if __name__ == '__main__':
    Q = int(input())
    while Q>0:
        Q-=1

        print(encrypt(input(),input()))

