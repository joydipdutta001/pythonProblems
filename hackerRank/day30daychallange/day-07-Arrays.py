""" 
////////////////////////////////////////////////////////////////////////////////
                author_name= Joydip Dutta,
                author_email= duttajoydip98@gmail.com,
                github_id = joydipdutta001
                linkedIn_id = Joydip Dutta (JD)
                Website = cybotians.com
                
                Problem No. = Day-07
                
                
 ////////////////// THANK YOU /////////////////////////////////////////////////   
 """




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = ""

    for i in range(len(arr)-1,-1,-1):
        res += str(arr[i]) + " "
    print(res)