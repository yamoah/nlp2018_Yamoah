
# coding: utf-8

# In[ ]:


##....................This is Empty...............................##


# In[4]:


#...........Completed..............#
#yamoah naive_bayes
#!/usr/bin/python
import sys

def readDataSet(dataname,filename):
    classZero = [""] #set of elements in class zero
    classOne = [""] #set of elements in class one
    setClassZero =() # unique set of elements in class zero
    setClassOne = () # unique set of elements in class one
    noClass = [""] #unclassified
    BagOfWords = [""]
    #----------------------------------------#

    countZero=countOne=countLess=0
    classZeroCount = classOneCount = classlessCount = 0
    numLines = 0
    for d in dataname:
        myFile = open(d,"r")
        line = myFile.readline()
        while ((line!="") & (numLines<3000)):
            lineSplit = line.split()
            lineLength = len(lineSplit)
            rClass = lineSplit[lineLength-1] #the class (0 or 1)
            lineSplit.pop(lineLength-1)
            if(rClass=="0"):
                classZero.extend(lineSplit)
                classZeroCount = classZeroCount + len(lineSplit)
                countZero = countZero + 1
            elif(rClass=="1"):
                classOne.extend(lineSplit)
                classOneCount = classOneCount + len(lineSplit)
                countOne = countOne + 1
            else:
                noClass.extend(lineSplit)
                noClass.append(rClass)
                classlessCount = classlessCount + len(lineSplit) + 1
                countLess = countLess + 1
            numLines = numLines + 1
            line = myFile.readline()

    #At this point we have our bag of words and the counts
    #But the words may not be unique, so I will use sets
    #print(numLines)
    #print(countLess)
    #......prior prob..........#
    priorZero = countZero/(countZero+countOne)
    priorOne = countOne/(countZero+countOne)

    setClassZero = set(classZero)
    setClassOne = set(classOne)
    countSetZero = -1
    countSetOne = -1
    for a in setClassZero:
        countSetZero = countSetZero + 1
    for b in setClassOne:
        countSetOne = countSetOne + 1

    #.......calculate likelihood.....#

    myFilee = open(filename,"r")
    linee = myFilee.readline()
    outFile = open("results_file.txt","w")
    while (linee!=""):
        probClassZero = 1
        probClassOne = 1
        lineSplitt = linee.split()
        for m in lineSplitt:
            a = classZero.count(m)
            aa = a + 1
            probClassZero = probClassZero * (aa/(classZeroCount+countSetZero+countSetOne))
            b = classOne.count(m)
            bb = b + 1
            probClassOne = probClassOne * (bb/(classOneCount+countSetZero+countSetOne))
        if probClassZero > probClassOne:
            outFile.write("0\n")
        elif probClassZero < probClassOne:
            outFile.write("1\n")
        else:
            outFile.write("uncertain\n")
        linee = myFilee.readline()
    outFile.close()
    
try:
    #print(sys.argv[1])
    myFile = sys.argv[1]
    myDataSet = ["amazon.txt","imdb.txt","yelp.txt"]
    readDataSet(myDataSet,myFile)
except:
    print("Big Error")
    
    

