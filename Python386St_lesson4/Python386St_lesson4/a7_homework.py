
### first task - ( Fobinachi numbers)
### ------------------

#counter = 0
#end_value = 20

#while counter < end_value:
#    if counter == 0:
#        val_fob_1 = 0
#        print(val_fob_1)
#    elif counter == 1:
#        val_fob_2 = 1
#        print(val_fob_2)    
#    else:

#        val_fob = val_fob_1 + val_fob_2
#        print(val_fob)
#        val_fob_1 = val_fob_2
#        val_fob_2 = val_fob

#    print(counter + 1)
#    counter += 1




### second task - "Hello world" (change "o"->"a", "l"->"e")
### ------------------
#string = "Hello world"
#print(string)
#print("----------")
#str_n = ''
#for i in string:
#    if i == 'o':
#        str_n += 'a'
#    elif i == 'l':        
#        str_n += 'e'
#    else:
#        str_n += i

#    #str_n += i
#    #print(i)
#    #print(type(i))
#print(str_n)




### third task - (change odd->"_", ever and "a"->"b")
### ------------------
#string = 'Ham is tasty'
#print(string)
#print("----------")
#str_n = ''
#cointer = 0
#for i in string:
#    cointer += 1
#    if cointer % 2 != 0:
#        str_n += "_"    
#    else:
#        if i == 'a':
#            str_n += 'b'
#        else:
#            str_n += i
#print(str_n)




## fourth task - (divide on 3)
## ------------------
#start_cointer = 0
#end_cointer = 101
#while start_cointer < end_cointer:
#    if start_cointer != 0:
#        if start_cointer % 3 == 0:
#            print(start_cointer)
#    start_cointer += 1





## fifth task - (continue and break)
## ------------------
start_cointer = -1
end_cointer = 101
while start_cointer < end_cointer:
    start_cointer += 1
    
    if start_cointer == 4:
        continue
    print(start_cointer)
    if start_cointer == 18:
        break
    