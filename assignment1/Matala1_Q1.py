#present: Halel Stern
#Id: 212122147

def my_func(x1,x2,x3):
    y1 = x1+x2+x3
    y2 = x2+x3
    numerator = y1*y2*x3
    denominator = y1
    if denominator == 0:
        print("Not a number – denominator equals zero")
    elif type(x1) == int or type(x2) == int or type(x3) == int:
        print("Error: parameters should be float")
    elif type(x1) != float or type(x2) != float or type(x3) != float:
        print("None")
    else:
        ans = numerator / denominator
        print (ans)

my_func(1.0,2.0,3.0)