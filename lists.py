#Lists in python
names = ['bob', 'john', 'doe', 'sarah','mary']
#if you print names you will get the same whole list you prepared
print(names)
#but if you print the index of the list you will get the specific name of the index which you desired for example i want the name of index [2] in the list
print(names[2])
#if you want to print the negative index of the list it will print the values from the end of the list for rxample i want last name from list you can either use "print(names[4]) or you can use this command
print(names[-1])
# if you want from a set of index you can use these commands
print(names[2:]) #prints from indexes of 2 till the end of list
print(names[2:5]) #prints from index of 2 till the index of 4 excluding the last index mentioned

# print the largest number from the list
numbers = [2,3,6,4,8,12,11]
max =0
for i in numbers:
  if i>max:
      max = i
print(max)
