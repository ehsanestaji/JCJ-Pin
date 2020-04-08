# First Version
import copy
Swap=set()
WrongDigit=set()
WrongList=set()
new_WrongDigit=set()


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
    new_Swap=copy.deepcopy(Swap)
    Swap.clear()
    return new_Swap


#This function generate all possible errors for just one wrong digit
def WrongDigitErrors(List,i):
    new_list = copy.deepcopy(List)
    for j in range(10):
        new_list[i]=j
        WrongDigit.add(tuple(new_list))
    #WrongDigit.clear()
    return new_WrongDigit

def WrongDigitErrorFull(List):
    new_list = copy.deepcopy(List)
    for i in range(len(new_list)):
        WrongDigitErrors(new_list,i)
    return WrongDigit

def PinSpan(List):
    new_list = copy.deepcopy(List)
    WrongDigit.clear()
    return swapErrors(new_list).union(WrongDigitErrorFull(new_list))





import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

w=findsubsets({1,2,3},2)
print(PinSpan([1,2,3]),len(PinSpan([1,2,3])))
print(PinSpan([2,5,4]),len(PinSpan([2,5,4])))
print(PinSpan([6,7]),len(PinSpan([6,7])))









#print(PinSpan([1,2,3,4,5]))



#This function return all n-element subsets of the set "S"



# Let's start for the case of 3 digits PIN's
num3=[]
for num in range(100):
    num3.append(pin_rep(num,2))

#print(list(num3))



#for j in range(len(w)):
 #   print(w[j],"==========" ,PinSpan(list(w[j])), len(PinSpan(list(w[j]))))