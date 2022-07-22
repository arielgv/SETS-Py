newset= {1,3,6,101,"una string", 0.5, 3}
print(newset)
print(type(newset))   # Prints : Class 'set'
#print(newset.pop())
#print(newset)

setn2= {3, 3, 1, 22, 33, 44, "otra sring"}
print(setn2)
combination = newset | setn2
print("the union(combination) is with | that character ")
print(combination)

print("\nDifference: Takes two or more sets and deletes from set 1 every repeated item which can be found on set 2. The way for use it is with minus sign - ")
difference = newset - setn2
print(difference)
print("\n")



setofunion = newset & setn2
print("using & (intersection!) you can pick only the shared items and save to a new set, this is intersection : ")
print(setofunion)

listwith= newset ^ setn2
print("DIFERENCIA SIMETRICA. Symetric Difference.  using ^ you delete the repeated items between two or more sets \n")
print (listwith)




