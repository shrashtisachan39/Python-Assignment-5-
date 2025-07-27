dicti={'mick':75,'nick':85,'john':90}
a=input("Enter the student's name:" )


if a in dicti :
    print(a,"'s marks:",dicti[a])
else:
     print("Student not found.")


