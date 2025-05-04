import streamlit as st
import pandas as pd 
import modules.data_processing as dp


def app():
    st.title("Happiness Comparator")
    st.subheader("Data Processing")
    
    # Display the dataframe
    st.write("Dataframe:")
    st.dataframe(dp.df.head())


if __name__ == "__main__":
    app()