print("Hello, World!")

x = "Hello, World!"
print(x)

#This is a comment.

"""
multi
line
comment
"""

x,y,z = 'Hello', ',', 'World!'
print(x,y,z)

x = ', World!'
print('Hello' + x)

def myfunc():
    print('Hello' + x)

myfunc()


def myfunc2():
    global x
    x = 'awesome'

myfunc2()

print('Python is ' + x)

thislist = ['apple', 'banana', 'orange', 'pineapple']
for x in thislist:
    print(x)

thislist.append('cherry')
print(thislist)

if 'cherry' in thislist:
    print('ay, yo')

thislist.insert(3, 'mango')
print(thislist)