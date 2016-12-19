# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

#Rishab Verma
#16 Dec 2106

def solution(A):
    # write your code in Python 2.7
    
    times = {}#number of occurances.
    for num in A:
        if times.get(num):
            times[num] = times[num] + 1
        else:
            times[num] = 1
            
    for num in times:
        if times[num] % 2 <> 0: #haha i did'nt know the != sign in python :(
            return num
            
    pass
