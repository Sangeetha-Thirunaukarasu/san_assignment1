#new question
# find the given email is valid or not
#@ should be present, @ & . shold not be repeated, atleat 4 charactres b/w @ and . 
#should be atleast 3 characters before @ , end of mail id shold be .com 
# print yes if it is vaid otherwise no

import re
email = input()

pattern = '[a-zA-Z0-9&#*]{3}@[a-zA-Z]{4}.com'

op = re.findall(pattern,email)

if op:
    print("yes")
else:
    print("no")


    


