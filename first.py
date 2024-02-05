a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))
wow = [a, b, c]
max = max(wow)
min = min(wow)
if a > min and a < max:
    print (a)
elif b > min and b < max:
    print(b)
elif c > min and c < max:
    print(c)    

