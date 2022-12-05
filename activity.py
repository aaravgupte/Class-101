import time
def timer(seconds):
    while seconds>0:
        minutes=int(seconds/60)
        secs=int(seconds%60)
        countdown=f'{minutes} : {secs}'
        print(countdown,end='\r')
        time.sleep(1)
        seconds-=1
    print("Time Over")    

seconds=int(input("Enter the time in seconds"))
timer(seconds)    

