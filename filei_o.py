  
h = open("input.txt", "a+")
h.write("Hy there")
h.seek(0)
print(h.read())
#s = h.read(50) # read expects an argument as count -> which denotes the number of bytes to be counted
#print(s)
