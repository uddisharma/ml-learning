import pandas as pd

# s = pd.Series([10, 20, 30])
# print(s)

data = {"name": ["Naruto", "Luffy"], "episodes": [720, 1000]}
data2 = {"name": ["Deepak", "Kamal"], "episodes": [500, 2000]}


df = pd.DataFrame(data)
df1 = pd.DataFrame(data2)

# print(df)
# df.to_csv("output.csv", index=False)

file = pd.read_csv("./output.csv")
# print(file) # all columns
# print(file[["name", "episodes"]])  # select the columns

# print(file.loc[0])
# print(file.iloc[1])
# print(file.loc[0:2, ["name", "episodes"]])

# print(file[file["episodes"] > 800]) # condition
# print(file[(file["episodes"] > 500) & (file["name"] == "Naruto")]) #double condition

file["rating"] = [9, 10]  # add new column
# print(file)

file.drop("rating", axis=1, inplace=True)
# print(file)

# join
print(pd.merge(df1, df, on="name", how="inner"))
