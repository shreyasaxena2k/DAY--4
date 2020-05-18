val=input('Input the tuple')
tuple= tuple(val.split(','))

def Count(tup, en):
    return tup.count(en)

x=(input('Enter the value to be found: '))
print(Count(tuple,x))