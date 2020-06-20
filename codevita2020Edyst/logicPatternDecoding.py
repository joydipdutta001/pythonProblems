# Decode the logic and print the Pattern that corresponds to given input.
#
# If N= 3
#
# then pattern will be :
#
# 10203010011012
# **4050809
# ****607
#
# If N= 4, then pattern will be:
#
# 1020304017018019020
# **50607014015016
# ****809012013
# ******10011

currentNumber = 1
stop = 1
rows = 4  # Rows you want in your pattern

for i in range(0,rows):

    print((i*2) * '*', end="")
    for column in range(0,rows+i):
        print(currentNumber, end='0')
        currentNumber += 1
    print("")
    stop += 1