# print out all multiples of 3 up to 100
for count in range(100):
    if count % 3 == 0:
        print(count)
    elif count % 5 == 0: # must use elif or else the same multiples will come up twice ex. 90
        print(count)
# using the same loop, print out multiples of 5 as well
    
