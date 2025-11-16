#MapPlot.py
#Name:
#Date:
#Assignment:
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import coffee

coffee_data = coffee.get_coffee()

years = []
scores = []

for bean in coffee_data:
    year = bean["Year"]
    score = bean["Data"]["Scores"]["Total"]   # adjust key if needed
    if score != 0:
        years.append(year)
        scores.append(score)

df = pd.DataFrame({"Year": years, "Score": scores})

# --- Outlier removal using IQR ---
Q1 = df["Score"].quantile(0.25)
Q3 = df["Score"].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[(df["Score"] >= Q1 - 1.5*IQR) & (df["Score"] <= Q3 + 1.5*IQR)]

# --- Plot cleaned data without dashes ---
plt.figure(figsize=(8,6))
plt.scatter(df_clean["Year"], df_clean["Score"], c=df_clean["Score"], cmap="viridis", s=100, edgecolors="k")

plt.title("Coffee Intensity Scores Over Years", fontsize=16, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Total Score")
plt.colorbar(label="Score Intensity")
plt.grid(True, linestyle=":", alpha=0.7)

plt.savefig("chart.png", dpi=300)
plt.show()

