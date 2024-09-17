list_of_sports=['Cricket','Tennis','Football','Hockey']
def my_function():
    B=input("Do you want to proceed further: ")
    if B == 'Yes':
        for i in list_of_sports:
            print(i)
    else:
        print ('you dont want proceed further, Thank You!')
        
my_function()
    