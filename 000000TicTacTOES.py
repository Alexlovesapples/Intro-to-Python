import shutil
import sys
columns = shutil.get_terminal_size().columns
def p():
	print("%s|%s|%s".center(columns) % (a,b,c))
	print("=====  ".center(columns))
	print("%s|%s|%s".center(columns) % (d,e,f))
	print("=====  ".center(columns))
	print("%s|%s|%s".center(columns) % (g,h,i))
def one():
	if a == "X" and b == "X" and c == "X" or d == "X" and e == "X" and f == "X" or g == "X" and h == "X" and i == "X" or a == "X" and e == "X" and i == "X" or c == "X" and e == "X" and g == "X" or a == "X" and d == "X" and g == "X" or b == "X" and e == "X" and h == "X" or c == "X" and f == "X" and i == "X":
		print("Player one has won!".center(columns))
		sys.exit()
	else: 
		pass
def two():
	if a == "O" and b == "O" and c == "O" or d == "O" and e == "O" and f == "O" or g == "O" and h == "O" and i == "O" or a == "O" and e == "O" and i == "O" or c == "O" and e == "O" and g == "O" or a == "O" and d == "O" and g == "O" or b == "O" and e == "O" and h == "O" or c == "O" and f == "O" and i == "O":
		print("Player two has won!".center(columns))
		sys.exit()
	else:
		pass
a = "1"
b = "2"
c = "3"
d = "4"
e = "5"
f = "6"
g = "7"
h = "8"
i = "9"
p()
playerone = input("Player one's turn: ")
if playerone == "1" and a == "1":
	a = "X"
	p()
elif playerone == "2" and b == "2":
	b = "X"
	p()
elif playerone == "3" and c == "3":
	c = "X"
	p()
elif playerone == "4" and d == "4":
	d = "X"
	p()
elif playerone == "5" and e == "5":
	e = "X"
	p()
elif playerone == "6" and f == "6":
	f = "X"
	p()
elif playerone == "7" and g == "7":
	g = "X"
	p()
elif playerone == "8" and h == "8":
	h = "X"
	p()
elif playerone == "9" and i == "9":
	i = "X"
	p()
else:
	print("God you are bad at games")
	sys.exit()
playertwo = input("Player two's turn: ")
if playertwo == "1" and a == "1":
	a = "O"
	p()
elif playertwo == "2" and b == "2":
	b = "O"
	p()
elif playertwo == "3" and c == "3":
	c = "O"
	p()
elif playertwo == "4" and d == "4":
	d = "O"
	p()
elif playertwo == "5" and e == "5":
	e = "O"
	p()
elif playertwo == "6" and f == "6":
	f = "O"
	p()
elif playertwo == "7" and g == "7":
	g = "O"
	p()
elif playertwo == "8" and h == "8":
	h = "O"
	p()
elif playertwo == "9" and i == "9":
	i = "O"
	p()
else:
	print("God you are bad at games")
	sys.exit()
playerone = input("Player one's turn: ")
if playerone == "1" and a == "1":
	a = "X"
	p()
elif playerone == "2" and b == "2":
	b = "X"
	p()
elif playerone == "3" and c == "3":
	c = "X"
	p()
elif playerone == "4" and d == "4":
	d = "X"
	p()
elif playerone == "5" and e == "5":
	e = "X"
	p()
elif playerone == "6" and f == "6":
	f = "X"
	p()
elif playerone == "7" and g == "7":
	g = "X"
	p()
elif playerone == "8" and h == "8":
	h = "X"
	p()
elif playerone == "9" and i == "9":
	i = "X"
	p()
else:
	print("God you are bad at games")
	sys.exit()
playertwo = input("Player two's turn: ")
if playertwo == "1" and a == "1":
	a = "O"
	p()
elif playertwo == "2" and b == "2":
	b = "O"
	p()
elif playertwo == "3" and c == "3":
	c = "O"
	p()
elif playertwo == "4" and d == "4":
	d = "O"
	p()
elif playertwo == "5" and e == "5":
	e = "O"
	p()
elif playertwo == "6" and f == "6":
	f = "O"
	p()
elif playertwo == "7" and g == "7":
	g = "O"
	p()
