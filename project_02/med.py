
# coding: utf-8

# In[1]:


##...yamoah min-edit-distance....##


# In[2]:


import numpy as np


# In[3]:


def main(source, target):
    distMatrix = min_edit_distance(source, target)
    distMatrix = initiate(distMatrix, len(source), len(target))
    med = recurrRelation(distMatrix,source,target)
    print(distMatrix)
    print(med)


# In[4]:


def min_edit_distance(source, target):
    n = len(source) + 1
    m = len(target) + 1
    print(source +" "+ str(n))
    print(target +" "+ str(m))
    myMatrix = np.zeros((n,m))
    #myMatrix = np.matrix(np.arange(n*m).reshape((n,m)))
    return myMatrix


# In[5]:


def initiate(distanceMatrix, n, m):
    #print(distanceMatrix)
    #distanceMatrix.shape
    for i in range(1,n+1):
        distanceMatrix[i,0] = distanceMatrix[i-1,0] + 1 #del-cost(source[i])
    for j in range(1,m+1):
        distanceMatrix[0,j] = distanceMatrix[0,j-1] + 1 #ins-cost(target[j])
    return distanceMatrix


# In[6]:


def recurrRelation(D, source, target):
    n = len(source)
    m = len(target)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(source[i-1]!=target[j-1]):
                D[i,j]=min((D[i-1,j]+1),#del-cost(source[i])
                           (D[i-1,j-1]+2),#sub-cost(source[i],target[j])
                           (D[i,j-1]+1))#ins-cost(target[j])
            else:
                D[i,j]=min((D[i-1,j]+1),#del-cost(source[i])
                           (D[i-1,j-1]),#sub-cost(source[i],target[j])
                           (D[i,j-1]+1))#ins-cost(target[j])
    return D[n,m]


# In[9]:


main("intention", "execution")


# In[ ]:


def doMatrix(n, m):
    aa = np.matrix(np.arange(n*m).reshape((n,m)))
    #print(aa.shape)
    print(aa)
#doMatrix(5,5)


# In[ ]:


#b = np.zeros((3,4))
#b.shape
#print(b)
#print("----------------")
#for i in range(1,3):
#    b[0,i] = i+10
#print(b)

