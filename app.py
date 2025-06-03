import streamlit as st
import pandas as pd

# Page Title
st.title("🍕 Food Orders Dashboard")
st.subheader("View and Filter Orders from CSV")

# Sidebar - Upload CSV
st.sidebar.header("Upload Your CSV File")
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Show Data if File is Uploaded
if file:
    data = pd.read_csv(file)
    
    # Show Full Data
    st.write("### All Orders")
    st.dataframe(data)

    # Sidebar - Filter by City
    cities = st.sidebar.multiselect("Filter by City", data['City'].unique())
    if cities:
        data = data[data['City'].isin(cities)]
        st.write("### Filtered Orders")
        st.dataframe(data)

    # Summary
    total_orders = data['OrderID'].nunique()
    total_revenue = (data['Price'] * data['Quantity']).sum()

    st.write("### Summary")
    st.write("Total Orders:", total_orders)
    st.write("Total Revenue:", total_revenue)