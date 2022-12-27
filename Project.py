contacts= {
"Syamanth": 9704770968,
"Jotham Roy": 7670892114,
"Hemanth":9502850367,
"Manikanta":9059101049,
"Sumanth":7981351497,
"Uday":9177971960,
"Vinay":9908491224,
"Yogindhra":8500710099,
"Harry":6305219267,
"Hemanth sai kumar":8340065854,
"Viswa vardhan":9121345262,
"Vardhan":9866003479,
"Karna Balaji":7736952669
}
def single_search():
	name=input(">>>Enter the name of the contact: ").upper()
	if name in contacts:
		print(f"\n{name}: {contacts[name]}")
	else:
	   b=input("\nNo such contact found\nIf you wish to add one, type 'Yes' else type 'No': ").lower()
	   if b=="yes":
	     new_contact(name)
	     print(f"{name}: {contacts[name]}")
	   elif b=="no":
	     	pass
	   else:
	     print("Enter either yes or no ")

def multiple_search():
	     result={}
	     s1=[]
	     s=0
	     name1=input("Enter the names of the contacts seperated by commas: ").split(",")
	     for i in name1:
	     			i=i.upper()
	     			if i in contacts:
	     				result[i]=contacts[i]
	     			else:
	     				s1.append(i)
	     				s+=1
	     if s>0:
	     	c=(input(f"\nCouldn't find contacts {s1} . \nDo you wish to add them? Enter Yes or No: ")).lower()
	     	if c=="yes":
	     		for i in s1:
	     			new_contact(i)
	     			if i in contacts:
	     				result[i]=contacts[i]
	     		print()
	     		print(result)
	     	elif c=="no":
	     		print()
	     		if result=={}:
	     			pass
	     	else:
	     		print("\n")
	     else:
	     	print()
	     	print(result)
	     		
def new_contact(contact_name):
	     print()
	     contact_number=int(input(">>>Enter their contact number: "))
	     contacts[contact_name]=contact_number
	     
choice=int(input("Would you like to: \n\n1. Search for a single contact \n2. List all the contacts \n3. Search for multiple contacts \n \nEnter your choice: "))

if choice==1:
	single_search()
	
elif choice==2:
	print()
	print(contacts)
	
elif choice==3:
	multiple_search()

else:
	print("Choose from the given options!")
