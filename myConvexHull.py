def convexHull(pts): #recieves list of points
    if(len(pts)<2):
        return pts #needs at least two points
    pts.sort()
    a=pts[0]
    b=pts[len(pts)-1]
    left=[] #left of pivot ab
    right=[] #right of pivot ab
    for p in pts: #traverse all points and divide points
        area=getArea(a,b,p)
        if (area>0): 
            left.append(p)
        elif (area<0):
            right.append(p)
    
    #call recursion
    left=convexHullRec(left,a,b)
    right=convexHullRec(right,b,a)
    return left+right
    
    
def getArea(a,b,c): #gets area of triangle ABC
    #if positive, c is to the left of line ab, and right otherwise
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-a[0]*c[1]-b[0]*a[1]-c[0]*b[1]

    
def convexHullRec(pts,a,b): #recursive function (points, pivot left, pivot right)
    if (len(pts)==0): #meets base case, return right point only for sorting purposes
        return [b]
    
    #if not base case, divide and recurse
    #step 1: get furthest point
    maxArea=0
    pivot=[]
    for p in pts:
        area=getArea(a,b,p)
        if(area>maxArea):
            maxArea=area
            pivot=p
    
    #step 2: get left and right
    left=[]
    right=[]
    for p in pts:
        areaL=getArea(a,pivot,p)
        areaR=getArea(pivot,b,p)
        if (areaL>0.00001):
            left.append(p)
        elif (areaR>0.00001):
            right.append(p)
    
    #call recursion
    left=convexHullRec(left,a,pivot)
    right=convexHullRec(right,pivot,b)
    return left+right

'''
points = [[4.3, 3.0], [4.4, 2.9], [4.4, 3.0], [4.4, 3.2], [4.5, 2.3], [4.6, 3.1], [4.6, 3.2], [4.6, 3.4], [4.6, 3.6], [4.7, 3.2], [4.7, 3.2], [4.8, 3.0], [4.8, 3.0], [4.8, 3.1], [4.8, 3.4], [4.8, 3.4], [4.9, 3.0], [4.9, 3.1], [4.9, 3.1], [4.9, 3.6], [5.0, 3.0], [5.0, 3.2], [5.0, 3.3], [5.0, 3.4], [5.0, 3.4], [5.0, 3.5], [5.0, 3.5], [5.0, 3.6], [5.1, 3.3], [5.1, 3.4], [5.1, 3.5], [5.1, 3.5], [5.1, 3.7], [5.1, 3.8], [5.1, 3.8], [5.1, 3.8], [5.2, 3.4], [5.2, 3.5], [5.2, 4.1], [5.3, 3.7], [5.4, 3.4], [5.4, 3.4], [5.4, 3.7], [5.4, 3.9], [5.4, 3.9], [5.5, 3.5], [5.5, 4.2], [5.7, 3.8], [5.7, 4.4], [5.8, 4.0]]
[[4.9, 2.4], [5.0, 2.0], [5.0, 2.3], [5.1, 2.5], [5.2, 2.7], [5.4, 3.0], [5.5, 2.3], [5.5, 2.4], [5.5, 2.4], [5.5, 2.5], [5.5, 2.6], [5.6, 2.5], [5.6, 2.7], [5.6, 2.9], [5.6, 3.0], [5.6, 3.0], [5.7, 2.6], [5.7, 2.8], [5.7, 2.8], [5.7, 2.9], [5.7, 3.0], [5.8, 2.6], [5.8, 2.7], [5.8, 2.7], [5.9, 3.0], [5.9, 3.2], [6.0, 2.2], [6.0, 2.7], [6.0, 2.9], [6.0, 3.4], [6.1, 2.8], [6.1, 2.8], [6.1, 2.9], [6.1, 3.0], [6.2, 2.2], [6.2, 2.9], [6.3, 2.3], [6.3, 2.5], [6.3, 3.3], [6.4, 2.9], [6.4, 3.2], [6.5, 2.8], [6.6, 2.9], [6.6, 3.0], [6.7, 3.0], [6.7, 3.1], [6.7, 3.1], [6.8, 2.8], [6.9, 3.1], [7.0, 3.2]]
[[4.9, 2.5], [5.6, 2.8], [5.7, 2.5], [5.8, 2.7], [5.8, 2.7], [5.8, 2.8], [5.9, 3.0], [6.0, 2.2], [6.0, 3.0], [6.1, 2.6], [6.1, 3.0], [6.2, 2.8], [6.2, 3.4], [6.3, 2.5], [6.3, 2.7], [6.3, 2.8], [6.3, 2.9], [6.3, 3.3], [6.3, 3.4], [6.4, 2.7], [6.4, 2.8], [6.4, 2.8], [6.4, 3.1], [6.4, 3.2], [6.5, 3.0], [6.5, 3.0], [6.5, 3.0], [6.5, 3.2], [6.7, 2.5], [6.7, 3.0], [6.7, 3.1], [6.7, 3.3], [6.7, 3.3], [6.8, 3.0], [6.8, 3.2], [6.9, 3.1], [6.9, 3.1], [6.9, 3.2], [7.1, 3.0], [7.2, 3.0], [7.2, 3.2], [7.2, 3.6], [7.3, 2.9], [7.4, 2.8], [7.6, 3.0], [7.7, 2.6], [7.7, 2.8], [7.7, 3.0], [7.7, 3.8], [7.9, 3.8]]
print(convexHull(points))
'''