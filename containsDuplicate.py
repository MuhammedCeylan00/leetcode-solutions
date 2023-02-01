def containdDuplicate(myList):
    myList.sort()
    for i in range(0,len(myList)-1):
        if myList[i]==myList[i+1]:
            return True
    else:
        return False


print(containdDuplicate([1,2,3,4]))