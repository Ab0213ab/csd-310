
# Andrew Schaefer
# 6/28/21
# CSD-310
# Module 8.3

import mysql.connector
from mysql.connector import errorcode 

config = {
	"user": "pysports_user",
	"password": "weare138",
	"host": "127.0.0.1",
	"database": "pysports",
	"raise_on_warnings": True
}

db = mysql.connector.connect(**config)
mycursor = db.cursor()

mycursor.execute("SELECT team_id, team_name, mascot FROM team")
myresult2 = mycursor.fetchall()

print("\n--DISPLAYING TEAM RECORDS--")

for x in myresult2:
	print("Team ID: {}" .format(x[0]))
	print("Team Name: {}" .format(x[1]))
	print("Mascot: {}" .format(x[2]))

mycursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
myresult = mycursor.fetchall()

print("\n--DISPLAYING PLAYER RECORDS--")

for x in myresult:
	print("Player ID: {}" .format(x[0]))
	print("First Name: {}" .format(x[1]))
	print("Last Name: {}" .format(x[2]))
	print("Team ID: {}" .format(x[3]))

try:
	db = mysql.connector.connect(**config)

	input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print(" The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print(" The specified database does not exist")

	else:
		print(err)

finally:
	db.close()