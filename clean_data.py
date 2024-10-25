# runnable Python script that takes messy_population_data.csv as input and outputs cleaned_population_data.csv
#python3 clean_data.py
import pandas as pd
df = pd.read_csv('messy_population_data.csv')

# Detect missing values
df.isna().sum()
# Drop rows with any missing values
df_clean = df.dropna()
# Forward fill
df.ffill()
# Backward fill
df.bfill()

# Check for duplicates
df.duplicated()
# Remove duplicates
df_clean = df.drop_duplicates()

# Using IQR, handle outliers
Q1 = df['population'].quantile(0.25)
Q3 = df['population'].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[~((df['population'] < (Q1 - 1.5 * IQR)) | (df['population'] > (Q3 + 1.5 * IQR)))]

# Check for valid values in a categorical column
df['gender'].dtype
valid_categories = [1.0,2.0]
# Replace invalid values with 0 to represent unknown
df.loc[~df['gender'].isin(valid_categories), 'gender'] = 0.0
print(df['gender'].value_counts())


output_file = 'clean_population_data.csv'
# Save the clean dataset
df_clean.to_csv(output_file, index=False)
print(f"\nClean dataset saved as '{output_file}'")

print(df_clean.info())
print(df_clean.describe())
unique_counts = df_clean.nunique()
print(unique_counts)
