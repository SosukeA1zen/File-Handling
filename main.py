file=open("abc.txt","r")
print(file.read())

file=open("abc.txt","w")
file.write("I am 16yrs old.")

file=open("abc.txt","a")
file.write("My name is Samuel")

file=open("xyz.txt","w")
file.write("My name is Samuel")

file.close()