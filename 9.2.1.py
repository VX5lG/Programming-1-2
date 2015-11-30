# Axel
# Period 4
# 11/23/2015

# 9.2.1

# this will get a name and grade lvel, and print out greeting

name = input("What is yor name? ")
grade = int(input("What grade are you in? "))

if grade == 9:
    print ("Hi %s, welcome to your first year of high school." %(name))
elif grade == 10:
    print ("I hope to see you around %s." %(name))
elif grade == 11:
           print ("You need one more year to go %s." %(name))
elif grade == 12:
           print ("You are soon to graduate, congrats %s." %(name))
else:
           print ("Sorry, invalid grade.")
           
