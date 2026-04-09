#This was only used for combining the columns across multiple csv file no need to run this code 
import pandas as pd

data = pd.read_csv('data.csv')
data.head()


new_data =data[['Label','Language']]
new_data.to_csv('new_data.csv',index=False)

more_data = data[["Label", "Language_ur"]]

# Step 3: Rename "Language_ur" to "Language" so it matches new_file.csv
more_data = more_data.rename(columns={"Language_ur": "Language"})

# Step 4: Append into new_file.csv without repeating headers
more_data.to_csv("new_data.csv", mode="a", index=False, header=False)

print("Done! Rows added to new_file.csv successfully!")