file = open("data.txt", "w")
file.write("Hello, this is Tara!")
file.close()


file = open("data.txt", "r")
print(file.read())
file.close()

