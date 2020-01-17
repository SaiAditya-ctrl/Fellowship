
try:
    import json
except ImportError:
    print("import error")


class AddressBook():  


    def __init__(self, filename):  
        with open(filename) as f:
            
            self.data = json.load(f) 
    
    def addRecord(self):  
        while True:
            try:
                

                first_name = input("enter your first name :")
                if first_name.isalpha() is False:
                    print("enter vaild name ")
                    continue

                last_name = input("enter your last name :")
                if last_name.isalpha() is False:
                    print("length of last name should be less than 26")
                    continue

                address = input("enter your 1st and 2nd line of address :")
                if len(address) >= 100:
                    print("length of address should be less than 100")
                    continue

               
                city = input("\nenter the city name from above list :")
                
               

                state = input("enter the state name :")

                zipcode = int(input("enter the zip code :"))
                if len(str(zipcode)) >= 7:
                    print("length of input should be less than 7")
                    continue

                phone_number = int(input("enter the full mobile number"))
                if phone_number <= 916000000000 or phone_number >= 920000000000:
                    print("enter vaild number starting from 91")
                    continue

            
                dic = {"first_name": first_name,
                       "last_name": last_name,
                       "address": address,
                       "city": city,
                       "state": state,
                       "zipcode": zipcode,
                       "phone_number": phone_number}
                print("user data added successfully")
                s=open(filename,'a')
                d1=json.load(s)

                data = self.data
                
                data.append(dic)
                 
                print(dic)
                
                break
            except ValueError:
                print("check user input")
    
    def delete(self):  

        
        delete = input("\nname of the person you want to delete from the address book :")
        print(datadelete, "is deleted from address book ")

        name = []
        for i in range(len(self.data)):
            name.append(self.data[i]["first_name"])
               index = -1  
        
        for para in self.data:  
            index += 1
           
            if datadelete == para["first_name"]: 
               
                del self.data[index] 
             
                return index  
        print(datadelete, " is deleted from address book ")
   
    def printData(self):  

        data = self.data
      
        for i in range(len(data)):  
            for j in data[i].values():
                print(j)
            print()

    def sort(self): 

        array = []
        data = self.data  

        for i in range(len(self.data)): 
            array.append((self.data[i]["first_name"]))
        name_sort = sorted(array) 

        sorteddata = []  

        for i in name_sort:  
            for j in range(len(data)):
                if i == data[j]["first_name"]:
                    sorteddata.append(data[j]) 
        self.data = sorteddata  
        return sorteddata  

    def dumping(self, filename):  
        
        with open('/home/bridgelabz/Videos/DS/AddressBook/address_json.json', 'w') as f:
            json.dump(self.data, f, indent=2)

    def onlyNames(self): 
        data = self.data
        for i in range(len(data)):

             print("**", (data[i]["first_name"]), end=" ")
