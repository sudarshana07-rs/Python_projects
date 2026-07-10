print(f'To Do List !!!')
list=[]
list_completed=[]
list_name=input("Enter the List name: ")
list_no=int(input("Enter the total number of tasks for today : "))
for i in range(list_no):
    list_task=input(f'Enter the {i+1} task: ')
    list.append(list_task)
# print(f'Final List: {list}')
print("Final List 🎯: ")
for i in list:
    print(i)
for i in range(list_no):
    completed_task=input("Enter the completed Task: ")
    if (completed_task in list):
        list.remove(completed_task)
        print('Upadated List: ')
        for i in list:
            print(i)

