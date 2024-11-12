# Import required libraries
import streamlit as st
import pandas as pd
import seaborn as sns
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
        
        # Plotting with Seaborn
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x='sales_date', y='sales_amount')
        plt.title("Sales Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sales Amount")
        st.pyplot(plt)  # Display the plot in Streamlit
        
    else:
        st.warning("Please ensure your data has 'sales_date' and 'sales_amount' columns for sales visualization.")

    # * Customer Segmentation by Region
    st.header("Customer Segmentation")
    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.write("Customer Segmentation")
        
        # Plotting with Seaborn
        plt.figure(figsize=(8, 8))
        region_sales = data.groupby('region')['sales_amount'].sum().reset_index()
        sns.barplot(data=region_sales, x='region', y='sales_amount')
        plt.title("Customer Segmentation by Region")
        plt.xlabel("Region")
        plt.ylabel("Total Sales Amount")
        st.pyplot(plt)
        
    else:
        st.warning("Please ensure your data has a 'region' column for customer segmentation.")

    # * Product Analysis
    st.header("Product Analysis")
    if 'product' in data.columns and 'sales_amount' in data.columns:
        st.write("Top Products by Sales")
        
        # Calculating top products by sales
        top_products_df = data.groupby('product')['sales_amount'].sum().nlargest(10).reset_index()
        
        # Plotting with Seaborn
        plt.figure(figsize=(12, 6))
        sns.barplot(data=top_products_df, x='product', y='sales_amount')
        plt.title("Top Products By Sales")
        plt.xlabel("Product")
        plt.ylabel("Sales Amount")
        st.pyplot(plt)
        
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
