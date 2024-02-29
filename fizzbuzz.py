for count in range(1, 31):
    if count % 15 == 0:
        print("fizz buzz")
    elif count % 3 == 0:
        print("fizz")
    elif count % 5 == 0:
        print("buzz")
    else:
        print(count)
    
# print out all numbers between 1-30
# if the number is a multiple of 3, print fizz
# if the number is a multiples of 5, print buzz
# if the number is a multiple of 15, print fizzbuzz
       