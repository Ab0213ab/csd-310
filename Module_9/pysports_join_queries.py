
# Andrew Schaefer
# 7/6/21
# CSD-310
# Module 9.2

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


# Inner Join
sql = "SELECT player_id, first_name, last_name, team_name \
	FROM team \
	INNER JOIN player ON team.team_id = player.team_id"

mycursor.execute(sql)
myresult = mycursor.fetchall()

print("\n--DISPLAYING PLAYER RECORDS--")

for x in myresult:
	print("Player ID: {}" .format(x[0]))
	print("First Name: {}" .format(x[1]))
	print("Last Name: {}" .format(x[2]))
	print("Team Name: {}" .format(x[3]))


# Left Outer Join
sql2 = "SELECT player_id, first_name, last_name, team_name \
	FROM team \
	LEFT OUTER JOIN player ON team.team_id = player.team_id"

mycursor.execute(sql2)
myresult = mycursor.fetchall()

print("\n--DISPLAYING PLAYER RECORDS--")

for x in myresult:
	print("Player ID: {}" .format(x[0]))
	print("First Name: {}" .format(x[1]))
	print("Last Name: {}" .format(x[2]))
	print("Team Name: {}" .format(x[3]))


# Right Outer Join
sql3 = "SELECT player_id, first_name, last_name, team_name \
	FROM team \
	RIGHT OUTER JOIN player ON team.team_id = player.team_id"

mycursor.execute(sql3)
myresult = mycursor.fetchall()

print("\n--DISPLAYING PLAYER RECORDS--")

for x in myresult:
	print("Player ID: {}" .format(x[0]))
	print("First Name: {}" .format(x[1]))
	print("Last Name: {}" .format(x[2]))
	print("Team Name: {}" .format(x[3]))


# WHERE Clause Used
sql4 = "SELECT first_name, last_name \
	FROM player \
	WHERE player_id = 3"

mycursor.execute(sql4)
myresult = mycursor.fetchall()

print("\n--DISPLAYING PLAYER RECORDS--")

for x in myresult:
	print("First Name: {}" .format(x[0]))
	print("Last Name: {}" .format(x[1]))


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







