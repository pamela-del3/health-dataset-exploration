import pandas as pd
import matplotlib.pyplot as plt

print("Script is running")

# 1. Load dataset (Clean absolute path)
df = pd.read_csv("/Users/deepamelaa/Desktop/health-dataset-exploration/data/data.csv")

print("Columns:", df.columns)
print("Shape:", df.shape)
print(df.head())

# 2. Plot
df[df.columns[0]].hist() 

plt.title("Distribution")

# 3. Save the image (Clean absolute path)
plt.savefig("/Users/deepamelaa/Desktop/health-dataset-exploration/images/distribution.png")

plt.show()