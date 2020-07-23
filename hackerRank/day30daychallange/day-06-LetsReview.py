""" 
////////////////////////////////////////////////////////////////////////////////
                author_name= Joydip Dutta,
                author_email= duttajoydip98@gmail.com,
                github_id = joydipdutta001
                linkedIn_id = Joydip Dutta (JD)
                Website = cybotians.com
                
                Problem No. = Day-06
                
                
 ////////////////// THANK YOU /////////////////////////////////////////////////   
 """


def letsReview(s):
    rn = ""
    ak = ""
    for i in range(0, len(s)):

        if i % 2 == 0:
            rn += s[i]
        else:
            ak += s[i]
    return rn + " " + ak


if __name__ == '__main__':
    testCases = int(input())
    for _ in range(0, testCases):
        s = input()
        print(letsReview(s))