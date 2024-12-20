
# args and kwargs i python
'''In Python, *args and **kwargs are used in function definitions to allow for variable numbers of arguments. Here's a breakdown of each:
*args
*args allows a function to accept any number of positional arguments.
The arguments are passed as a tuple.
Example:'''

# code
def example_of_args(pos1,pos2,*args):
    print(pos1,pos2)    #output 1,2
    print(args)    # output (3, 4, 4) ==> this shows that here it is pass as a tuple
    # or i can print is as in for loop
    for arg in args:
        print(arg)


example_of_args(1,2,3,4,4)


# **kwargs
'''**kwargs allows a function to accept any number of keyword arguments.
The arguments are passed as a dictionary.'''
# a = 1,b = 2, this two values should be explicitely set 

def kwarg_exmple(key_value1 = None, key_value2 = None,**kwargs):
    print(key_value1)
    print(key_value2)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwarg_exmple(a = 1,b = 2, c= 5, d = 6, f= 10)
print("\n\n\n")

def kwarg_exmple(key_value1 = None, key_value2 = None,**kwargs):
    print(key_value1)
    print(key_value2)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwarg_exmple(key_value1 = 999, key_value2 = 222, c= 5, d = 6, f= 10)        # here i set the parameters explicitely
