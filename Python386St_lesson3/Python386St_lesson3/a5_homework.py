
## First task (even or odd numbers)
## ---------------------------
#number = int(input("Enter number: "))

#if not number % 2:
#    print("This number {} is even.")
#else:
#    print("This number {} is odd")




## Second task (animal: car or dog)
## ---------------------------
#animal_talk = str(input("Enter how talk animal (Meow, Bark) : "))

#if animal_talk == 'Meow':
#    print("This animal is a 'Cat'")
#elif animal_talk == 'Bark':
#    print("This animal is a 'Dog'")
#else:
#    print("I don't know this animal.")




## Third task  (number -> positive, negative, zero)
## ---------------------------
enter_number = int(input('Enter integer number: '))
if enter_number > 0:
    print("This number '{}' is positive.".format(enter_number))
elif enter_number < 0:
    print("This number '{}' is negative.".format(enter_number))
else:
    print("This number '{}' is - zero".format(enter_number))
print("this is {}- digit number : {}".format(len(str(abs(enter_number))), enter_number))


