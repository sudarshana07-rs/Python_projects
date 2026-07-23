text=input("Enter a sentence: ")
with open("server.log","w") as file:
    file.write(text)
print ("Successfull")    