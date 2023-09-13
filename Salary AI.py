import numpy as np
import seaborn as sns
import altair as alt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load the dataset
@st.cache_data  # Cache the function to enhance performance
def load_data():
    # Define the file path
    file_path = 'G:\My Drive\Markus\VSCode Projects\BDS Projects\salaries.csv'
    
    # Load the CSV file into a pandas dataframe
    df = pd.read_csv(file_path)

    # Create age groups and add as a new column
    bin_edges = [1, 50001, 75001, 100001, 125001, 150001]
    bin_labels = ['50k or less', '50k-75k', '75k-100k', '100k-125k', '125k-150k',]
    df['SalaryLevel'] = pd.cut(df['salary'], bins=bin_edges, labels=bin_labels, right=False)

    return df

# Load the data using the defined function
df = load_data()

# Set the app title and sidebar header
st.title("Employee Salary Dashboard 😊📈")
st.sidebar.header("Amazing Filters 📊")

# Introduction

# HR Attrition Dashboard
st.markdown("""
            Welcome to the Employee Salary Dashboard.
""")
with st.expander("📊 **Objective**"):
                 st.markdown("""
At the heart of this dashboard is the mission to visually decode data in order to assist with gaining better insights in salary distribution for various categories, such as different levels of experience and job types related to developing AI. How exciting!
"""
)

# Sidebar filter: Salary Level
selected_salary_level = st.sidebar.multiselect("Select Salary Level 🕰️", df['SalaryLevel'].unique().tolist(), default=df['SalaryLevel'].unique().tolist())
if not selected_salary_level:
    st.warning("Please select a salary level from the sidebar ⚠️")
    st.stop()
filtered_df = df[df['salary'].isin(selected_salary_level)]

# Sidebar filter: Experience Level
experience_level = df['experience_level'].unique().tolist()
selected_experience_level = st.sidebar.multiselect("Select Experience Level 🏢", experience_level, default=experience_level)
if not selected_experience_level:
    st.warning("Please select a experince level from the sidebar ⚠️")
    st.stop()
filtered_df = filtered_df[filtered_df['experience_level'].isin(selected_experience_level)]

# Sidebar filter: Employment Type
employment_type = df['employment_type'].unique().tolist()
selected_employment_type = st.sidebar.multiselect("Select Employment Type 🏢", employment_type, default=employment_type)
if not selected_employment_type:
    st.warning("Please select a employment type from the sidebar ⚠️")
    st.stop()
filtered_df = filtered_df[filtered_df['employment_type'].isin(employment_type)]

st.header('Analysis of AI-Salary📊')

#Dropdown box
visualization_option = st.selectbox(
      "Try and select, it might work!🤥",
      ["Salary by ExperienceLevel",
       "Salary by ExperienceLevel",
       "Salary by CompanySize"]
)

#chart1
st.header("Salary vs Experience Level")
plt.figure(figsize=(10, 6))
sns.boxplot(x='experience_level', y='salary_in_usd', data=df)
plt.title("Salary vs Experience Level")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

#chart2
st.header("Salary by Experience Level")
plt.figure(figsize=(10, 6))
sns.countplot(x='SalaryLevel', hue='experience_level', data=df)
plt.title("Salary Level by Experience Level")
st.pyplot()

#chart3
chart_option = st.selectbox("Choose Chart", ['Salary by Company Size', 'Experience Level by Company Size'])
if chart_option == 'Salary by Company Size':
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='company_size', y='salary_in_usd', data=df)
    plt.title("Salary by Company Size")
else:
    plt.figure(figsize=(10, 6))
    sns.countplot(x='company_size', hue='experience_level', data=df, )
    plt.title("Experience Level by Company Size")
st.pyplot()

st.image("https://en.meming.world/images/en/b/be/But_It%27s_Honest_Work.jpg")
