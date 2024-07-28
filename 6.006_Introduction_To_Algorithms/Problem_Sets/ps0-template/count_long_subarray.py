def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    l=1
    cur=1
    count = 0
    n=len(A)
    for i in range(1,n):
        if A[i]>A[i-1]:
            l+=1
        
        else:
            if l>cur:
                cur=l
                count=1
            elif cur==l:
                count+=1
            l=1
        #print(l," ",cur," ",count)
    if l>cur:
        cur=l
        count=1
    elif cur==l:
        count+=1
    return count

if __name__ == '__main__':
    A=(2, 2, 4, 1, 4)
    print(count_long_subarray(A))