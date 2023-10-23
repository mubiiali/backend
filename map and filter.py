# # map function

# menu = [ "espresso" , "mocha" , "latte" , "cappuccino" , "cortado" , "americano"]
# def find_coffee(coffee):
#     if coffee[0] =='c':
#         return coffee

# map_coffee = map(find_coffee , menu)
# print(map_coffee)
# for x in map_coffee:
#     print (x )     


#     # filter function  


# menu = [ "espresso" , "mocha" , "latte" , "cappuccino" , "cortado" , "americano"]
# def find_coffee(coffee):
#     if coffee[0] =='c':
#         return coffee

# filter_coffee = filter(find_coffee , menu)
# print(filter_coffee)
# for x in filter_coffee:
#     print (x )  



    # map example
menu = [1 , 2 , 3 , 4 , 5]
def find_num(num):
    return num*4
map_num = map(find_num , menu)
print(map_num)
for x in map_num:
    print (x) 

     