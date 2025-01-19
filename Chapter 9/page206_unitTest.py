import myProgram as mp

def unitTest():
    firstNums = [1,2,3,4,5]
    secondNums = [1,1,4,-1,100]
    fails = 0
    for i in range(len(firstNums)):
    #[i] is the loop position value from the list
        test1 = firstNums[i]
        test2 = secondNums[i]
        testAns = mp.largerNumber(test1,test2)
        if test1 > test2:
            if test1 != testAns:
                fails +=1
        else:
            if test2 != testAns:
                fails +=1
                return fails
print("Total Fails: ", unitTest())
