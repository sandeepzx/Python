
# pattern = "python"
# print(re.sub(pattern,"hello", "python harry python hi python world"))
   
import re

pattern = "[A-z][0-9][a-z]"
if re.search(pattern,"P8h"):
    print("matched")
else:
    print("not")
