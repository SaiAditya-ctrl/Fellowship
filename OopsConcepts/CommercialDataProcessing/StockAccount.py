
try:
    import json
except ImportError:
    print("import error")

if __name__ == '__main__' :
    inp = input(" Are having an Existing Account? (y/n):")
    if (inp == "y") or (inp == "Y"):
        try:
            f = open("newUser.json","r")
            data_key= json.load(f)

        except FileNotFoundError:
            print("file not found")
       
        customerId=input("please Type Your Registerd customer Id:")  
        for data in data_key["User"]:
            if data["customerId"] == customerId:
                
                print("Welcome",data["name"], "How much you want to buy shares")
               
                product_quantity=int(input("enter quantity")) 
                data["product"]+=product_quantity  
               
                amount=int(input("enter amount")) 
                data["share_amount"] -= amount 
                
                with open('newUser.json', '+w') as json_file:
                    json.dump(data_key, json_file)
    else:
        
        f = open("newUser.json","a+")
        customerId=input("Enter the customer Id: ")
        name = input("Enter the Name: ")
        age = int(input("Enter the Age: "))
        phno = int(input("Enter your Mobile Number: "))
        amount = int(input("Enter the Amount for Shares: "))
        product = int(input(" product qountity"))
       
        cont = f.write(' [{'+'    "customerId" : "'+ customerId +'",\n' + '       "name" : "'+ name +'",\n' + '       "age"  : "'+str(age)+'",\n'+'       "Ph.No" : "'+str(phno)+'",\n'+'       "share_amount" : "'+str(amount)+'"       "product"  : "'+str(product)+'",\n'+'             }]\n')
        print("The Data has been Stored Successfully in 'newUser.json' file. ")

class StockAccount:
   
    def getStockDetails(self):
        try:
            file=open("company_shares.json","r")
        
            data_key= json.load(file)
            data1=data_key["Company"]
            data2=data_key["Shares"]
            data3=data_key["Products"]
        except FileNotFoundError:
            print("file not found")
            

        
        type = int(input("\nType:0 for HCL share:Production\nType:1 for TCS share:Sales\nType 2 for CGI share: Marketing"))
        if type == 0:
            for data in data_key["Shares"]:
                if data['share'] == "Production":
                    input_amount=int(input("enter amount"))  
                    data['amount'] += input_amount
                    input_stock=int(input("enter stock"))  
                    data['stock']-=input_stock
                    with open('company_shares.json', '+w') as json_file:
                        json.dump(data_key, json_file)
        if type == 1:
            for data in data_key["Shares"]:
                print("hello")
                if data['share'] == "Sales": 
                    input_amount=int(input("enter amount"))
                    data['amount'] -= input_amount
                    with open('company_shares.json', '+w') as json_file:
                        json.dump(data_key, json_file)
        if type == 2:
            for data in data_key["Shares"]:
                print("hello")
                if data['share'] == "Marketing":
                    input_amount = int(input("enter amount"))
                    data['amount'] -= input_amount
                    with open('company_shares.json', '+w') as json_file:
                        json.dump(data_key, json_file)

        else: ("bye")


obj1=StockAccount()
obj2=obj1.getStockDetails()


   
