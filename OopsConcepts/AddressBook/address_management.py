try:
    import json
    from address_book import AddressBook
except ImportError:
    print("import error")

def addressbook_management():
    while True:
        address = AddressBook("address_json.json")

        try:  
            
            userdata = int(input("number of data you want to delete or add :"))
            if userdata>=10:
                print("enter the number below 10")
                continue
            for i in range(userdata):

                user = int(input("""\npress 1 to add\npress 2 to delete\
    \npress 3 to  exit \npress 4 to print in mailing format
                                   \nuser input :"""))
                if user>=5:
                    print("enter below 5")
                    continue

              
                if user == 1:
                    
                    print(address.addRecord())   
                
                if user == 2:
                    
                    address.onlyNames() 
                
                    address.delete()    
            
                if user == 3:

                    print("program ended")
                    return

                
                elif user == 4:
            
                    address.printData()  

            
                address.sort()
        
                print("\ndata is sorted which can be seen in json file ")
                address.dumping("/home/bridgelabz/Videos/DS/AddressBook/address_json.json")
                break

        except ValueError:
           
            print("check the input")



if __name__ == '__main__':
    addressbook_management()
