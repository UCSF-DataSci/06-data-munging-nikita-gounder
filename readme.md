

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
- **Affected Column(s)**: year and population
- **Example**: 'year' and 'population' columns are stored as string instead of integers.
- **Potential Impact**: Incorrect data types can lead to errors in analysis and visualization

### Issue 4: Outliers
- **Description**: Some columns have outlying values
- **Affected Column(s)**: population
- **Example**: 
- **Potential Impact**: Outliers can skew data analsyis by in/de-flating values

### Issue 5: Inconcsistent Categories
- **Description**: Some columns have extra categories
- **Affected Column(s)**: gender
- **Example**: additional category "3"
- **Potential Impact**: Inconsistent categories can mean misclassified values that then mess up our analysis


## 2. Data Cleaning Process

### Issue 1: [Issue Name]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 2: [Next Issue]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 3: [Next Issue]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 4: [Next Issue]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 5: [Next Issue]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
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

