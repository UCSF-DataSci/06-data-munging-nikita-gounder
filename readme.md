

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
