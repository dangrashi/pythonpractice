#Dictionary methods 
student={
    "name":"rashi",
    "subjects":{
        "eco":"88",
        "acc":"90",
        "bst":"84"
    }
}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"city":"delhi"})
print(student)