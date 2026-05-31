import pandas as pd

df = pd.read_csv('contacts.csv')

df.to_excel("contacts.xlsx", index=False)