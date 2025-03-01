#Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

import time
hour = int(time.strftime("%H"))
if(hour >= 0 and hour <12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<18):
    print("Good Afternoon Sir!")
elif(hour>=18 and hour<21):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")