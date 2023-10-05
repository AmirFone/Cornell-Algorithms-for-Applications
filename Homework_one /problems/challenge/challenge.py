import math


def reference_multiply(x, y):
    x_string = ''.join([str(bit) for bit in x])  
    y_string = ''.join([str(bit) for bit in y])  
    x_int = int(x_string, 2)  
    y_int = int(y_string, 2)  
    product = x_int * y_int  
    product_binary = bin(product)  
    product_list = [int(bit) for bit in product_binary[2:]] 
    return product_list



def karatsuba(x,y):
    def karatsuba_base_10(x, y):

        if x < 10 or y < 10:
            return x*y

        n = max(len(str(x)), len(str(y)))
        m = n//2

        a = x // 10**m
        b = x % 10**m
        c = y // 10**m
        d = y % 10**m

        z0 = karatsuba_base_10(a, c)
        z1 = karatsuba_base_10(a + b, c + d)
        z2 = karatsuba_base_10(b, d)

        return (z0 * 10**(2*m)) + ((z1 - z0 - z2) * 10**m) + z2
    x = int(''.join(map(str,x)), 2) 
    y = int(''.join(map(str,y)), 2)
    product = karatsuba_base_10(x, y)

    return [int(d) for d in bin(product)[2:]] 


def fft(x, y):
    pass
