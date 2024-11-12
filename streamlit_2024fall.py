# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1.0 Title and Introduction
st.title("Business Dashboard")
st.write("""
This dashboard provides insights into sales, customer demographics, and product performance. Upload your data to get started.
""")

# 2.0 Data Input
st.header("Upload Business Data")
uploaded_file = st.file_uploader("Choose a CSV File", type="csv", accept_multiple_files=False)

# 3.0 App Body 
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of the Uploaded Data:")
    st.write(data.head())

    # * Sales insights
    st.header("Sales Insights")
    if 'sales_date' in data.columns and 'sales_amount' in data.columns: 
        st.write("Sales Over Time")
        
        # Plotting with Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(data['sales_date'], data['sales_amount'], marker='o', linestyle='-')
        ax.set_title("Sales Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales Amount")
        st.pyplot(fig)
        
    else:
        st.warning("Please ensure your data has 'sales_date' and 'sales_amount' columns for sales visualization.")

    # * Customer Segmentation by Region
    st.header("Customer Segmentation")
    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.write("Customer Segmentation")
        
        # Plotting with Matplotlib
        fig, ax = plt.subplots(figsize=(8, 8))
        region_sales = data.groupby('region')['sales_amount'].sum()
        ax.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=90)
        ax.set_title("Customer Segmentation by Region")
        st.pyplot(fig)
        
    else:
        st.warning("Please ensure your data has a 'region' column for customer segmentation.")

    # * Product Analysis
    st.header("Product Analysis")
    if 'product' in data.columns and 'sales_amount' in data.columns:
        st.write("Top Products by Sales")
        
        # Calculating top products by sales
        top_products_df = data.groupby('product')['sales_amount'].sum().nlargest(10)
        
        # Plotting with Matplotlib
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(top_products_df.index, top_products_df.values)
        ax.set_title("Top Products By Sales")
        ax.set_xlabel("Product")
        ax.set_ylabel("Sales Amount")
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
    else:
        st.warning("Please ensure your data has 'product' and 'sales_amount' columns for product analysis.")

    # * Feedback Form
    st.header("Feedback (Your Opinion Counts)")
    feedback = st.text_area("Please provide any feedback or suggestions.")
    if st.button("Submit Feedback"):
        st.success('Thank you for your feedback.')

# 4.0 Footer
st.write("---")
st.write("This business dashboard template is flexible. Expand upon it based on your specific business needs.")

if __name__ == "__main__":
    pass
