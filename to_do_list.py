print(f'To Do List !!!')
list=[]
list_name=input("Enter the List name: ")
list_no=int(input("Enter the total number of tasks for today : "))
for i in range(list_no):
    list_task=input(f'Enter the {i+1} task: ')
    final_list=list.append(list_task)
print(f'Final List: {final_list}')
