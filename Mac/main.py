import mysql.connector
from tabulate import tabulate
import maskpass


class Element:
    def __init__(self):
        self.chemicalSymbol = input("Element symbol: ")
        self.name = input("Element name: ")
        self.atomicNumber = input("Atomic number: ")
        self.atomicWeight = input("Atomic weight: ")
        self.electronNumber = input("Electron count: ")
        self.group = input("Element group: ")
        radioactive = None
        while radioactive != 'y' and radioactive != 'n':
            radioactive = input("Radioactive? y/n: ")
            self.radioactive = radioactive
        magnetic = None
        while magnetic != 'y' and magnetic != 'n':
            magnetic = input("Magnetic? y/n: ")
            self.magnetic = magnetic
        stateAtRoomTemp = None
        while stateAtRoomTemp != 's' and stateAtRoomTemp != 'l' and stateAtRoomTemp != 'g':
            stateAtRoomTemp = input("State at room temperature s/l/g: ")
            self.stateAtRoomTemp = stateAtRoomTemp
        self.meltingPoint = input("Element melting point: ")
        self.boilingPoint = input("Element boiling point: ")
        print()

    def inputValues(self):
        sql = "INSERT INTO ElementTable (elementSymbol, name, atomicNumber, atomicWeight, electronCount, " \
              "elementGroup, radioactive, magnetic, stateAtRoomTemp, meltingPoint, boilingPoint)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.chemicalSymbol, self.name, self.atomicNumber, self.atomicWeight, self.electronNumber
               , self.group, self.radioactive, self.magnetic, self.stateAtRoomTemp, self.meltingPoint, self.boilingPoint)
        mycursor.execute(sql, val)
        mydb.commit()

    def printValues(self):
        print("Element symbol:", self.chemicalSymbol)
        print("Element name:", self.name)
        print("Atomic number:", self.atomicNumber)
        print("Atomic weight:", self.atomicWeight)
        print("Amount of electrons:", self.electronNumber)
        print("Element group", self.group)
        print("Radioactive: ", self.radioactive)
        print("Magnetic:", self.magnetic)
        print("State at room temperature:", self.stateAtRoomTemp)
        print("Melting point:", self.meltingPoint)
        print("Boiling point:", self.boilingPoint)
        print()


class Molecule:
    def __init__(self):
        self.chemicalFormula = input("Molecule formula: ")
        self.name = input("Molecule name: ")
        self.electronNumber = input("Electron count: ")
        self.bondType = input("Bond type: ")
        self.bondDiagram = input("Bond diagram: ")
        radioactive = None
        while radioactive != 'y' and radioactive != 'n':
            radioactive = input("Radioactive? y/n: ")
            self.radioactive = radioactive
        magnetic = None
        while magnetic != 'y' and magnetic != 'n':
            magnetic = input("Magnetic? y/n: ")
            self.magnetic = magnetic
        stateAtRoomTemp = None
        while stateAtRoomTemp != 's' and stateAtRoomTemp != 'l' and stateAtRoomTemp != 'g':
            stateAtRoomTemp = input("State at room temperature s/l/g: ")
            self.stateAtRoomTemp = stateAtRoomTemp
        self.meltingPoint = input("Molecule melting point: ")
        self.boilingPoint = input("Molecule boiling point: ")
        print()

    def inputValues(self):
        sql = "INSERT INTO MoleculeTable (moleculeFormula, name, electronCount, bondType, bondDiagram, " \
              "radioactive, magnetic, stateAtRoomTemp, meltingPoint, boilingPoint)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.chemicalFormula, self.name, self.electronNumber, self.bondType, self.bondDiagram
               , self.radioactive, self.magnetic, self.stateAtRoomTemp, self.meltingPoint, self.boilingPoint)
        mycursor.execute(sql, val)
        mydb.commit()

    def printValues(self):
        print("Molecule formula:", self.chemicalFormula)
        print("Molecule name:", self.name)
        print("Amount of electrons:", self.electronNumber)
        print("Bond type: ", self.bondType)
        print("Bond diagram: ", self.bondDiagram)
        print("Radioactive: ", self.radioactive)
        print("Magnetic:", self.magnetic)
        print("State at room temperature:", self.stateAtRoomTemp)
        print("Melting point:", self.meltingPoint)
        print("Boiling point:", self.boilingPoint)
        print()


