

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125718 
- **Columns**: 5

### Column Details

 #   Column         Non-Null Count   Dtype  
---  ------         --------------   -----  
 0   income_groups  119412 non-null  object 
 1   age            119495 non-null  float64
 2   gender         119811 non-null  float64
 3   year           119516 non-null  float64
 4   population     119378 non-null  float64
dtypes: float64(4), object(1)


## Identified Issues

### Issue 1: Duplicates
- **Description**: There are 2950 duplicate rows in the dataset.
- **Affected Column(s)**: All columns (affected by rows)
- **Example**: duplicates in every column
- **Potential Impact**: Duplicates can skew analysis/results 

### Issue 2: Missing Values
- **Description**: There are missing values in the 'population' column.
- **Affected Column(s)**: income_groups, age, gender, year, population       
- **Example**: income_groups has 6306 missing values 
- **Potential Impact**: Missing values can lead to inaccurate analysis calculations 

### Issue 3: Unexpected Data Types
- **Description**: Many column are classified as the wrong data type
- **Affected Column(s)**: year, age, gender
- **Example**: 'year' and 'age' columns are stored as a float instead of an integer.
- **Potential Impact**: Incorrect data types can lead to errors in analysis and visualization


## 2. Data Cleaning Process
