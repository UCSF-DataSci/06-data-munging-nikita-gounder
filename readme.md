

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718 
- **Columns**: 5

### Column Details
| Column Name     | Data Type | Non-Null Count  | Unique Values | Mean         |
|------------------|-----------|-----------------|---------------|--------------|
| income_groups     | object    | 119412 non-null | 8             | N/A          |
| age               | float64  | 119495 non-null | 101           | 50.007038    |
| gender            | float64  | 119811 non-null | 3             | 1.578578     |
| year              | float64  | 119516 non-null | 169           | 2025.068049  |
| population        | float64  | 119378 non-null | 114925        | 111298300.0  |


## Identified Issues

### Issue 1: Duplicates
- **Description**: There are 2950 duplicate rows in the dataset.
- **Affected Column(s)**: All columns (affected by rows)
- **Example**: duplicates in every column
- **Potential Impact**: Duplicates can skew analysis/results 

### Issue 2: Missing Values
- **Description**: There are missing values in many column.
- **Affected Column(s)**: income_groups, age, gender, year, population       
- **Example**: income_groups has 6306 missing values 
- **Potential Impact**: Missing values can lead to inaccurate analysis calculations 

### Issue 3: Unexpected Data Types
- **Description**: Many column are classified as the wrong data type
- **Affected Column(s)**: year and population
- **Example**: 'year' and 'population' columns are stored as string instead of integers.
- **Potential Impact**: Incorrect data types can lead to errors in analysis and visualization

### Issue 4: Outliers
- **Description**: Some columns have outlying values
- **Affected Column(s)**: population
- **Example**: the populaton columns has many outlying values as seen by the IQR
- **Potential Impact**: Outliers can skew data analsyis by in/de-flating values

### Issue 5: Inconcsistent Categories
- **Description**: Some columns have extra categories
- **Affected Column(s)**: gender
- **Example**: additional category "3"
- **Potential Impact**: Inconsistent categories can mean misclassified values that then mess up our analysis


## 2. Data Cleaning Process

### Issue 1: [Missing Values]
- **Cleaning Method**: Detect missing values and drop rows with missing values
- **Implementation**:
  ```python
  df.isna().sum()
  df_clean = df.dropna()
  ```
- **Justification**: Since we don't have a good measure of replacement (replacing with mean only works depending on data), dropping the rows seemed like the best solution.
- **Impact**: 
  - Rows affected: 30978 missing values in total
  - Data distribution change: This is a lot of missing values so a lot of the key values may change

### Issue 2: [Duplicates]
- **Cleaning Method**: check for and remove duplicates
- **Implementation**:
  ```python
  df.duplicated()
  df_clean = df.drop_duplicates()
  ```
- **Justification**: duplicates implies that the value already exists somewhere, therefore taking out unecessary duplications is the best solution
- **Impact**: 
  - Rows affected: 2950 duplcate values in rows
  - Data distribution change: Everything will probably decrease a bit since many excess values were removed

### Issue 3: [Outliers]
- **Cleaning Method**: using IQR to find and remove outliers
- **Implementation**:
  ```python
  Q1 = df['population'].quantile(0.25)
  Q3 = df['population'].quantile(0.75)
  IQR = Q3 - Q1
  df_clean = df[~((df['population'] < (Q1 - 1.5 * IQR)) | (df['population'] > (Q3 + 1.5 * IQR)))]
  ```
- **Justification**: Identifies values above and below quartiles and removes them
- **Impact**: 
  - Rows affected: population column
  - Data distribution change: More accurate representation of the population data without these outlying values

### Issue 5: [Fix Caetgorical Values]
- **Cleaning Method**: Identifies values in geneder that are not categorized correctly and replaces w/ 0
- **Implementation**:
  ```python
  valid_categories = [1.0,2.0]
  df.loc[~df['gender'].isin(valid_categories), 'gender'] = 0.0
  print(df['gender'].value_counts())
  ```
- **Justification**: Since we do not know what the real value is,it is best to make a new category to still represent the data
- **Impact**: 
  - Rows affected: gender column with any 3 values
  - Data distribution change: [Describe any significant changes]


## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv (or whatever you named it)
- **Rows**: [Your answer]
- **Columns**: [Your answer]

### Column Details
| Column Name | Data Type | Non-Null Count | #Unique Values |  Mean  |
|-------------|-----------|----------------|----------------|--------|
| [Column 1]  | [Type]    | [Count]        | [#Unique]      | [Mean] |
| ...         | ...       | ...            | ...            | ...    |

### Summary of Changes
- [List major changes made to the dataset]
- [Discuss any significant changes in data distribution]