elif playertwo == "8" and h == "8":
	h = "O"
	p()
elif playertwo == "9" and i == "9":
	i = "O"
	p()
else:
	print("God you are bad at games")
	sys.exit()
playerone = input("Player one's turn: ")
if playerone == "1" and a == "1":
	a = "X"
	p()
	one()
elif playerone == "2" and b == "2":
	b = "X"
	p()
	one()
elif playerone == "3" and c == "3":
	c = "X"
	p()
	one()
elif playerone == "4" and d == "4":
	d = "X"
	p()
	one()
elif playerone == "5" and e == "5":
	e = "X"
	p()
	one()
elif playerone == "6" and f == "6":
	f = "X"
	p()
	one()
elif playerone == "7" and g == "7":
	g = "X"
	p()
	one()
elif playerone == "8" and h == "8":
	h = "X"
	p()
	one()
elif playerone == "9" and i == "9":
	i = "X"
	p()
	one()
else:
	print("God you are bad at games")
	sys.exit()
playertwo = input("Player two's turn: ")
if playertwo == "1" and a == "1":
	a = "O"
	p()
	two()
elif playertwo == "2" and b == "2":
	b = "O"
	p()
	two()
elif playertwo == "3" and c == "3":
	c = "O"
	p()
	two()
elif playertwo == "4" and d == "4":
	d = "O"
	p()
	two()
elif playertwo == "5" and e == "5":
	e = "O"
	p()
	i()
elif playertwo == "6" and f == "6":
	f = "O"
	p()
	two()
elif playertwo == "7" and g == "7":
	g = "O"
	p()
	two()
elif playertwo == "8" and h == "8":
	h = "O"
	p()
	two()
elif playertwo == "9" and i == "9":
	i = "O"
	p()
	two()
else:
	print("God you are bad at games")
	sys.exit()
playerone = input("Player one's turn: ")
if playerone == "1" and a == "1":
	a = "X"
	p()
	one()
elif playerone == "2" and b == "2":
	b = "X"
	p()
	one()
elif playerone == "3" and c == "3":
	c = "X"
	p()
	one()
elif playerone == "4" and d == "4":
	d = "X"
	p()
	one()
elif playerone == "5" and e == "5":
	e = "X"
	p()
	one()
elif playerone == "6" and f == "6":
	f = "X"
	p()
	one()
elif playerone == "7" and g == "7":
	g = "X"
	p()
	one()
elif playerone == "8" and h == "8":
	h = "X"
	p()
	one()
elif playerone == "9" and i == "9":
	i = "X"
	p()
	one()
else:
	print("God you are bad at games")
	sys.exit()
playertwo = input("Player two's turn: ")
if playertwo == "1" and a == "1":
	a = "O"
	p()
	two()
elif playertwo == "2" and b == "2":
	b = "O"
	p()
	two()
elif playertwo == "3" and c == "3":
	c = "O"
	p()
	two()
elif playertwo == "4" and d == "4":
	d = "O"
	p()
	two()
elif playertwo == "5" and e == "5":
	e = "O"
	p()
	i()
elif playertwo == "6" and f == "6":
	f = "O"
	p()
	two()
elif playertwo == "7" and g == "7":
	g = "O"
	p()
	two()
elif playertwo == "8" and h == "8":
	h = "O"
	p()
	two()
elif playertwo == "9" and i == "9":
	i = "O"
	p()
	two()
else:
	print("God you are bad at games")
	sys.exit()
playerone = input("Player one's turn: ")
if playerone == "1" and a == "1":
	a = "X"
	p()
	one()
elif playerone == "2" and b == "2":
	b = "X"
	p()
	one()
elif playerone == "3" and c == "3":
	c = "X"
	p()
	one()
elif playerone == "4" and d == "4":
	d = "X"
	p()
	one()
elif playerone == "5" and e == "5":
	e = "X"
	p()
	one()
elif playerone == "6" and f == "6":
	f = "X"
	p()
	one()
elif playerone == "7" and g == "7":
	g = "X"
	p()
	one()
elif playerone == "8" and h == "8":
	h = "X"
	p()
	one()
elif playerone == "9" and i == "9":
	i = "X"
	p()
	one()
else:
	print("God you are bad at games")
	sys.exit()



