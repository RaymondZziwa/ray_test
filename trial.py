result = int(input("Enter your score?"))
if result <= 39:
    print("F9")
elif result > 39 and result <= 45:
    print("P8")
elif result > 45 and result <= 49:
    print("P7")
elif result > 49 and result <= 55:
    print("C6")
elif result > 55 and result <= 59:
    print("C5")
elif result > 59 and result <= 69:
    print("C4")
elif result > 69 and result <= 75:
    print("C3")
elif result > 75 and result <= 79:
    print("D2")
else:
    print("D1")
         