# First Version
import copy
Swap=set()
WrongDigit=set()
WrongList=set()


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
    for j in range(len(List)-1):
        Swap.add(swapPositions(List,j,j+1))
        Swap.add(swapPositions(List,0,0))
    return Swap


#This function generate all possible errors for just one wrong digit
def WrongDigitErrors(List,i):
    new_list = copy.deepcopy(List)
    for j in range(10):
        new_list[i]=j
        WrongDigit.add(tuple(new_list))
    return WrongDigit


def WrongDigitErrorFull(List):
    for j in range(len(List)):
        WrongDigitErrors(List,j)
    return WrongDigit


def PinSpan(List):
    return swapErrors(List).union(WrongDigitErrorFull(List))



print(PinSpan([1,2,3,4,5]))



#This function return all n-element subsets of the set "S"
import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))


# Let's start for the case of 3 digits PIN's
num3=[]
for num in range(1000):
    num3.append(pin_rep(num,3))

