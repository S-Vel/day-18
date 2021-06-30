#2. Get the doctor(s) who have more than 5 patients visited

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient_visited >5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)