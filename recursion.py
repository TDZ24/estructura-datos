numero = 5
num = 7

#def factorial (n:int):
#    res = 1
#
#    for i in range (1, n+1): 
#         res = res * i
#    return res
#
#print (factorial(numero))

def fact (j: int) -> int:
    if j == 1:
        return j
    return fact (j - 1) * j   

print (fact(num))

