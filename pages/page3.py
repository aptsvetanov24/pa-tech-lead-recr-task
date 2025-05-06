import streamlit as st
import modules.utils as utils
import modules.config as config
import modules.data_processing as dp


def app():
    ### ---------------  Load the dataframe
    df = dp.df
    df_viz = df

    ### ---------------  Create drop-down menus for filtering
    # Drop-down menu for countries
    selected_countries = st.multiselect(
        "Countries:",
        options = sorted(df['Country'].unique().tolist()),
        help = "Select the countires you want to see the happiness trends for",
        default = ['Bulgaria','Brazil','Finland','Ghana','Jamaica','Japan','Russia','United States'] # Default countries
    )

    
    # Display the plot in Streamlit
    st.pyplot(utils.plot_happiness_trends(df_viz, selected_countries, figsize=config.FIGSIZE))
    
if __name__ == "__main__":
    app()