def skip_elements(elements):
    newlist=[]
    j=0
    for j in elements:
        if int(j)%2==0:
            newlist.append(j)
            j +=1
        return newlist

print(skip_elements("a","b","c","d","e","f","g"))
print(skip_elements(['orange','pineapple','strawberry','kiwi','peach']))
print(skip_elements([]))


