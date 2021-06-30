#3. Get the doctors with no patients visit

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient_visited=0")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)