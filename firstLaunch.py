import mysql.connector
import os


login = False
while not login:
    print("Please log in:")
    Uname = input("Username: ")
    pwd = input("Password: ")
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user=Uname,
            password=pwd,
        )
    except:
        print("Incorrect username or password\n")
        print()
    else:
        mycursor = mydb.cursor()
        print()
        login = True

def ignore_DEV():
    mycursor.execute("CREATE DATABASE ChemicalDatabase")
    mycursor.execute("CREATE TABLE ElementTable (elementSymbol VARCHAR(255), name VARCHAR(255), atomicNumber VARCHAR(255), "
                     "atomicWeight VARCHAR(255), electronCount VARCHAR(255), "
                     "elementGroup VARCHAR(255), radioactive VARCHAR(255), magnetic VARCHAR(255), stateAtRoomTemp VARCHAR(255), "
                     "meltingPoint VARCHAR(255), boilingPoint VARCHAR(255))")
    mycursor.execute("CREATE TABLE moleculeTable (moleculeFormula VARCHAR(255), name VARCHAR(255), electronCount VARCHAR(255), "
                     "bondType VARCHAR(255), bondDiagram VARCHAR(255), "
                     "radioactive VARCHAR(255), magnetic VARCHAR(255), stateAtRoomTemp VARCHAR(255), meltingPoint VARCHAR(255), "
                     "boilingPoint VARCHAR(255))")
    mycursor.execute("CREATE TABLE IsotopeTable (baseElement VARCHAR(255), name VARCHAR(255), neutronCount VARCHAR(255), "
                     "isotopPercentage VARCHAR(255), atomicNumber VARCHAR(255), "
                     "radioactive VARCHAR(255), magnetic VARCHAR(255), stateAtRoomTemp VARCHAR(255), meltingPoint VARCHAR(255), "
                     "boilingPoint VARCHAR(255))")


mydb = mysql.connector.connect(
            host="localhost",
            user=Uname,
            password=pwd,
            database="ChemicalDatabase"
        )

mycursor=mydb.cursor()
mycursor.execute("TRUNCATE TABLE ElementTable")
mycursor.execute("TRUNCATE TABLE moleculeTable")
mycursor.execute("TRUNCATE TABLE IsotopeTable")
file = open("ElementTable.txt", "r")
read = file.readlines()
elementTable = []
for x in read:
    x = x.rstrip("|")
    elementTable.append(x.split("|"))
for x in elementTable:
    sql = "INSERT INTO ElementTable (elementSymbol, name, atomicNumber, atomicWeight, electronCount, " \
          "elementGroup, radioactive, magnetic, stateAtRoomTemp, meltingPoint, boilingPoint)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10])
    mycursor.execute(sql, val)
    mydb.commit()
file.close()
file = open("moleculeTable.txt", "r")
read = file.readlines()
elementTable = []
for x in read:
    x = x.rstrip("|")
    elementTable.append(x.split("|"))
for x in elementTable:
    sql = "INSERT INTO MoleculeTable (moleculeFormula, name, electronCount, bondType, bondDiagram, " \
          "radioactive, magnetic, stateAtRoomTemp, meltingPoint, boilingPoint)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9])
    mycursor.execute(sql, val)
    mydb.commit()
file.close()
file = open("IsotopeTable.txt", "r")
read = file.readlines()
elementTable = []
for x in read:
    x = x.rstrip("|")
    elementTable.append(x.split("|"))
for x in elementTable:
    sql = "INSERT INTO IsotopeTable (baseElement, name, neutronCount, isotopPercentage, atomicNumber, " \
          "radioactive, magnetic, stateAtRoomTemp, meltingPoint, boilingPoint)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9])
    mycursor.execute(sql, val)
    mydb.commit()
file.close()
os.system("open ~/ChemicalDatabase/LetTheBubblingCommence")
exit()
