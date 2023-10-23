# def divide_by(a,b):
#      return a/b

# print(divide_by(40, 0))   

# solving execption error
def divide_by(a,b):
    return a/b
try:
    ans=divide_by(40, 0)  
except Exception as e:
    print("some thing went wrong", e)    