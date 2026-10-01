#question 2  
print("for fahrenhiet to celsuis  enter  1  and for  celsius to fahrenheit enter  2")
conversion = int(input())
if(conversion==2):
    celsius = float(input("enter  the  temperatue  in celsius : "))
    fahrenheit= celsius*9/5  + 32 
    print("the fahrenhiet is : " , fahrenheit , "degree  F")

elif(conversion==1):
    fahrenheit = float(input("enter  the  temperatue  in  fahrenheit:  ")) 
    celsius  =  (fahrenheit - 32 )*5/9
    print("the  teemperature  in celsius is: "  , celsius , "degree  C" )
