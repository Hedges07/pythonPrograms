task=input("Enter a task for your to-do list. Press <enter> when done: ")
lis=[]
while(task!=""):
    lis.append(task)
    task=input("Enter a task for your to-do list. Press <enter> when done: ")
if(len(lis)==0):
    print("Your list is empty")
else:
    print("Your To-Do List has",len(lis),"items.")
    print("-------------------------------------")
for i in sorted(lis):
    print(i[0].upper()+i[1:])