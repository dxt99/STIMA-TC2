# # Tugas Kecil 2 Strategi Algoritma: Convex Hull
# ## 1. Convex Hull Data Iris
# ### Load Data Iris:

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import myConvexHull as cv
from sklearn import datasets
data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

# ### Plot Convex Hull data Iris (Sepal Length vs Width):

# In[2]:


plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Sepal Length vs Sepal Width')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    bucket = bucket.tolist() #convert to list
    hull = cv.convexHull(bucket)
    bucket = np.array(bucket) #convert back to np.array
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    x=[hull[len(hull)-1][0]] #get x coordinates
    y=[hull[len(hull)-1][1]] #get y coordinates
    for p in hull:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, colors[i]) #plot
    plt.legend()
plt.show()


# ### Plot Convex Hull Data Iris (Petal Length vs Width):

# In[3]:


plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Length vs Petal Width')
plt.xlabel(data.feature_names[2])
plt.ylabel(data.feature_names[3])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[2,3]].values
    bucket = bucket.tolist() #convert to list
    hull = cv.convexHull(bucket)
    bucket = np.array(bucket) #convert back to np.array
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    x=[hull[len(hull)-1][0]] #get x coordinates
    y=[hull[len(hull)-1][1]] #get y coordinates
    for p in hull:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, colors[i]) #plot
    plt.legend()
plt.show()


# ## 2. Convex Hull Data Wine
# ### Load Data Wine:

# In[4]:


data = datasets.load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)


# ### Plot Data Wine (Alchohol vs Flavanoids)

# In[5]:


plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Alchohol vs Flavanoids')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[6])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,6]].values
    bucket = bucket.tolist() #convert to list
    hull = cv.convexHull(bucket)
    bucket = np.array(bucket) #convert back to np.array
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    x=[hull[len(hull)-1][0]] #get x coordinates
    y=[hull[len(hull)-1][1]] #get y coordinates
    for p in hull:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, colors[i]) #plot
    plt.legend()
plt.show()


# ### Plot Data Wine (Ash vs Total Phenols)

# In[6]:


plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Ash vs Total Phenols')
plt.xlabel(data.feature_names[2])
plt.ylabel(data.feature_names[5])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[2,5]].values
    bucket = bucket.tolist() #convert to list
    hull = cv.convexHull(bucket)
    bucket = np.array(bucket) #convert back to np.array
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    x=[hull[len(hull)-1][0]] #get x coordinates
    y=[hull[len(hull)-1][1]] #get y coordinates
    for p in hull:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, colors[i]) #plot
    plt.legend()
plt.show()

