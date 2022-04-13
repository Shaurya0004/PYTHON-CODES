  
f1 = open('input.txt', 'a+')

print(f1.tell())
'''
f1.tell()-->> it basically tells us that what is the position of our cursor(in simple language)
f1.seek(x)-->> it basically shifts/transfers our cursor to xth position  
'''
f1.seek(0)
print(f1.read(5))
f1.write('Punjab engineering college')