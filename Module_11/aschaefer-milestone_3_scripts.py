
# Andrew Schaefer, Jennifer Thomas, Milo Blake, Shane Fox, Caleb Mastromonaco
# 7/13/21
# CSD-310
# Module 11.1
# Delta Group
# Milestone 3

import mysql.connector
from mysql.connector import errorcode 

# Configures and connects to database
config = {
	"user": "bacchus_user",
	"password": "weare138",
	"host": "127.0.0.1",
	"database": "bacchus",
	"raise_on_warnings": True
}

db = mysql.connector.connect(**config)
mycursor = db.cursor()


# DISPLAYING INNER JOIN DELIVERIES/SUPPLIER (report 1)
sql = "SELECT d.supplier_id, d.jan, d.feb, d.mar, d.apr, d.may, d.jun, d.jul, d.aug, d.sep, d.oct, d.nov, d.decem, s.supplier_name \
   FROM deliveries as d, supplier as s WHERE s.supplier_id = d.supplier_id"

mycursor.execute(sql)
myresult1 = mycursor.fetchall()

print("\n--DISPLAYING REPORT 1--")

for x in myresult1:
   print("Supplier ID: {}" .format(x[0]))
   print("January: {}" .format(x[1]))
   print("February: {}" .format(x[2]))
   print("March: {}" .format(x[3]))
   print("April: {}" .format(x[4]))
   print("May: {}" .format(x[5]))
   print("June: {}" .format(x[6]))
   print("July: {}" .format(x[7]))
   print("August: {}" .format(x[8]))
   print("September: {}" .format(x[9]))
   print("October: {}" .format(x[10]))
   print("November: {}" .format(x[11]))
   print("December: {}" .format(x[12]))
   print("Supplier Name: {}" .format(x[13]))


# DISPLAYING INNER JOIN WINE/DISTRIBUTOR (report 2)
sql2 = "SELECT w.wine_id, w.wine_name, w.bottles_sold, w.distributor_id, d.distributor_name \
   FROM wine as w, distributor as d WHERE d.distributor_id = w.distributor_id"

mycursor.execute(sql2)
myresult2 = mycursor.fetchall()

print("\n--DISPLAYING REPORT 2--")
for x in myresult2:
   print("Wine ID: {}" .format(x[0]))
   print("Wine Name/Type: {}" .format(x[1]))
   print("Bottles Sold: {}" .format(x[2]))
   print("Distributor ID: {}" .format(x[3]))
   print("Distributor Name: {}" .format(x[4]))


# DISPLAYING EMPLOYEES RECORDS (report 3)
mycursor.execute("SELECT employee_id, employee_name, q_1, q_2, q_3, q_4 FROM employees")
result3 = mycursor.fetchall()

print("\n--DISPLAYING REPORT 3--")
for x in result3:
	print("Employee ID: {}" .format(x[0]))
	print("Employee Name: {}" .format(x[1]))
	print("Quarter 1 Hours: {}" .format(x[2]))
	print("Quarter 2 Hours: {}" .format(x[3]))
	print("Quarter 3 Hours: {}" .format(x[4]))
	print("Quarter 4 Hours: {}" .format(x[5]))
