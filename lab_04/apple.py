def countApplesAndOranges(s,t,a,b,apples,oranges):
    fruitA = 0
    fruitB = 0   
    for distance in apples: #tests all distances
        location = a + distance  #apple tree to the left
        if location >= s and location <= t:
            fruitA = fruitA + 1           
    for distance in oranges:
        location = b + distance 
        if location >= s and location <= t:
            fruitB = fruitB + 1
            
    print(fruitA)
    print(fruitB)

countApplesAndOranges(7,10,4,12,[3,0],[3,0])
countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])




