""" 
////////////////////////////////////////////////////////////////////////////////
                author_Name= Joydip Dutta,
                author_Email= duttajoydip98@gmail.com,
                github_ID = joydipdutta001
                linkedIn_ID = Joydip Dutta (JD)
                Website = cybotians.com
                Problem No. = Day-04
                
                Thank You...
 ///////////////////////////////////////////////////////////////////////////////   
 """

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            self.ageNow = 0
        else:
            self.ageNow = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.ageNow >= 18:
            print("You are old.")
        elif self.ageNow >= 13:
            print("You are a teenager.")
        else:
            print("You are young.")
    def yearPasses(self):
        self.ageNow +=1
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


