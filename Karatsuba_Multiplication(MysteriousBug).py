## BUG  (@Line 40) : I still don't understand why 10**(half*2) differs from 10**(n) and 10**(half) differs from 10**(n//2) given that half = n//2 .
## They should be mathematically identical but the program output tells me they are different


## Assumption : No. of digits of two numbers are SAME and POWER of 2
## Idea : Equally partition Fisrt and Second number to ab & cd 
## .... xy = 10^(n)(ac) + 10^(n/2)(ad + bc) + bd
## Lemma : ad + bc = (a + b)*(c + d) - ac - bd


import time

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
explanation_switch = 0

print(f"The length of digit is: {len(str(x))}")

def KaratsubaMultiply(x,y):

    ## Base Case
    if x < 10 or y < 10:
        return x * y

    ## Convergence
    else:
        n = max(len(str(x)), len(str(y)))
            
        a, b = divmod(x, 10**(n // 2))
        c, d = divmod(y, 10**(n // 2))

        if explanation_switch == True:
            print(f'Turn for {x} & {y}')
            print(f'In Detail : {x}*{y} = 10^({n})*({a}*{c}) + 10^({n}/2)*({a+b}*{c+d} - {a}*{c} - {b}*{d}) + {b}*{d} \n')

        ac = KaratsubaMultiply(a,c)
        bd = KaratsubaMultiply(b,d)
        ad_plus_bc = KaratsubaMultiply(a + b, c + d) - ac - bd

        ####################### BUG here ######################
        return (10**(n))*ac + (10**(n // 2))*(ad_plus_bc) + bd
        ####################### BUG end #######################


time_start = time.time()
sol_kara = KaratsubaMultiply(x,y)
time_end = time.time()
print('By Karatsuba:', sol_kara)
print(f"Execution time: {time_end - time_start} seconds")

print('')


time_start = time.time()
sol_conv = x*y
time_end = time.time()
print('By Conventional:', sol_conv)
print(f"Execution time: {time_end - time_start} seconds")


print(f"Are the results same?")
if sol_kara != sol_conv:
    print('false')
else:
    print('true')
