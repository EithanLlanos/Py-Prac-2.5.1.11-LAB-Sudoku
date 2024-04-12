# Scenario
# As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

# each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
# each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
# each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
# If you need more details, you can find them here.

# Your task is to write a program which:

# reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
# outputs Yes if the Sudoku is valid, and No otherwise.
# Test your code using the data we've provided.


####################################################################################################
# Test data
# Sample input:

# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672
# Sample output:

# Yes


# Sample input:

# 195743862
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 254938671
# Sample output:

# No


####################################################################################################


# str(2*3*5*7*11*13*17*19*23)

def sdku(txt):
    vrf = {"1":2,"2":3,"3":5,"4":7,"5":11,"6":13,"7":17,"8":19,"9":23}
    val1 = [1]*9
    val2 = [1]*9
    
    ct2=0
    for ndx1,elm1 in enumerate(txt):
        val3=1
        ct1=0
        for ndx2,elm2 in enumerate(elm1):
            val1[ndx2] *= vrf[elm2]
            val3*=vrf[elm2]
            val2 [ct1+ct2] *= vrf[elm2]
            
            if((ndx2+1)%3==0):
                ct1+=1
        if((ndx1+1)%3==0):
            ct2+=3
        print (val2)
        if val3 != 223092870:
            return "No"
    if any(i != 223092870 for i in val1) or any(i != 223092870 for i in val2) : 
        return "No"
    return "Yes"

print("Please enter the sudoku (9 row of inputs):\n")
txt = [None] * 9

#Correct
# txt = ["295743861","431865927","876192543","387459216","612387495","549216738","763524189","928671354","154938672"]


#Incorrect
# txt = ["195743862","431865927","876192543","387459216","612387495","549216738","763524189","928671354","254938671"]
for i in range(9):
    txt[i]=input()
print(sdku(txt))
