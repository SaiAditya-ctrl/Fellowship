
import json

class Stock:

    def getStockDetails(self):
       
        with open('stock_json.json') as f:

            
            data1= json.load(f)
            
            data = data1["Stock_report"]
        return data


stock=Stock()

a =stock.getStockDetails()
