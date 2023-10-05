def binary_mult(x,y):
    # Convert the binary to integer
    x_int = int(''.join(map(str,x)), 2)
    y_int = int(''.join(map(str,y)), 2)
    
    # Find the product
    product = x_int * y_int
    
    return product