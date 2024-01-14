import time
current_time=time.strftime("%H hrs : %M mins : %S secs")
print("Current time in India >> " , current_time)

hour=int(time.strftime("%H"))

name=input("enter ur name >>")
if(hour>=0 and hour<=12):
    print("Good Morning",name)
elif(hour>=12 and hour<16):
    print("Good Afternoon",name)
elif(hour>=16 and hour<18):
    print("Good Evening",name)
elif(hour>=18 and hour<=0):
    print("Good Night",name)
