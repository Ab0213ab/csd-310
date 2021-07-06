
# Andrew Schaefer
# 7/6/21
# CSD-310
# Module 9.3

import mysql.connector
from mysql.connector import errorcode 

# Configures and connects to database
config = {
	"user": "pysports_user",
	"password": "weare138",
	"host": "127.0.0.1",
	"database": "pysports",
	"raise_on_warnings": True
}
db = mysql.connector.connect(**config)
mycursor = db.cursor()

# Insert new player record
mycursor.execute("""INSERT INTO player(first_name, last_name, team_id)
	VALUES('Elissa', 'Steamer', 1)""")


# Inner Join selection statement 
sql = "SELECT player_id, first_name, last_name, team_name \
	FROM team \
	INNER JOIN player ON team.team_id = player.team_id"

mycursor.execute(sql)
myresult = mycursor.fetchall()

# Display output heading
print("\n--DISPLAYING PLAYER RECORDS--")

# Display all records
for x in myresult:
	print("Player ID: {}" .format(x[0]))
	print("First Name: {}" .format(x[1]))
	print("Last Name: {}" .format(x[2]))
	print("Team Name: {}" .format(x[3]))


# Update record
sql2 = "UPDATE player SET team_id = 2 WHERE first_name = 'Elissa'"
mycursor.execute(sql2)


# Inner Join selection statement
sql3 = "SELECT player_id, first_name, last_name, team_name \
	FROM team \
	INNER JOIN player ON team.team_id = player.team_id"

mycursor.execute(sql3)
myresult2 = mycursor.fetchall()

# Display output heading
print("\n--DISPLAYING PLAYER RECORDS--")

# Display all records
for x in myresult2:
	print("Player ID: {}" .format(x[0]))
	print("First Name: {}" .format(x[1]))
	print("Last Name: {}" .format(x[2]))
	print("Team Name: {}" .format(x[3]))


# Delete record
sql4 = "DELETE FROM player WHERE first_name = 'Elissa'"
mycursor.execute(sql4)

# Inner Join selection statement
sql5 = "SELECT player_id, first_name, last_name, team_name \
	FROM team \
	INNER JOIN player ON team.team_id = player.team_id"

mycursor.execute(sql5)
myresult3 = mycursor.fetchall()

# Display output heading
print("\n--DISPLAYING PLAYER RECORDS--")

# Display all records
for x in myresult3:
	print("Player ID: {}" .format(x[0]))
	print("First Name: {}" .format(x[1]))
	print("Last Name: {}" .format(x[2]))
	print("Team Name: {}" .format(x[3]))

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







