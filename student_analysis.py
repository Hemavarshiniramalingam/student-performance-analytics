import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student_data.csv")

# Total & Average
df["Total"] = df[["Maths","Physics","Chemistry"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Pass / Fail
df["Result"] = np.where(df["Average"] >= 50, "Pass", "Fail")

print(df)

# Visualization
sns.barplot(x="Name", y="Average", data=df)
plt.title("Average Marks of Students")
plt.show()
