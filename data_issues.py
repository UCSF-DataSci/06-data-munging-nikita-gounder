import pandas as pd
#python3 data_issues.py

# Relevant df info
df = pd.read_csv('messy_population_data.csv')
print(df.head())
print(df.info())
print(df.describe())

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Check for missing values
missing_values = df.isnull().sum()
print(f"Number of missing values: {missing_values}")

# Validate data types
print(df.dtypes)

# Unique value counts
unique_counts = df.nunique()
print(f"Number of unique values: {unique_counts}")


