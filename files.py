import re
import requests
i=1
with open('images.md', 'r') as file :
  for line in file:
    i+= 1
    string = line
    firstDelPos=string.find("(") # get the position of [
    secondDelPos=string.find(")") # get the position of ]
    stringAfterReplace = string[firstDelPos+1:secondDelPos]
    print (stringAfterReplace + ',')
    response = requests.get(stringAfterReplace)

    file = open("img/"+str(i)+".png", "wb")
    file.write(response.content)
    file.close()

# Replace the target string
 # print the string after sub string between dels is replaced
