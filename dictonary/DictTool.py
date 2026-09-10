# nested  for  example  
student={
    "name": "adarsh" ,
    "subjects":{
        "math": ["algebra" , "geometry" , "trigonometry"] ,
        "physics": ["mechanics" , "optics" , "thermodynamics"] ,
        "data structure": ["array" , "linked list" , "stack" , "queue" , "tree" , "graph"] ,
    }
}
print(student)
print()
print(student["subjects"])   # for  accessing the  keyword of key  
print(student.get("subject"))   # same but  at  any  type  eeror  output  is  none  
print(student["subjects"]["math"])

# using  updaate  tool for  inserting  new  value or  changing  \
student.update({"city":"spain" , "name": "AADARSH JAISWAL"})
print(student)
print(student["name"])