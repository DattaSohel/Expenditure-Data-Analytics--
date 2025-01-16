# Required Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport  # Use ydata_profiling instead of pandas_profiling

# Step 1: Load Dataset
file_path = "D:\Aptech\Python\ExpenditureDB\Final_expenditure.csv"  # Replace with your dataset path
data = pd.read_csv(file_path)

# Step 2: Display Initial Information
print("Initial Dataset Information:")
print(data.info())
print("\nSummary Statistics:")
print(data.describe())

# Step 3: Generate Initial Profiling Report
profile = ProfileReport(data, title="Initial Dataset Report")
profile.to_file("initial_dataset_report.html")

# Step 4: Analyze Missing Values
print("\nMissing Value Analysis:")
missing_values = data.isnull().sum()
missing_percent = (missing_values / len(data)) * 100
missing_analysis = pd.DataFrame({'Total Missing': missing_values, 'Percentage': missing_percent})
print(missing_analysis)

# Step 5: Visualize Missing Values
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title("Heatmap of Missing Values")
plt.savefig('Heatmap of Missing Values.png') 

# Step 6: Data Distributions (e.g., for numeric columns)
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns].hist(bins=20, figsize=(12, 8), edgecolor='black')
plt.suptitle("Histograms of Numeric Columns")
plt.savefig('Histograms of Numeric Columns.png') 

# Step 7: Categorical Analysis
categorical_columns = data.select_dtypes(include=['object']).columns
for column in categorical_columns:
    plt.figure(figsize=(10, 4))
    sns.countplot(y=data[column], palette="viridis", hue=None)
    plt.title(f"Countplot of {column}")
    plt.savefig('Countplot.png') 

# Step 8: Analyze Unique Values in Columns
for col in data.columns:
    unique_count = data[col].nunique()
    print(f"Column '{col}' has {unique_count} unique values.")

# Handle missing values (example: fill with 0 or mean for numeric columns)
data_cleaned = data.copy()
data_cleaned.fillna(0, inplace=True)

# Creating a new DataFrame with only numeric columns to compute the correlation matrix
numeric_data = data_cleaned.select_dtypes(include='number')
correlation_matrix = numeric_data.corr()
print(correlation_matrix)

# Check for duplicate rows
print("Number of duplicate rows:", data_cleaned.duplicated().sum())

# Drop duplicate rows
data_cleaned.drop_duplicates(inplace=True)

# Save cleaned data to CSV
data_cleaned.to_csv('expenditure_cleaned.csv', index=False)

# Generate the profiling report
profile = ProfileReport(data, title="Expenditure Dataset Report")
profile.to_file("expenditure_report.html")

# Check the data types of each column in the DataFrame
print("Data Types:")
print(data_cleaned.dtypes)

# Select only numeric columns for correlation analysis
numeric_data = data_cleaned.select_dtypes(include=['number'])

# Compute the correlation matrix
correlation_matrix = numeric_data.corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Heatmap for correlation
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig('Correlation Heatmap.png') 

# Count of unique categories in "Exp Category"
print("Unique Expenditure Categories:", data_cleaned['Exp Category'].nunique())

# Countplot for "Exp Category"
plt.figure(figsize=(12, 6))
sns.countplot(y=data[column], palette="viridis", hue=None)
plt.xticks(rotation=90)
plt.title("Exp Category Count")
plt.savefig('Exp Category Count.png') 

# Count of unique states
print("Unique States:", data_cleaned['State'].nunique())

# Countplot for "State"
plt.figure(figsize=(12, 6))
sns.countplot(y=data[column], palette="viridis", hue=None)
plt.xticks(rotation=90)
plt.title("Expenditure by State")
plt.savefig('Expenditure by State.png') 

# Trend Analysis: Expenditure over years for a specific state or category
state_to_analyze = 'ExampleState'  # Replace with a specific state name or keep dynamic
category_to_analyze = 'ExampleCategory'  # Replace with a specific category

# Filter data for the specific state or category
state_data = data_cleaned[data_cleaned['State'] == state_to_analyze]
category_data = data_cleaned[data_cleaned['Exp Category'] == category_to_analyze]

# Line plot for yearly expenditure in the specific state
if not state_data.empty:
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=state_data, x='Year', y='Value', marker='o', label=state_to_analyze)
    plt.title(f"Yearly Expenditure in {state_to_analyze}")
    plt.savefig('Yearly Expenditure in States.png') 
else:
    print(f"No data available for state: {state_to_analyze}")
    
# Line plot for yearly expenditure in the specific category
if not state_data.empty:
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=category_data, x='Year', y='Value', marker='o', label=category_to_analyze)
    plt.title(f"Yearly Expenditure for {category_to_analyze}")
    plt.savefig('Yearly Expenditure.png') 
else:
    print(f"No data available for state: {state_to_analyze}")

# Extra Analysis: Top 5 states contributing to total expenditure
top_states = data_cleaned.groupby('State')['Value'].sum().sort_values(ascending=False).head(5)
print("Top 5 States by Total Expenditure:")
print(top_states)

# Bar plot for top 5 states
plt.figure(figsize=(10, 6))
sns.barplot(x=top_states.index, y=top_states.values, palette="Blues_d")
plt.title("Top 5 States by Total Expenditure")
plt.savefig('Top 5 States by Total Expenditure.png') 

# Extra Analysis: Top 5 expenditure categories
top_categories = data_cleaned.groupby('Exp Category')['Value'].sum().sort_values(ascending=False).head(5)
print("Top 5 Expenditure Categories:")
print(top_categories)

# Bar plot for top 5 expenditure categories
plt.figure(figsize=(10, 6))
sns.barplot(x=top_categories.index, y=top_categories.values, palette="Greens_d")
plt.title("Top 5 Expenditure Categories")
plt.savefig('output_plot_name.png') 

# Save final cleaned and analyzed dataset
data_cleaned.to_csv('expenditure_final_cleaned.csv', index=False)
