# First Version
A=set()

# k is the length of PIN and num is the Number
# This function takes a number and the length of Pin and then output Pin representation of this number as a tuple
# We use tuple to be able use add method
def pin_rep(num,k):
    res = list(map(int, str(num)))
    for i in range(k-len(res)):
        res.insert(0,0)
    return tuple(res)


# This function just swap the list elements of "list" with indices "pos1" and "pos2" and after changing the list will be
# without change
def swapPositions(list, pos1, pos2):
    global B
    list[pos1], list[pos2] = list[pos2], list[pos1]
    B=tuple(list)
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return B



# This function generate all possible swapping error list of a PIN
def swapErrors(List):
    print(List)
    for j in range(len(List)-1):
        A.add(swapPositions(List,j,j+1))
        A.add(swapPositions(List,0,0))
    return A




#This function return all n-element subsets of the set "S"
import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))


# Let's start for the case of 3 digits PIN's
num3=[]
for num in range(1000):
    num3.append(pin_rep(num,3))
#print(type(list(num3[0])))


print("This is the list of all errors for 3 digits PIN")
#for j in range(10):
#    print(j, swapErrors(list(num3[j])))
j=998
print(num3[j],"==========",swapErrors(list(num3[j])))

#
#
#
#
#

