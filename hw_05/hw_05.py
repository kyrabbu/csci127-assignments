newList = []
oldList = [1, 2, 3, 4, 5, 6, 7, 8]

def filterodd(l):
    for element in l: #scans each element in list
        if element % 2 == 1: #checks if odd
            newList.append(element) #adds element in list
    print('Input List:', l) 
    print('Odd Numbers:', newList)
    
filterodd(oldList) #test
    
#do nothing

squareList = []
noSquare = [4, 2, 5, 3, 5]

def mapsquare(l):
    for value in l:
        newVal = value ** 2
        squareList.append(newVal)
    print('\nInput List:', l)
    print('Squared Numbers:', squareList)
    
mapsquare(noSquare) #test