import streamlit as st
import pandas as pd 
import modules.data_processing as dp


def app():
    st.title("Happiness Comparator2")
    st.subheader("Data Processing2")
    
    # Display the dataframe
    st.write("Dataframe2:")
    st.dataframe(dp.df.head())


if __name__ == "__main__":
    app()