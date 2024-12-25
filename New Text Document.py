import pandas as pd 
file=pd.read_json(r"C:\Users\h\OneDrive\Desktop\PMW\New Text Document.json")
file.to_csv(r"C:\Users\h\OneDrive\Desktop\PMW\New Text Document.csv")
print("convert_from_CSV_to_json")