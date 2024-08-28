"""s=int(input("数学成绩："))
if s<70:
    print("damn")
elif 70<=s<90:
    print("fighting")
else :
    print("shit") 

fruits=['apple','banana','orange']
for a in fruits:
    print(a)  
    
for i in range(1,1000):
    print(i)     
【类】   
class Ball( ):
    def __init__(self,n,s,c):
        self.name=n
        self.size=s
        self.color=c  
    def play(self):
         print('打'+self.name) 
b1=Ball('篮球','大','紫色') 
b2=Ball('排球','小','白色')
print(b2.color+b1.size+b1.name)
b1.play()             """ 
 
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) 