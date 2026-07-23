count=0
with open("notes.txt","r") as file:
    for line in file:
        if "ERROR" in line:
            count+=1
print(count)