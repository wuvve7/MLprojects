import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Employee Name': ['Ahmed', 'Sara', 'Mariam', 'Ali', 'Fatima', 'Mohammed', 'Yusuf', 'Nora'],
    'Age': [25, 30, 28, 35, 40, 22, 27, 33],
    'Salary': [5000, 6000, 5500, 7000, 8000, 4500, 6500, 7500],
    'Department': ['Marketing', 'HR', 'Development', 'Marketing', 'Finance', 'Development', 'HR', 'Finance']
}

df = pd.DataFrame(data)

def clean_data(df):
    df.fillna(method='ffill', inplace=True)
    df = df[df['Salary'] <= 10000]
    return df

df = clean_data(df)

def basic_analysis(df):
    average_salary = df['Salary'].mean()
    max_salary = df['Salary'].max()
    min_salary = df['Salary'].min()
    median_salary = df['Salary'].median()
    print(f"Average Salary: {average_salary}")
    print(f"Max Salary: {max_salary}")
    print(f"Min Salary: {min_salary}")
    print(f"Median Salary: {median_salary}")
    department_avg_salary = df.groupby('Department')['Salary'].mean()
    print("\nAverage Salary by Department:")
    print(department_avg_salary)
basic_analysis(df)

def plot_data(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Salary'], kde=True, color='blue')
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.show()

    sns.scatterplot(x='Age', y='Salary', data=df, hue='Department', palette='Set1')
    plt.title('Age vs Salary')
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.show()

plot_data(df)
