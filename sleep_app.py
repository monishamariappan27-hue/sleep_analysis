import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------
# 1. Load CSV
# ---------------------------
csv_file = "Sleepdata.csv"

# Read CSV with utf-8-sig to handle BOM
df = pd.read_csv(csv_file, encoding="utf-8-sig")

# Drop any unnamed index column if exists
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Clean column names (remove BOM or spaces)
df.columns = df.columns.str.replace("\ufeff", "", regex=True).str.strip()

print("\n===== CSV LOADED SUCCESSFULLY =====")
print("Columns:", df.columns.tolist())
print(df.head())

# ---------------------------
# 2. Convert Data Types
# ---------------------------
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", errors="coerce")
df["SleepHours"] = pd.to_numeric(df["SleepHours"], errors="coerce")
df["ScreenTime"] = pd.to_numeric(df["ScreenTime"], errors="coerce")
df["Mood"] = pd.to_numeric(df["Mood"], errors="coerce")
df["Energy"] = pd.to_numeric(df["Energy"], errors="coerce")

# Drop rows with missing critical values
df = df.dropna(subset=["Date", "SleepHours"]).reset_index(drop=True)

# ---------------------------
# 3. Summary Statistics
# ---------------------------
print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

# ---------------------------
# 4. Sleep Hours Trend
# ---------------------------
plt.figure(figsize=(10,4))
plt.plot(df["Date"], df["SleepHours"], marker="o", color="blue")
plt.title("Sleep Hours Trend")
plt.xlabel("Date")
plt.ylabel("Sleep Hours")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt.gcf())


# ---------------------------
# 5. Screen Time Trend
# ---------------------------
plt.figure(figsize=(10,4))
plt.plot(df["Date"], df["ScreenTime"], marker="o", color="red")
plt.title("Screen Time Trend")
plt.xlabel("Date")
plt.ylabel("Screen Time (Hours)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
st.pyplot(plt.gcf())


# ---------------------------
# 6. Mood & Energy Trend
# ---------------------------
plt.figure(figsize=(10,4))
plt.plot(df["Date"], df["Mood"], marker="o", label="Mood", color="green")
plt.plot(df["Date"], df["Energy"], marker="o", label="Energy", color="orange")
plt.title("Mood & Energy Trend")
plt.xlabel("Date")
plt.ylabel("Level")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
st.pyplot(plt.gcf())


# ---------------------------
# 7. Correlation Heatmap
# ---------------------------
plt.figure(figsize=(8,6))
sns.heatmap(df[["SleepHours","ScreenTime","Mood","Energy"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
st.pyplot(plt.gcf())



