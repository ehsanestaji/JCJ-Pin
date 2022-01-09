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

#def PinSpan(List):
#    new_list = copy.deepcopy(List)
#    WrongDigit.clear()
#    return swapErrors(new_list).union(WrongDigitErrorFull(new_list))


def PinSpan(List):
    new_list = copy.deepcopy(List)
    #WrongDigit.clear()
    return swapErrors(new_list)




#w=[1,2]
#print(PinSpan(w),"====",len(PinSpan(w)))

import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

####### Here we declare the length of PINs
k=4
#######
num_elements=[]
for num in range(10**k):
    num_elements.append(pin_rep(num,k))

def ListPinSpan(List):
    A=set()
    for j in range(len(List)):
        A = A.union(PinSpan(list(List[j])))
    print(A,"====",len(A))
    if len(A)>=10**k:
        return True
    else:
        return False

#ListPinSpan([[0,1],[2,3],[4,5],[6,7],[8,9],[1,0],[3,2],[5,4]])

Basis=set()
#for i in range(10**k):
#    if (len(num_elements)!=0):
#        Basis=Basis.union(sample(num_elements,1))
#        A=set()
#        List=list(Basis)
#        for j in range(len(Basis)):
#            A = A.union(PinSpan(list(List[j])))
#        num_elements=list(set(num_elements)-A)
#        #print("Step i=",i+1)
#        #print("Current Basis:", Basis)
#        if len(A)==10**k:
#            print("The size of PIN space spanned by current Basis:", len(A),"<><>", i+1)
#        #print("##############################################################")
Basis = set()
for i in range(10 ** k):
    if (len(num_elements) != 0):
        #print("===",i,"====")
        Basis = Basis.union(sample(num_elements, 1))
        A = set()
        List = list(Basis)
        for j in range(len(Basis)):
            A = A.union(PinSpan(list(List[j])))
        num_elements = list(set(num_elements) - A)
        # print("Step i=",i+1)
        # print("Current Basis:", Basis)
        print("The size of PIN space spanned by current Basis:", len(A), "<><>", i + 1)
        #if len(A)==10**k:
        #    print(i+1)
0
for g in range(0):
    for num in range(10 ** k):
        num_elements.append(pin_rep(num, k))
    Basis = set()
    for i in range(10 ** k):
        if (len(num_elements) != 0):
            Basis = Basis.union(sample(num_elements, 1))
            A = set()
            List = list(Basis)
            for j in range(len(Basis)):
                A = A.union(PinSpan(list(List[j])))
            num_elements = list(set(num_elements) - A)
            # print("Step i=",i+1)
            # print("Current Basis:", Basis)
            if len(A)==10**k:
                print(i+1)
                #print("The size of PIN space spanned by current Basis:", len(A), "<><>", i + 1)
            # print("##############################################################")

    #for j in range(len(List)):
    #    A = set()
    #    A = A.union(PinSpan(list(List[j])))
    #    print(A, "======",len(A))
    #if (len(A)==1000):
    #    print("The basis is" ,Basis)
    #else:
    #    num_elements=list(set(num_elements)-A)
    #    print("<<<<<<<", A, ">>>>>>", len(A),len(num_elements))

def Is_There_Good_Choice(n,k):
    for j in tqdm(range(n)):
        w = sample(num_elements, k)
        if ListPinSpan(w):
            counter=True
            print("The set ",w, "is a good choice for adversary of length ", len(w))
            break
#Is_There_Go od_Choice(1000,150)