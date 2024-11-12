# Import required libraries
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


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
        fig = go.Figure(data=go.Scatter(x=data['sales_date'], y=data['sales_amount'], mode='lines'))
        fig.update_layout(title="Sales Over Time", xaxis_title="Date", yaxis_title="Sales Amount")
        st.plotly_chart(fig)
    else:
        st.warning("Please ensure your data has 'sales_date' and 'sales_amount' columns for sales visualization.")

    # * Customer Segmentation by Region
    st.header("Customer Segmentation")
    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.write("Customer Segmentation")
        fig = go.Figure(data=go.Pie(labels=data['region'], values=data['sales_amount']))
        fig.update_layout(title="Customer Segmentation by Region")
        st.plotly_chart(fig)
    else:
        st.warning("Please ensure your data has a 'region' column for customer segmentation.")

    # * Product Analysis
    st.header("Product Analysis")
    if 'product' in data.columns and 'sales_amount' in data.columns:
        st.write("Top Products by Sales")
        
        top_products_df = data.groupby('product').sum('sales_amount').nlargest(10, 'sales_amount')
        
        fig = go.Figure(data=go.Bar(x=top_products_df.index, y=top_products_df['sales_amount']))
        fig.update_layout(title="Top Products By Sales", xaxis_title="Product", yaxis_title="Sales Amount")
        
        st.plotly_chart(fig)
        
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
