def task ():
    task = [] #empty list 
    print("-----TO-DO-LIST-----")

Total_task = int(input("Enter how many task you want to add = "))

for i in range(1, Total_task + 1):
    task_name = input(f"Enter task{i} = ")
    task.append(task_name)

print(f"Today's task are\n{task}")

while True :
    operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5- exit/stop/"))

    if operation == 1:
         add = input("Enter task you want to add = ")
         task.append (add)
         print(f"Task {add}  has been successfully added... ")