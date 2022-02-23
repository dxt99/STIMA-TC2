import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import myConvexHull as cv
from sklearn import datasets
data = datasets.load_iris()
#create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
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
    plt.plot(x, y, colors[i]) #plo
    plt.legend()
plt.show()