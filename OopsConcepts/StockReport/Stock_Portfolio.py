
import json
from Stock import Stock

class Stock_Portfolio:
    def gettingAllData(self,data):
       
        total_number_of_share =0
        total_share_price =0
        total_stock_price =0
        for item in data:
            total_number_of_share = total_number_of_share+item["number_of_share"]
            total_share_price = total_share_price+item["share_price"]
            total_stock_price = total_stock_price+item["stock_price"]

        print("total number_of_share :",total_number_of_share)
        print("total share_price :",total_share_price)
        print("total stock_price :", total_stock_price)
       
    def eachdata(self,data):

        each_price=0

       
        for item in data:
            each_price=item["share_price"] * item["stock_price"]
            print("each_price :", each_price)
           
      
        json_string = json.dumps(data)
        print(json_string)

stock=Stock()
data = stock.getStockDetails()
obj=Stock_Portfolio()
obj.gettingAllData(data)
obj.eachdata(data)

