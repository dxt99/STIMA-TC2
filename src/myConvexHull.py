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
        if (area>0.00001): 
            left.append(p)
        elif (area<-1*0.00001):
            right.append(p)
    
    #call recursion
    left=convexHullRec(left,a,b)
    right=convexHullRec(right,b,a)
    return left+right
    
    
def getArea(a,b,c): #gets area of triangle ABC
    #if positive, c is to the left of line ab, and right otherwise
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-a[0]*c[1]-b[0]*a[1]-c[0]*b[1]

    
def convexHullRec(pts,a,b): #recursive function (points, pivot left, pivot right)
    if (len(pts)==0): #meets base case, return right pivot only
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
