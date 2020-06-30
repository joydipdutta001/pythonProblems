def chatRoom(s):
    message = "hello"
    count = 0
    for i in range(len(s)):
        if s[i] == message[count]:
            count+=1
        if count == len(message):
            return True


if __name__ == '__main__':

    string = input()
    if chatRoom(string):
        print("YES")
    else:
        print("NO")