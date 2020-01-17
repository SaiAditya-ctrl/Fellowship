try:
    import json
except ImportError:
    print("import error")
class Search:

    def search(self):
        
        select = input(" who's details u want? (d/p):")
        
        if (select == "d") or (select == "D"):
            try:
               
                f = open("json_file.json","r")
                data_key= json.load(f)
                f.close()

            except FileNotFoundError:
                print("file not found")
            
            specialization=input("please Type Doctor specialization:")  
            
            for data in data_key["Doctors"]:
                if data["specialization"] == specialization:
                    
                    print("Doctor",data["name"],data["specialization"],"specialist", "Availability Time:",data["availability"])
                else:
                    f = open("new_doctor.json","a+")
                    def search(self):
                        contactNumber = input("Enter your Mobile Number: ")
                        availability = input("Enter the availability time: ")
                        cont = f.write(' [{'+'    "name" : "'+ name +'",\n' + '       "id" : "'+ id +'",\n' + '       "specialization"  : "'+str(specialization)+'",\n'+'       "contactNumber" : "'+str(contactNumber)+'",\n'+'       "availability" : "'+str(availability)+'"    }]\n')
                      
                        print("The Data has been Stored Successfully in 'new_doctor.json' file. ")
        elif(select == "p") or (select == "P"):
            try:
                f = open("json_file.json","r")
                data_key= json.load(f)

            except FileNotFoundError:
                print("file not found")
        
           
            name=input("your good name:")  
            for data in data_key["Patients"]:
                if data["name"] == name:
              
                    print("Patient Name:",data["name"],"Patient Gender:",data["gender"], "Patient Age:",data["age"])
                else:
                    f = open("new_patients.json","a+")
                    def search(self):
                        weight = input("Enter yor weight: ")
                        height = input("Enter yor height: ")
                        cont = f.write(' [{'+'    "name" : "'+ name +'",\n' + '       "id" : "'+ id +'",\n' + '       "gender" : "'+str(gender)+'",\n'+'       "age" : "'+str(age)+'",\n'+'       "profession"  : "'+str(profession)+'",\n'+'       "weight" : "'+weight+'",\n'+'       "height" : "'+height+'"  }]\n' )
                   
                        print("The Data has been Stored Successfully in 'new_patient.json' file. ")

find=Search()
find.search()
