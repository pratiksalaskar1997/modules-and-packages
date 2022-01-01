'''# WAP to add the values
x = 'python'

def add(a, b):

    print('addition: ',a+b)

def bank_info(a,b,c):
    return  a+b+c

bank_info(2,3,4)

s = input('enter the string: ')
print(s[0])
print(s[-1])
print(s[len(s)//2])
print(len(s))

s = input('Enter the string: ')
print('length of the string is:',len(s))
e = input('Enter the word to search: ')
if s.find('e')== -1:
    print('Entered word is not present....')
else:
    print('indexing of',e,'is',s.find(e))

bal = [10000, 12000, 14000, 20000]
ten = map(lambda x : x * 0.1, bal)
print([sum(i) for i in zip(ten, bal)])

s1 = [10, 20, 30, 40]
for i in s1:
    print(i/2)

s = 'today its very cold'
x = input('Enter the word to search:')
if s.count(x) >= 1:
    print(' present')
else:
from loan import home_loan
from loan.home_loan import hm
from loan.vehical_loan import vl
from loan.gold_loan import gl

# expected o/p -- a4k3b2
s = 'a'
i = 0

print(chr(97),chr(97+4),chr(107),chr(107+3),chr(98),chr(100),sep='')

#expected = 'a12b6c634'
s = 'a12b6c634'
if s == 'isalpha':
    print('')



def splitString(str):
    alpha = ""
    num = ""
    for i in range(len(str)):
        if (str[i].isdigit()):
            num = num + str[i]
        else:
            ((str[i] >= 'A' and str[i] <= 'Z') or
              (str[i] >= 'a' and str[i] <= 'z')):
                  alpha += str[i]

    print(alpha)
    print(num)

    str = 'a12b6c634'
    splitString(str)


s = 'python'
l = 'Java'
for i in range(7):

    res = s[i]+l[i]+s[]
    print(res+a,end='')


#d = {1:2, 3:4, 5:6}
e = { 7 : 8, 9 : 10, 11:12}
for i in e.items():
    print(list(i))

print({i:i**2 for i in range(1, 16)})


# WAP to print maximum number of occurence of pair:
d = [{1:2, 3:4}, {10:20,30:40,50:60}, {100:1,200:2,300:3,400:4}]
l = []
k = []
for i in d:
    l.append(len(i))
print(max(l))
if max(l) == len(i):
    print(i)
'''











