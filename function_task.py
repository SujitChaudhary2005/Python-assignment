def calcufunc():
    results = {}
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print('--------------------------')

    results['add'] = num1+num2
    results['sub'] = num1-num2
    results['mul'] = num1*num2
    results['div'] = num1/num2
    results['rem'] = num1%num2

    print("The data on dictionary: ",results.items()) #This line is just to show how data is saved in dictionary.

    print('--------------------------')

    for task, output in results.items(): #Used items() method because it return the list with all dictionary keys with values.
        print(f"The {task} of {num1} and {num2} is: {output}")
        
    print('--------------------------')

calcufunc()

"""
Here is how results dictionary might look like:

    results = {
        add: num1+num2,   # in this task is add and output is num+num2    key=add    value=num+num2 // item1
        sub: num1-num2,   # in this task is sub and output is num-num2    key=sub    value=num-num2 // item2
        mul: num1*num2,   # in this task is mul and output is num*num2    key=mul    value=num*num2 // item3
        div: num1/num2,   # in this task is div and output is num/num2    key=div    value=num/num2 // item4
        rem: num1%num2    # in this task is rem and output is num%num2    key=rem    value=num%num2 // item5
    }

    Therefore: task = key   output = value
"""