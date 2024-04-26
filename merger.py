import pandas as pd

df1 = pd.read_excel(io='anon_data1.xlsx')
df2 = pd.read_excel(io='anon_data2.xlsx')

mapping_table = {
    "Leader Name": "Participant_Name",
    "Leader Email": "Participant_Email",
    "Leader Phone": "Participant_Mobile",
    "Candidate's Name": "Participant_Name",
    "Candidate's Email": "Participant_Email",
    "Candidate's Mobile": "Participant_Mobile",
    "Candidate Type": "Participant_Type"
}

val1 = df1[['Team Name', 'Leader Name', 'Leader Email', 'Leader Phone']].rename(columns=mapping_table)
val2 = df2[["Team Name", "Candidate's Name", "Candidate's Email", "Candidate's Mobile", "Candidate Type"]].rename(columns=mapping_table)
val1["Participant_Type"] = "team leader"

merged_df = pd.concat([val1, val2]).drop_duplicates(subset="Participant_Email", keep="first")
merged_df['Participant_Mobile'] = merged_df['Participant_Mobile'].astype(str)

merged_df.to_excel('merged_spreadsheet.xlsx', index=False)
