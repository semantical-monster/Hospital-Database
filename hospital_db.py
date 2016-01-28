# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect(host="N/A", user = "dt339", passwd = "ab1234", db = "troxler_dbms")

cur = db.cursor()

q = int(0)

run = True

while run:
    
    user = input("What operation would you like to perform on the Database?\n1. Enterinformation on newly‐hired doctors\n2. Remove information on doctors no longer employed\n3. Produce a listing ofthe names and specialties of all doctors currently employed\n4. Change the contents of a doctor’srecord.\n5. Admit patientsto the hospital.\n6. Provide visibility to a patient’srecord.\n7. Produce a list of allthe patients of a given doctor.\n8. Dismiss patientsfromthe hospital.\n9. Change the contents of a patient’srecord.\n10. Be able to search by doctorspecialty and patient primary illness.\n11. Assign patient to doctor\n12. Quit\n")
    if user == 1:
        dID = raw_input("What is the doctor's ID number?\n")
        specialty = raw_input("What is the doctor's specialty?\n")
        doc_name = raw_input("What is the name of the doctor?\n")
        cur.execute("INSERT INTO Doctors (DOC_ID,SPECIALTY,DOC_NAME) VALUES('"+str(dID)+"','"+str(specialty)+"','"+str(doc_name)+"')")
        #cur.execute("")

    if user == 2:
        doc_delete = raw_input("What is the name of the doctor you would like to remove?\n")
        doc_delete2 = raw_input("What is the ID of the doctor you would like to remove?\n")
        cur.execute("DELETE FROM Doctors WHERE Doctors.DOC_NAME = ('"+str(doc_delete)+"') OR Doctors.DOC_ID = ('"+str(doc_delete2)+"')")
            
    if user == 3:
        cur.execute("SELECT * FROM Doctors")
        doctors = cur.fetchall()
        print("")
        print("Current Doctors")
        print("---------------")
        for each in doctors:
            print(str(each[0])+", "+each[2]+", "+each[1])
        print("")    
       
    if user == 4:
        y = raw_input("What is the name of the doctor you would like to update?\n")
        update = raw_input("What do you want to update?\n1. Doctor ID\n2. Specialty\n3. Name\n")
        if update == "1":
            new_id = raw_input("What do you want the new ID to be?\n")
            cur.execute("UPDATE Doctors SET DOC_ID = ('"+str(new_id)+"') WHERE Doctors.DOC_NAME = ('"+str(y)+"')")
        if update == "2":
            new_specialty = raw_input("What is the specialty of the doctor?\n")
            cur.execute("UPDATE Doctors SET SPECIALTY = ('"+str(new_specialty)+"') WHERE Doctors.DOC_NAME = ('"+str(y)+"')")
        if update == "3":
            new_name = raw_input("What is the name of the doctor?\n")
            cur.execute("UPDATE Doctors SET DOC_NAME = ('"+str(new_name)+"') WHERE Doctors.DOC_NAME = ('"+str(y)+"')")
            
    if user == 5:
        pName = raw_input("What is the name of the patient?\n")
        pIllness = raw_input("What is the patient's illness?\n")
        pAdmissionDate = raw_input("What date was the patient admitted?\n")
        cur.execute("INSERT INTO Patients (ADMISSION_DATE,PATIENT_NAME,ILLNESS) VALUES('"+str(pAdmissionDate)+"','"+str(pName)+"','"+str(pIllness)+"')")

    if user == 6:
        pView = raw_input("What is the name of the patient you would like to view?\n")
        
        cur.execute("SELECT * FROM Patients WHERE Patients.PATIENT_NAME = '"+str(pView)+"'")
        patients = cur.fetchall()
        print("")
        print("Patient's record:")
        print("---------------")
        for each in patients:
            print("ID: " +str(each[0])+", Admission Date: "+each[1]+", Release Date: "+each[2]+"\nName: "+each[3]+", Illness: "+each[4])
        print("")

    if user == 7:
        dVisible = raw_input("What is the name of the doctor?\n")
        cur.execute("SELECT DOC_ID FROM Doctors WHERE Doctors.DOC_NAME = '"+str(dVisible)+"'")
        p = cur.fetchall()
        p = str(p[0])
        p = p.replace("L","")
        p = p.replace(",","")
        p = p.replace("(","")
        p = p.replace(")","")
        p = int(p)
        cur.execute("SELECT PATIENT_ID FROM Cares_For WHERE DOC_ID = '"+str(p)+"'")
        pid = []
        z = cur.fetchall()
        for i in z:
            j = str(i[0])
            j = j.replace("L","")
            pid.append(j)
        pname = []
        for each in pid:    
            cur.execute("SELECT PATIENT_NAME FROM Patients WHERE PATIENT_ID = '"+str(each)+"'")
            for d in cur.fetchall():
                pname.append(d[0])
        for each in pname:
            print("Current patients: ")
            print(each)
            print(" ")

    if user == 8:
        doc_remove = raw_input("What is the name of the patient to be dismissed?\n")
        rDate = raw_input("What is the date the patient is being dismissed?\n")
        cur.execute("UPDATE Patients SET RELEASE_DATE = ('"+str(rDate)+"') WHERE Patients.PATIENT_NAME = '"+str(doc_remove)+"'")

    if user == 9:
        choice = input("What would you like to edit?\n1. Name\n2. Illness\n")
        ePatient = raw_input("What is the name of the patient you want to update?\n")
        if choice == 1:
            new_name = raw_input("What is the new name?\n")
            cur.execute("UPDATE Patients SET PATIENT_NAME = '"+str(new_name)+"' WHERE Patients.PATIENT_NAME = '"+str(ePatient)+"'")
        if choice == 2:
            new_illness = raw_input("What is the new illness?\n")
            cur.execute("UPDATE Patients SET ILLNESS = '"+str(new_illness)+"' WHERE Patients.PATIENT_NAME = '"+str(ePatient)+"'")

    if user == 10:
        choice = input("What would you like to search by?\n1. Doctor specialty\n2. Patient illness\n")
        if choice == 1:
            x = raw_input("What specialty would you like to search by?\n")
            cur.execute("SELECT * FROM Doctors WHERE Doctors.SPECIALTY = '"+str(x)+"'")
            y = cur.fetchall()
            for each in y:
                print(each[2])
                print(" ")
        if choice == 2:
            x = raw_input("What illness would you like to search by?\n")
            cur.execute("SELECT * FROM Patients WHERE Patients.ILLNESS = '"+str(x)+"'")
            y = cur.fetchall()
            for each in y:
                print(each[3])
                print(" ")            
        
    if user == 11:
        pSelect = raw_input("What is the name of the patient you want to assign a doctor to?\n")
        cur.execute("SELECT PATIENT_ID FROM Patients WHERE Patients.PATIENT_NAME = '"+str(pSelect)+"'")
        p = cur.fetchall()
        p = str(p[0])
        p = p.replace("L","")
        p = p.replace(",","")
        p = p.replace("(","")
        p = p.replace(")","")
        p = int(p)
        dSelect = raw_input("What is the name of the doctor you want to assign?\n")
        cur.execute("SELECT DOC_ID FROM Doctors WHERE Doctors.DOC_NAME = '"+str(dSelect)+"'")
        d = cur.fetchall()
        d = str(d[0])
        d = d.replace("L","")
        d = d.replace(",","")
        d = d.replace("(","")
        d = d.replace(")","")
        d = int(d)
        rID = raw_input("What relational ID would you like to assign to the two?\n")
        cur.execute("INSERT INTO Cares_For (RELATION_ID,DOC_ID,PATIENT_ID) VALUES('"+str(rID)+"','"+str(d)+"','"+str(p)+"')")
        
    if user == 12:
        run = False
    
