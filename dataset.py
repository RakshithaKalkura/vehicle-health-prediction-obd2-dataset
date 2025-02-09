import pandas as pd

xlsx_file = "data.xlsx"
csv_file = "dataset.csv" 

df = pd.read_excel(xlsx_file)
df.to_csv(csv_file, index=False)
df = pd.DataFrame(pd.read_excel("Test.xlsx")) 

print(f"Converted {xlsx_file} to {csv_file} successfully!")
