# Import required libraries
import pandas as pd
import seaborn as sns
import ydata_profiling as prf
import matplotlib
matplotlib.use("TkAgg")  # Set interactive backend
import matplotlib.pyplot as plt

# Load dataset
expenditure = pd.read_csv("D:\Aptech\Python\ExpenditureDB\Final_expenditure.csv")

# Generate an initial profile report
expenditure_profile = prf.ProfileReport(expenditure)
expenditure_profile.to_file(output_file="expenditure_before_preprocessing.html")

# Check for missing values
missing_values = expenditure.isnull().sum()
missing_percent = (missing_values / len(expenditure)) * 100

# Display missing values summary
missing_summary = pd.concat([missing_values, missing_percent], axis=1, keys=['Total', 'Missing %'])
print("Missing Values Summary:")
print(missing_summary)

# Visualize missing data with a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(expenditure.isnull(), cbar=False, cmap="viridis", yticklabels=False)
plt.title("Heatmap of Missing Values")
plt.show()

# Create a copy of the dataset before preprocessing
exp_data = expenditure.copy()

# Fill missing values with 0 (or any strategy of your choice)
exp_data.fillna(0, inplace=True)

# Check for duplicate rows
print("Number of duplicate rows before cleaning:", exp_data.duplicated().sum())
exp_data.drop_duplicates(inplace=True)
print("Number of duplicate rows after cleaning:", exp_data.duplicated().sum())

# Check the size of the cleaned dataset
print("Shape of cleaned dataset:", exp_data.shape)

# Save the cleaned dataset and profile report
exp_clean_profile = prf.ProfileReport(exp_data)
exp_clean_profile.to_file(output_file="expenditure_after_preprocessing.html")
exp_data.to_csv('expenditure_cleaned.csv', index=False)

# ---- DATA ANALYSIS ---- #

# Ensure only numerical columns are used for the correlation matrix
numerical_columns = exp_data.select_dtypes(include=['number'])
correlation_matrix = numerical_columns.corr()

print("Correlation Matrix:")
print(correlation_matrix)

# Visualize the correlation matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Save the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.savefig("correlation_matrix_heatmap.png")  # Save to file
plt.close()  # Close the figure

# Example for other plots:
sns.countplot(exp_data['Exp Category'])
plt.figure(figsize=(14, 8))
plt.xticks(rotation=90)
plt.title("Expenditure Categories Countplot")
plt.savefig("expenditure_categories_countplot.png")
plt.close()

# 2. Count and visualize unique categories in 'Exp Category'
print("Number of unique expenditure categories:", exp_data['Exp Category'].nunique())
plt.figure(figsize=(12, 6))
sns.countplot(data=exp_data, x='Exp Category', order=exp_data['Exp Category'].value_counts().index)
plt.title("Countplot of Expenditure Categories")
plt.xticks(rotation=90)
plt.show()

# 3. Count and visualize unique states in 'State'
print("Number of unique states:", exp_data['State'].nunique())
plt.figure(figsize=(12, 6))
sns.countplot(data=exp_data, x='State', order=exp_data['State'].value_counts().index)
plt.title("Countplot of States")
plt.xticks(rotation=90)
plt.show()

# Save the cleaned dataset
exp_data.to_csv('expenditure_processed.csv', index=False)
