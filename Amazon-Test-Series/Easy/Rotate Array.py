def rotateArr(A,D,N):
    #Your code here
    D = D%N
    rev(A,0,D-1)
    rev(A,D,N-1)
    rev(A,0,N-1)
    return A

def rev(A, start, end):
    while(start<end):
        A[start],A[end] = A[end], A[start]
        start += 1
        end -= 1
