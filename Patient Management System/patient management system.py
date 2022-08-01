# Q2. Create a Patient management system python console application that manages records of the patients in a hospital. You may use the MSSQL database

# • Implement basic CRUD operations for this scenario using dictionary in python.
# • There are four operations that are performed, namely, add patient record, update patient record, delete patient record and list with search for patient records.
# • The fields are patientId(int), patientName, gender, age, bloodGroup (string) for every patient.
# • Keep directory with patientId as key and rest as value array corresponding to each key.
# • Prompt user for the operation. 1. Add, 2.Update, 3.Delete, 4.List and Search. Make sure to alert user if a non int or blank value for patientId and blank for other fields.
# • All values should be received using user input only.

from pickle import TRUE
import pyodbc


class PMS:

    def __init__(self):
        self.conn = pyodbc.connect('''
        Driver={SQL Server};
        Server=DESKTOP-CSCIVVL\SQLEXPRESS;
        Database=patient_db;
        Trusted_Connection=yes;
    ''')
        self.cursor = self.conn.cursor()

    def isBlank(list):
        if '' in list:
            return TRUE

    def addPatient(self):
        try:
            self.patientId = int(input("Enter the patientId: "))
        except:
            print("Please enter an integer as patient ID")
            return
        else:
            self.patientName = input("Enter the name: ")
            self.gender = input("Enter the gender(M/F): ")
            self.age = input("Enter age: ")
            self.bloodGroup = input("Enter blood group: ")
        self.list = [self.patientId, self.patientName, self.gender, self.age, self.bloodGroup]
        self.checkBlank = PMS.isBlank(self.list)
        if self.checkBlank == TRUE:
            print("Cannot enter blank fields!")
        else:
            try:
                self.cursor = self.conn.cursor()
                self.cursor.execute('''
                    INSERT INTO PatientDetails VALUES (?,?,?,?,?);'''
                    ,(self.patientId, self.patientName, self.gender, self.age, self.bloodGroup)
                )
            except Exception as e:
                print("This patient ID already exists!")
            self.conn.commit()

    def updatePatient(self):
        try:
            self.patientId = int(input("Enter the patientId: "))
        except:
            print("Please enter an integer as patient ID")
            return
        else:
            self.patientName = input("Enter the name: ")
            self.gender = input("Enter the gender(M/F): ")
            self.age = input("Enter age:")
            self.bloodGroup = input("Enter blood group: ")
            self.list = [self.patientId, self.patientName, self.gender, self.age, self.bloodGroup]
            self.checkBlank = PMS.isBlank(self.list)
        if self.checkBlank == TRUE:
            print("Cannot enter blank fields!")
        else:
            try:
                    self.cursor = self.conn.cursor()
                    self.cursor.execute('''
                        UPDATE patientDetails
                        SET 
                            patientName = ?,
                            gender = ?,
                            age = ?,
                            bloodGroup = ?
                        WHERE
                            patientId = ?;'''
                        ,(self.patientName, self.gender, self.age, self.bloodGroup,self.patientId)
                        )
            except Exception as e:
                    print(type(e).__name__)
            self.conn.commit()

    def deletePatient(self):
        self.patientId = input("Enter the patient ID to be deleted: ")
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                DELETE FROM patientDetails
                WHERE patientId=(?);'''
                ,(self.patientId)
            )
        except Exception as e:
            print(type(e).__name__)
        self.conn.commit()

    def searchPatient(self):
        self.patientId = input("Enter the patient ID: ")
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                SELECT *
                FROM patientDetails
                WHERE patientId=(?);'''
                ,(self.patientId)
            )
            if self.cursor.rowcount == 0:
                print("No match found!")
                return
            for record in self.cursor.fetchall():
                print(f'''\nPatient ID: {record[0]}
                Patient Name: {record[1]}
                Gender: {record[2]}
                Age: {record[3]}
                Date of Birth: {record[4]}''')
        except Exception as e:
            print(type(e).__name__)       

    def listPatients(self):
        try:
            self.cursor.execute('''
                SELECT * FROM patientDetails;
            ''')
            for record in self.cursor.fetchall():
                print(f'''\nPatient ID: {record[0]}
                Patient Name: {record[1]}
                Gender: {record[2]}
                Age: {record[3]}
                Date of Birth: {record[4]}''')
        except Exception as e:
            print(type(e).__name__)


def displayMenu():
    global choice
    print("\nMENU:\n1 -> Add Patient\n2 -> Update Patient Details\n3 -> Delete Patient\n4 -> Search Patient\n5 -> List Patients\n6 -> Exit")
    choice = int(input("Enter your choice: "))
    return    

choice = 1
while(choice!=6):
    obj = PMS()
    displayMenu()
    if choice==1:
        obj.addPatient()
    elif choice==2:
        obj.updatePatient()
    elif choice==3:
        obj.deletePatient()
    elif choice==4:
        obj.searchPatient()
    elif choice==5:
        obj.listPatients()
    elif choice==6:
        print("Exited!")
        obj.conn.close()
        break
    else:
        print("Wrong choice")
    print("\nDisplaying Menu...")
    displayMenu()
