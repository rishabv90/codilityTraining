def solution(A, K):
    # write your code in Python 2.7
    if len(A) == K:
        return A
    
    if A == [] or A == [0]:
        return A

    K = -K % len(A)

    return(A[K:]+ A[:K])
    
    
