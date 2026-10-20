sec  = int(input("enter  the  seconds: "))
hour = sec//3600
minute =(sec%3600)//60 
sec = (sec%3600)%60

print(f" {hour} hour {minute} minutes and {sec} second"  )


