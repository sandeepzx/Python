file = open("Fileprogram.txt",'w')
content = file.write("hi i am Tony")
file.close()

file = open("Fileprogram.txt",'r')
content = file.read()
print(content)
file.close()

file = open("Fileprogram.txt",'a')
content = file.write(" iam fine, Thanks")
file.close()
