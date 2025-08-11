def length(a):
    counter = 0
    for _ in a:
        counter+=1
    return counter

print(length('salam'))


def max3(*args):
    m = float('-inf')
    for i in args:
        if i > m:
            m = i
    print('max is:',m)
    
max3(1,200,40,1000,-10)


def sum1(it):
    summ = 0
    for i in it:
        summ+=i
    print('sum is:',summ)
   
sum1([1,2,3,4])


def squre():
    a = int(input('enter your number:'))
    b = 1
    while 2*b<a:
        if b*b==a:
            print('Its squre')
            break
        else:
            b+=1
    else:
        print('not squre!')
    
    
squre()


def off():
    off = int(input('enter the percent of the off:'))
    price = int(input('enter the price:'))
    real_price=price-((price*off)/100)
    print('real price is:',real_price)
    
#off()

import string
def find_kind():
    a = input('enter something:')
    b = string.ascii_lowercase
    c = string.ascii_uppercase
    n = '0123456789'
    s = '~!@#$%^&*()?'
    if a in b:
        print('its lowercase!')
    elif a in c:
        print('uppercase!')
    elif a in n:
        print('its a number')
    elif a in s:
        print('its symbol')
    else:
        print('you did wrong!')

find_kind()