class Isotope:
    def __init__(self):
        self.baseElement = input("Isotope of: ")
        self.name = input("Isotope name: ")
        self.neutronNumber = input("Neutron count: ")
        self.atomicNumber = input("Atomic Number: ")
        self.isotopePercentage = input("Percentage of existence: ")
        radioactive = None
        while radioactive != 'y' and radioactive != 'n':
            radioactive = input("Radioactive? y/n: ")
            self.radioactive = radioactive
        magnetic = None
        while magnetic != 'y' and magnetic != 'n':
            magnetic = input("Magnetic? y/n: ")
            self.magnetic = magnetic
        stateAtRoomTemp = None
        while stateAtRoomTemp != 's' and stateAtRoomTemp != 'l' and stateAtRoomTemp != 'g':
            stateAtRoomTemp = input("State at room temperature s/l/g: ")
            self.stateAtRoomTemp = stateAtRoomTemp
        self.meltingPoint = input("Molecule melting point: ")
        self.boilingPoint = input("Molecule boiling point: ")
        print()

    def inputValues(self):
        sql = "INSERT INTO IsotopeTable (baseElement, name, neutronCount, isotopPercentage, atomicNumber, " \
              "radioactive, magnetic, stateAtRoomTemp, meltingPoint, boilingPoint)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.baseElement, self.name, self.neutronNumber, self.isotopePercentage, self.atomicNumber,
               self.radioactive, self.magnetic, self.stateAtRoomTemp, self.meltingPoint, self.boilingPoint)
        mycursor.execute(sql, val)
        mydb.commit()

    def printValues(self):
        print("Base element:", self.baseElement)
        print("Isotope name:", self.name)
        print("Amount of neutrons:", self.neutronNumber)
        print("Atomic number:", self.atomicNumber)
        print("Radioactive: ", self.radioactive)
        print("Magnetic:", self.magnetic)
        print("State at room temperature:", self.stateAtRoomTemp)
        print("Melting point:", self.meltingPoint)
        print("Boiling point:", self.boilingPoint)
        print()


def view(table):
    if table.lower() == "elementtable":
        mycursor.execute("SELECT * FROM "+table+" ORDER BY LENGTH(atomicNumber) ASC, atomicNumber ASC")
        result = mycursor.fetchall()
        data = []
        for x in result:
            data.append(x)
        col_names = ["Element Symbol", "Element Name", "Atomic Number", "Atomic\nWeight (u)",
                    "Amount of\nElectrons", "Element Group", "Radioactive", "Magnetic", "State at room\nTemperature (s/l/g)",
                    "Melting\nPoint (°C)", "Boiling\nPoint (°C)"]
        print()
        print(tabulate(data, headers=col_names))
        print()
    elif table.lower() == "moleculetable":
        mycursor.execute("SELECT * FROM "+table+" ORDER BY name ASC")
        result = mycursor.fetchall()
        data = []
        for x in result:
            data.append(x)
        col_names = ["Molecule Formula", "Molecule Name", "Amount of\nElectrons", "Bond type", "Bond diagram",
                     "Radioactive", "Magnetic", "State at room\nTemperature (s/l/g)",
                     "Melting\nPoint (°C)", "Boiling\nPoint (°C)"]
        print()
        print(tabulate(data, headers=col_names))
        print()
    elif table.lower() == "isotopetable":
        mycursor.execute("SELECT * FROM "+table+" ORDER BY LENGTH(atomicNumber) ASC, atomicNumber ASC"
                         ", LENGTH(neutronCount) ASC, neutronCount ASC")
        result = mycursor.fetchall()
        data = []
        for x in result:
            data.append(x)
        col_names = ["Base Element", "Isotope Name", "Amount of\nNeutrons", "Percentage", "Atomic Number",
                     "Radioactive", "Magnetic", "State at room\nTemperature (s/l/g)", "Melting\nPoint (°C)",
                     "Boiling\nPoint (°C)"]
        print()
        print(tabulate(data, headers=col_names))
        print()


def searchRecords(table, operation):
    search = input("Search here: ")
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='"+table+"'")
    myresult = mycursor.fetchall()
    columns = []
    for x in myresult:
        columns.append(x)
    count = 0
    for x in columns:
        sql = "SELECT * FROM "+table+" WHERE "+columns[count][0]+" LIKE '%"+search+"%'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        if result:
            if operation == 's':
                showRecords(result, table)
                return None
            for i in result:
                if operation == 'm':
                    showRecords(result, table)
                    print("Update or delete?")
                    answer = input("u/d")
                    if answer == 'd':
                        deleteRecords(columns[count][0], table, search)
                        return None
                    elif answer == 'u':
                        updateRecords(columns[count][0], table, search)
                        return None
        count = count + 1
    return None


def deleteRecords(count, table, search):
    print("Is this the record you want to delete?")
    mycursor.execute("SELECT * FROM "+table+" WHERE "+count+" LIKE '%"+search+"%'")
    results = mycursor.fetchall()
    showRecords(results, table)
    choice = input("\ny/n")
    if choice == 'y':
        mycursor.execute("DELETE FROM "+table+" WHERE "+count+" = '"+search+"'")
        mydb.commit()
        print("Record deleted")
    return None


def updateRecords(count, table, search):
    mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='" + table + "'")
    myresult = mycursor.fetchall()
    iteration = 0
    for x in myresult:
        if x[0] == 'name':
            nameColumnNo = iteration
        iteration = iteration + 1
    print("Is this the record you want to update?")
    mycursor.execute("SELECT * FROM " + table + " WHERE " + count + " LIKE '%" + search + "%'")
    results = mycursor.fetchall()
    name = results[0][nameColumnNo]
    showRecords(results, table)
    choice = input("\ny/n")
    if choice == 'y':
        print("Which record do you want to modify?")
        column = selectColumn(table)
        print("Updating to:")
        update = input("Enter new value: ")
        print(count)
        mycursor.execute("UPDATE "+table+" SET "+column+" = '"+update+"' WHERE name = '"+name+"'")
        mydb.commit()
        print("Record updated")
    return None


