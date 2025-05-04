import streamlit as st
import pandas as pd
import modules.data_processing as dp
import pages.page1 as p1
import pages.page2 as p2




# Configure your app's layout
st.set_page_config(
    page_title="Multi-Page Streamlit App",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Home", "Page 1", "Page 2"])

# # Home Page
# if page == "Home":
#     st.title("Welcome to the Multi-Page App")
#     st.write("Select a page from the sidebar to begin.")

# # Page 1
# elif page == "Page 1":
#     st.title("Page 1")
#     st.write("DataFrame from `data.py`:")
#     st.dataframe(data.df1)

# # Page 2
# elif page == "Page 2":
#     st.title("Page 2")
#     st.write("Combined Data:")
#     combined_df = data.get_combined_data()
#     st.dataframe(combined_df)


