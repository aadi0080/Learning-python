sec = int(input("enter  the time  is  second : "))
hour = sec//3600 
Min  = (sec%3600)//60
sec =  (sec%3600)%60

print(hour , "hour " , Min , "minutes" , sec , "second")