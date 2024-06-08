import time
from datetime import datetime


def task_1():
    time.sleep(2)
    print("call 1")
    
    
def task_2():
    time.sleep(2)
    print("call 2")

        
def task_3():
    time.sleep(2)
    print("call 3")
    

        
def task_4():
    time.sleep(2)
    print("call 4")
    
   
   
def task():
    print(datetime.now())
    task_1()
    task_2()
    task_3()
    task_4()
    print(datetime.now())

 
            
if __name__ == "__ main__":
    task()