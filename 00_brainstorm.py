import random
mylist = ["Food","School","Music","Sports","Memes"]
for x in range(1):
	randint = (random.randint(0,5))	
	print(mylist[randint])
	print("is your catagory!") 
nums = [1,2,3,4,5,6,7,8,9,10]
answerlist = []
i = 0
while i < 10:
	answerlist.append(input("{}. Give me an answer!: ".format(nums[i])))
	i += 1
print(answerlist[0].center(40))
print("")
print(answerlist[1].center(40))
print("")
print(answerlist[2].center(40))
print("")
print(answerlist[3].center(40))
print("")
print(answerlist[4].center(40))
print("")
print(answerlist[5].center(40))
print("")
print(answerlist[6].center(40))
print("")
print(answerlist[7].center(40))
print("")
print(answerlist[8].center(40))
print("")
print(answerlist[9].center(40))
print("")

