
import pandas as pd
file_path=r"C:\Users\yoeshwar\Downloads\hyderabad_companies.csv"
df=pd.read_csv(file_path)
revenue_words=[
"600","700","800","900",
"1000","1200","1500",
"2000","3000","5000"
]
pe_words=[
"pe backed",
"private equity",
"vc backed",
"venture capital",
"blackstone",
"carlyle",
"kkr",
"advent",
"warburg",
"tpg",
"investor owned"
]
df["Revenue Band"]=df["Revenue Band"].astype(str).str.lower()
df["Verdict Reasoning"]=df["Verdict Reasoning"].astype(str).str.lower()
df["Federer Score"]=pd.to_numeric(df["Federer Score"],errors="coerce")
revenue_check=~df["Revenue Band"].str.contains("|".join(revenue_words),na=False)
pe_check=~df["Verdict Reasoning"].str.contains("|".join(pe_words),na=False)
filtered_df=df[revenue_check & pe_check]
top_25_df=filtered_df.sort_values(by="Federer Score",ascending=False).head(25)
rejected_df=df[~df.index.isin(top_25_df.index)]
filtered_df.to_csv(r"C:\Users\yoeshwar\Downloads\filtered_companies.csv",index=False)
top_25_df.to_csv(r"C:\Users\yoeshwar\Downloads\top_25_companies.csv",index=False)
rejected_df.to_csv(r"C:\Users\yoeshwar\Downloads\rejected_companies.csv",index=False)
print("All files saved successfully")
print("filtered_companies.csv")
print("top_25_companies.csv")
print("rejected_companies.csv")

