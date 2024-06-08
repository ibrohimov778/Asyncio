import asyncio

async def read_file(filename: str):
    with open (filename) as f:
        data: str = f.read()
        return data 



async def fetch_data(data:int) -> dict:
    if data == 0:
        raise  Exception("No data found...")
    return {"data": data}


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fetch_data(1))
            tg.create_task(fetch_data(2))
            tg.create_task(fetch_data(3))
            tg.create_task(fetch_data(4))
            tg.create_task(fetch_data(5))
            tg.create_task(fetch_data(6))
            tg.create_task(fetch_data(7))
            tg.create_task(fetch_data(8))
          
        print(task.result())
        print('Done!')
    except* FileNotFoundError as eg:
        for error in eg.exceptions:
            print(error)
            
    except* Exception as eg:
        print(eg.exceptions)        
            
        
async def main():
    tasks = asyncio.gather (
        fetch_data(1),
        fetch_data(2),
        read_file("image.png"),
        fetch_data(0),
        return_exceptions=True
    )

    results = await tasks
    print(results)
    print("Done!")
    
    
    
asyncio.run(main())
print("Done!")




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
    
    
    
def task_5():
    time.sleep(2)
    print("call 5")
    
    
def task_6():
    time.sleep(2)
    print("call 6")
    

        
def task_7():
    time.sleep(2)
    print("call 7")
    
    
    
def task_8():
    time.sleep(2)
    print("call 8")


   
def task():
    print(datetime.now())
    task()
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    print(datetime.now())


            
if __name__ == "__ main__":
    task()
