import streamlit as st
import modules.data_processing as dp
import modules.utils as utils
import modules.config as config



def app():
    ### ---------------  Load the dataframe
    df = dp.df
    df_viz = df

    ### ---------------  Create drop-down menus for filtering
    # Create three columns
    col1, col2, col3 = st.columns([1, 2, 3])

    # Drop-down menu for year
    with col1:
        selected_year = st.selectbox(
            "Year:",
            options = ['All'] + df['Year'].unique().tolist(),
            help = "Select a year to filter the data",
            index = 5  # Default value 2019
        )

    # Drop-down menu for country
    with col2:
        selected_country = st.selectbox(
            "Country:",
            options = ['All'] + df['Country'].unique().tolist(),
            help = "Select a country to filter the data",
            index = 0  # Default value All
        )

    # Drop-down menu for region
    with col3:
        selected_region = st.selectbox(
            "Region:",
            options = ['All'] + df['Region'].unique().tolist(),
            help = "Select a region to filter the data",
            index = 0  # Default value All
        )

    ### --------------- Sort the DataFrame based on the selected column and order
    row2_col1, row2_col2, row2_col3 = st.columns([3, 1, 2])

    #disable/enable user input for number of rows
    with row2_col2:
        disable_input = st.checkbox("All rows",
                                    value=False,
                                    help="Check to display all rows",)  

    # User input for number of rows 
    with row2_col3:
        max_rows = st.number_input("Maximum number of rows", 
                                   min_value=1, max_value=df_viz.shape[0], 
                                   value=config.MAX_ROWS if not disable_input else df_viz.shape[0], step=1,
                                   help="Select the maximum number of rows to display",)
        
    # Radio button to choose between top or bottom N rows
    with row2_col1:
        option = st.radio(
            f"Top/Bottom Happiness Score:",
            ('Top', 'Bottom'),
            horizontal=True,
            help="Select whether to display the top or bottom N rows based on the Happiness Score",
        )



    # ---------------  Display DataFrame
    st.dataframe(utils.refresh_data(df_viz, 
                                    selected_country, 
                                    selected_year, 
                                    selected_region, 
                                    option=option,
                                    max_rows=max_rows,
                                    show_all=disable_input))
    

    
if __name__ == "__main__":
    app()