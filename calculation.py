def get_addition(a,b):
    add= a + b
    print(f"addition of {a} and {b} is {add}")
    return add

def get_multiplication(x,y):

    """This is multiplication function"""
    multi = x * y
    #print(f"multiplication of {x} and {y} is {multi}")
    return multi


if __name__ == "__main__" :
    get_addition(10,20)
    print(get_multiplication.__doc__)