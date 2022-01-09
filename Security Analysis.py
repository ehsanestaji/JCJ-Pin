# First Version
import copy
Swap = set()
WrongDigit = set()
WrongList = set()
new_WrongDigit = set()
from tqdm import tqdm
from time import sleep

# k is the length of PIN and num is the Number
# This function takes a number and the length of Pin and then output Pin representation of this number as a tuple
# We use tuple to be able use add method
def pin_rep( num , k):
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


print(len(PinSpan([1,2])))

import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

num_elements=[]
for num in range(100):
    num_elements.append(pin_rep(num,2))




#print(num_elements)
#w=findsubsets(num_elements,8)
#print(len(w))

def ListPinSpan(List):
    A=set()
    for j in range(len(List)):
        A = A.union(PinSpan(list(List[j])))
    if len(A)>=100:
        return True
    else:
        return False

#for j in tqdm(range(len(w))):
    #print(j, " of ", len(w))
#    if ListPinSpan(w[j]):
#        print("The set ",w[j], "is a good choice for adversary")
#        break
#print("<<<================>>>")

# Now for the final step I am going to define aa function that checks is there any a good choice for a PIN's of
# of length n and size k