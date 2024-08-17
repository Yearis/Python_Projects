def fibonachi(n): 
    if(n==1):
        return 1               
    elif(n==0):
        return 0
    else:
        return fibonachi(n-1)+fibonachi(n-2)
    # f0 = 0
    # f1 = 1
    # f2 = f1 + f2
    # fn = f(n-1) + f(n-2)    
print(fibonachi(6))
# when i take 6 :
#  f6=f(6-1)+f(6-2)
#  f6=f(6-1)+f(6-2)