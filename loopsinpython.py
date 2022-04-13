# let's learn about while loops

i = 1

while i < 10:
	print("value of i is ", i)
	i = i + 1
print("ending loop")

# let's do something avenger style

enemy = 1

while enemy < 100:
	print("Avengers are fighting")
	if enemy == 30:
		print("We love iron man 3000 <3")
	enemy = enemy + 1



	#let us try a question on loops and conditions 


a = int(input("Give input of first angle ")) # giving user a prompt during input
b = int(input("Give input of second angle "))
c = int(input("Give input of third angle "))
# now in the above lines we wrote "give input of first angle" this is same as if we write print("give input of the first angle")
if a > 0 and b > 0 and c > 0:
	if a + b + c == 180:
		print("Yes they are angles of a triangle")
	else:
		print("No they are not angles of triangle")
else:
	print("If the angles are not greater than zero then it is degenerate")