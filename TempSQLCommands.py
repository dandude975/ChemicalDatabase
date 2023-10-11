import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Dan",
    password="69420",
    database="ChemicalDatabase"
)

mycursor = mydb.cursor()


#print("Enter query")
#query = input()
def ignore():
    mycursor.execute("ALTER TABLE moleculeTable ADD bondDiagram VARCHAR(255) AFTER bondType")


    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
    mycursor.fetchall()
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='moleculeTable'")
    result = mycursor.fetchall()
    for x in result:
        print(x[0])

print("Exiting...")
mydb.close()
exit()

