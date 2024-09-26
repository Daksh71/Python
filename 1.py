# the condition statment will check if the statment is true or not 
#to check if user is eliddgebel to vote or not 
userage = int(input("enter your age"))
#note the default input return type is string 
if userage >18:
    print("your eligible to voting")
else:
    print("yore not elegible to vote")


    #usergender = input("enter your gender :")
    #if usergender  == 'male':
     #   print("you cannot in first chamber")
    #else usergender == 'female':
    #   print("you can sit in first chamber of metro")




    #if you are female above 18 you can apply for govenrment job and if you are male ablove 18 you can aplly in private job

usergender == input("enter your gender:   ")
userage == int(input(" enter your age :   "))
if usergender == 'female' and userage > 18:
    print("your are elegible for the governmentjob")
elif usergender == 'male' and userge > 18:
    print ("you are elegible for the private job ")
else :
    print("your are not applicable to apply anywhere")