print("Find The Median!")
tot = input("Total number of numbers that you want to calculate (min-5, max-10) = ")
print("Enter the numbers in ascending (small to big) order")
num1 = input("The first number - ")
num2 = input("The second number - ")
num3 = input("The third number - ")
num4 = input("The fourth number - " )
num5 = input("The fifth number - ")
num6 = input("The sixth number (leave blank if not applicable) - ")
num7 = input("The seventh number (leave blank if not applicable) - ")
num8 = input("The eighth number (leave blank if not applicable) - ")
num9 = input("The ninth number (leave blank if not applicable) - ")
num10 = input("The tenth number (leave blank if not applicable) - ")
if num6 == '':
    print("The median is " + num3)
if num6 != '' and num7 == '':
    print("The median is/are " + num3 + ' and ' + num4)
if num7 != '' and num8 == '':
    print("The median is " + num4)
if num8 != '' and num9 == '':
    print("The median is/are " + num4 + ' and ' + num5)
if num9 != '' and num10 == '':
    print("The median is " + num5)
if num10 != '':
    print("The median is/are " + num5 + ' and ' + num6)