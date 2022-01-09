from random import sample
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

#print("=====",PinSpan([1,2,3]),"=====", len(PinSpan([1,2,3])))



import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

######## Here we declare the length of PINs
k=2
#######


num_elements=[]
for num in range(10**k):
    num_elements.append(pin_rep(num,k))


#print(num_elements)
#w=findsubsets(num_elements,3)
#print(type(w[1]))
#print(len(w))
#w=sample(num_elements,10)
#print(w)


def ListPinSpan(List):
    A=set()
    for j in range(len(List)):
        A = A.union(PinSpan(list(List[j])))
    #print(len(A))
    if len(A)>=10**k:
        return True
    else:
        return False


def Is_There_Good_Choice(n,k):
    for j in tqdm(range(n)):
        w = sample(num_elements, k)
        if ListPinSpan(w):
            counter=True
            print("The set ",w, "is a good choice for adversary of length ", len(w))
            break



#Is_There_Good_Choice(1000000,83)

#global counter
counter=True
j=100
while (counter):
    w = sample(num_elements,j)
    if ListPinSpan(w):
        counter = True
        print("The set ", len(w), "is a good choice for adversary")
        break