def selectColumn(table):
    match = False
    while not match:
        mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='" + table + "'")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x[0])
        answer = input("Please enter column of record you wish to delete: ")
        for x in myresult:
            if answer == x[0]:
                return x[0]


def showRecords(results, table):
    data = []
    for x in results:
        print(x)
        data.append(x)
    if table.lower() == "elementtable":
        col_names = ["Element Symbol", "Element Name", "Atomic Number", "Atomic\nWeight (u)",
                    "Amount of\nElectrons", "Element Group", "Radioactive", "Magnetic", "State at room\nTemperature (s/l/g)",
                    "Melting\nPoint (°C)", "Boiling\nPoint (°C)"]
        print()
        print(tabulate(data, headers=col_names))
        print()
    elif table.lower() == "moleculetable":
        col_names = ["Molecule Formula", "Molecule Name", "Amount of\nElectrons", "Bond type", "Bond diagram",
                     "Radioactive", "Magnetic", "State at room\nTemperature (s/l/g)",
                     "Melting\nPoint (°C)", "Boiling\nPoint (°C)"]
        print()
        print(tabulate(data, headers=col_names))
        print()
    elif table.lower() == "isotopetable":
        col_names = ["Base Element", "Isotope Name", "Amount of\nNeutrons", "Percentage", "Atomic Number",
                     "Radioactive", "Magnetic", "State at room\nTemperature (s/l/g)", "Melting\nPoint (°C)",
                     "Boiling\nPoint (°C)"]
        print()
        print(tabulate(data, headers=col_names))
        print()


def admin():
    print("Enter a admin command or enter 'exit' to leave admin mode")
    print("Restore")
    command = input()
    command = command.lower()
    if command == "restore":
        restore()
    elif command == "exit":
        return None


def backup():
    file = open("ElementTable.txt", "w")
    mycursor.execute("SELECT * FROM ElementTable ORDER BY LENGTH(atomicNumber) ASC, atomicNumber ASC")
    result = mycursor.fetchall()
    data = []
    for x in result:
        line = ''
        for i in x:
            line = line+i+'|'
        line = line+"\n"
        data.append(line)
    file.writelines(data)
    file.close()
    file = open("moleculeTable.txt", "w")
    mycursor.execute("SELECT * FROM moleculeTable ORDER BY LENGTH(name) ASC, name ASC")
    result = mycursor.fetchall()
    data = []
    for x in result:
        line = ''
        for i in x:
            line = line + i + '|'
        line = line + "\n"
        data.append(line)
    file.writelines(data)
    file.close()
    file = open("IsotopeTable.txt", "w")
    mycursor.execute("SELECT * FROM IsotopeTable ORDER BY LENGTH(atomicNumber) ASC, atomicNumber ASC"
                     ", LENGTH(neutronCount) ASC, neutronCount ASC")
    result = mycursor.fetchall()
    data = []
    for x in result:
        line = ''
        for i in x:
            line = line + i + '|'
        line = line + "\n"
        data.append(line)
    file.writelines(data)
    file.close()
    print("Automatic backup complete")


def restore():
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


def logIn():
    login = False
    while not login:
        global mycursor
        global mydb
        global Uname
        global pwd
        print("Please log in:")
        Uname = input("Username: ")
        pwd = input("Password: ")
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user=Uname,
                password=pwd,
                database="ChemicalDatabase"
            )
        except:
            print("Incorrect username or password\n")
            print()
        else:
            mycursor = mydb.cursor()
            print()
            login = True


print()
print("RETIS software")
print()
logIn()

if Uname == "root":
    print("For admin controls type 'admin' or press enter to continue")
    if input() == "admin":
        admin()

print("Hi! Welcome to my chemical database")
tableDecision = False
while not tableDecision:
    print("Please choose a table from the list below or type 'exit' to quit")
    mycursor.execute("SHOW TABLES")
    result = mycursor.fetchall()
    for x in result:
        print("-"+x[0])
    print()
    tableChoice = input("Table: ")
    if tableChoice.lower() == "exit":
        backup()
        mydb.close()
        print("Byeeee!")
        exit()
    action = False
    while not action:
        print("Please choose to add, search, view or modify or type 'back' to go back")
        answer = input("a/s/v/m: ")
        if answer == 'a':
            if tableChoice.lower() == "elementtable":
                random = Element()
                random.inputValues()
                random.printValues()
            elif tableChoice.lower() == "moleculetable":
                random = Molecule()
                random.inputValues()
                random.printValues()
            elif tableChoice.lower() == "isotopetable":
                random = Isotope()
                random.inputValues()
                random.printValues()
        elif answer == 'v':
            view(tableChoice)
        elif answer == 's':
            searchRecords(tableChoice, 's')
        elif answer == 'm':
            searchRecords(tableChoice, 'm')
        elif answer.lower() == "back":
            action = True
        answer = None
