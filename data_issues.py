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


# Using IQR, check for outliers
Q1 = df['population'].quantile(0.25)
Q3 = df['population'].quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# Check categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\nUnique values in {col}:")
    print(df[col].value_counts())

# Check for valid values in a categorical column
valid_categories = ['1', '2']
df['is_valid'] = df['gender'].isin(valid_categories)
df['is_valid']

