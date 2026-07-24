sampleLst = list( map ( int , input ( " Enter the list : ").split()))
max = float('-inf')
smax = 0
for i in range (len(sampleLst)):
    if (max < sampleLst[i]):
        smax = max
        max = sampleLst[i]
    elif smax < sampleLst[i] and max != sampleLst[i]:
        smax = sampleLst[i]
print("The maximum value is ", max,
      "The second maximum value is ", smax)


    


