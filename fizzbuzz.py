numbers = [5, 6, 7, 8, 9]
list1 = [1,2,3,4]


def fizzbuzz(numbers, list1):    

    lists = numbers + list1
    if len(lists) % 3 == 0 and len(lists) % 5 == 0:
        return("fizzbuzz")
    elif len(lists) % 3 == 0:
        return "fizz"
    elif len(lists) % 5 == 0:
        return "buzz"
    else:
        return (len(lists))
    print(fizzbuzz(['5', '6', '7', '8', '9'], ['1', '2', '3', '4']))
