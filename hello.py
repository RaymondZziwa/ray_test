 
yob = int(input("Enter your year of birth?"))
current_year = 2019
age = current_year - yob         
if age < 0:
    print("You donot exist")   
elif < 18:
    print("You are a minor")
elif 18 <= age < 37:
    print(" you are a youth")    
else:
    print("you are an elder")
