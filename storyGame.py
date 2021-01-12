beginning ="You are at 1045 west cornelia avanue apartment 303.do you want to:\n" \
           "1.feed hank?\n" \
           "2.walk hank?\n" \
           "3.pet hank?"
print (beginning)
answer1=input("enter 1 2 or 3")
if answer1=="1":
    print("You fed hank to much food. he needs to barf. you will be paralyzed by it. be ready")
if answer1=="2":
    print("You walked hank. but you didnt let him sniff. he is mad at you. you will now be eaten by hank. be ready")
if answer1=="3":
    print("You pet hank for hours. he is happy. you just made a friend for life. he has your trust and you have his trust. you will be crime fighting partners")
if answer1=="1"or answer1=="2":
    print ("you lost. why did you do that. you have been convicted of hank abuse. thats just sad")
if answer1=="3":
    print("hank loves you <3. YOU WIN !!!!")