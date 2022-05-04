import pandas as pd
df = pd.read_csv("dwarf_stars.csv")
float(df["Radius"])
df["Radius"] = 0.102763*df["Radius"]

float(df["Mass"])
df["Mass"] = 0.000954588*df["Mass"]
df.to_csv("unit_converted_stars.csv")