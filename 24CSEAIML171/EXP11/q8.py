import pandas as pd
df_csv = pd.read_csv(r'C:\Users\student\Desktop\24CSEAIML230\EXP11\sample.csv')
print("DataFrame from CSV:")
print(df_csv)
df_json = pd.read_json(r'C:\Users\student\Desktop\24CSEAIML230\EXP11\sample.json')
print(df_json)