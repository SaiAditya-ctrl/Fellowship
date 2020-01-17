
try:
    import re
except ImportError:
    print("import error")

class Regex:
    
    def check(self):
        with open ('file.txt', 'r') as f:
            text = f.read()
            print(text)
        try:
            
            result = re.sub(r"[<]{2}[a-zA-Z]{4}[>]{2}", "<<SaiAditya>>", text)
            result = re.sub(r"[<]{2}[a-zA-Z]{8}[>]{2}", "<<Ede Sai Aditya>>", result)
            result = re.sub(r"[0-9]{10}", "4567586948", result)
            result = re.sub(r"[0-9]{2}/[0-9]{2}/[0=9]{4}", "01/02/2018", result)
            file1 = open("file.txt","w")
            file1.write(result) 
            print(result)
        except:
            
            print("An exception occurred")
 

obj = Regex()

obj.check()
