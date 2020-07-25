""" 
////////////////////////////////////////////////////////////////////////////////
                author_name= Joydip Dutta,
                author_email= duttajoydip98@gmail.com,
                github_id = joydipdutta001
                linkedIn_id = Joydip Dutta (JD)
                Website = cybotians.com

                Problem No. = Day-17
                

                
                
 ////////////////// THANK YOU /////////////////////////////////////////////////   
 """


class Calculator(Exception):
    def power(self, n, p):
        if (n < 0 or p < 0):
            raise Calculator("n and p should be non-negative")
        else:
            return pow(n, p)


if __name__ == '__main__':
    # Write Your code here

    myCalculator = Calculator()
    T = int(input())
    for i in range(T):
        n, p = map(int, input().split())
        try:
            ans = myCalculator.power(n, p)
            print(ans)
        except Exception as e:
            print(e)