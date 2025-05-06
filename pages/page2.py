import streamlit as st
import modules.utils as utils
import modules.config as config
import modules.data_processing as dp



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
            options = ['All'] + sorted(df['Country'].unique().tolist()),
            help = "Select a country to filter the data",
            index = 0  # Default value All
        )

    # Drop-down menu for region
    with col3:
        selected_region = st.selectbox(
            "Region:",
            options = ['All'] + sorted(df['Region'].unique().tolist()),
            help = "Select a region to filter the data",
            index = 0  # Default value All
        )

    ### ---------------  Create field form most influential compoment vizualization
    
    row2_col1, row2_col2 = st.columns([3, 1])
    with row2_col1:
        st.text("Most influential for happiness based on the filters above is:")
    
    with row2_col2:
        st.text(utils.get_most_influential_compoment(utils.refresh_data(df_viz, 
                                                        selected_country, 
                                                        selected_year, 
                                                        selected_region, 
                                                        update_rank=False,
                                                        update_sort=False)))


    ### ---------------  Create drop-down menu for components 
    selected_component = st.selectbox(
            "Happiness Score correlation with:",
            options = config.CORRELATION_COLUMNS,
            help = "Select a component to plot the correlation with Happiness Score",
            index = 0  # Default value Health
        )
    ### ---------------  Plot correlations between columns
    st.pyplot(utils.plot_correlation_matrix(utils.refresh_data(df_viz, 
                                                        selected_country, 
                                                        selected_year, 
                                                        selected_region, 
                                                        update_rank=False,
                                                        update_sort=False), 
                                                    selected_component,
                                                    figsize=config.FIGSIZE))
 

if __name__ == "__main__":
    app()