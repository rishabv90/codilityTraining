#Rishab Verma 
#16th Dec 2016

def binary_gap(N):
    num = bin(N)[2:]
    
    start = False
    max = 0
    gap = 0
    
    
    for digit in num:
        if num == '1':
            if gap > max:
                max = gap
                gap = 0
            start = True

        elif start:
            gap += 1
    return max
