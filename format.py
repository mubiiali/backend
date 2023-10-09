#STRING FORMATTING

# name=input("enter the name : ")
# number=len(name)*3
# print("hello {} , your lucky number is {}".format(name,number))
# print("hello {name} , your lucky number is {numb}".format(name=(name),numb=len(name)*3))

#formatting2

price=7.5
with_tax=price*1.09
print(price,with_tax)
print("base price:${:.2f}. with tax:${:>2f}".format(price, with_tax))


# formating3

def to_celsius(x):
    return(x-32)*5/9



