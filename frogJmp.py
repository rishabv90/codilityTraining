# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

#Rishab Verma 
#19th Dec 2016

def solution(X, Y, D):
    # write your code in Python 2.7
    dist = Y-X 
    
    
    #one = dist/D
    #two = dist/D + 1
    #print(one)
    #print(two)
    
    if(dist % D == 0):
        return dist/D
        
    if (dist % D <> 0):
        return dist/D + 1
