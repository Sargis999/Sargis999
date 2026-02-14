import time
def timer():
    while True:
        inp=input("Insert time to count down(h:m:s)")
        parts=inp.split(":")

        if len(parts) !=3:
            print("Wrong format!Insert time to count down (h:m:s) ")
            continue
        if not(parts[0].isdigit() and parts[1].isdigit()and parts[2].isdigit()):
            print("All parts shoud be numbers!")
            continue
        if int(parts[1])>=60 or int(parts[2])>=60:
            print("Minutes and seconds must be less than 60")
            continue
        else:
            break
        
    hours=int(parts[0])
    minutes=int(parts[1])
    seconds=int(parts[2])
    total_seconds=hours *3600 +minutes *60 +seconds
    while total_seconds>=0:
        hours =total_seconds//3600
        minutes=(total_seconds%3600)//60
        seconds=total_seconds%60
        print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
        time.sleep(1)
        total_seconds-=1


        print("Time is over")

timer()        


