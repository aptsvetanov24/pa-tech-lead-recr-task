import modules.config as config
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

###############################################################
###         1. DATA PROCESSING   (Load and clean)           ###
###############################################################
def load_data():
    # Load the data from the CSV files
    csv_files = [f for f in os.listdir(config.DATA_PATH) if f.endswith('.csv')]

    dataframes_dict = {}

    # Read each CSV file into a DataFrame and store it in the dictionary
    for file in csv_files:
        file_path = os.path.join(config.DATA_PATH, file)
        df_name = file.split('.')[0]  # Use the file name without the extension as the dictionary key
        dataframes_dict[df_name] = pd.read_csv(file_path)

    return dataframes_dict

def rename_column_by_key_word(df, key_word):
    # Rename columns that contain the key word
    for column_name in df.columns:
        if key_word.lower() in column_name.lower():
            new_column_name = f"{key_word}"
            df.rename(columns={column_name: new_column_name}, inplace=True)
            return df
    # print(f"No column found with the key word '{key_word}'")    
    return df

def rename_column_by_key_word_with_new_name(df, key_word, new_name):
    # Rename columns that contain the key word
    for column_name in df.columns:
        if key_word.lower() in column_name.lower():
            new_column_name = f"{new_name}"
            df.rename(columns={column_name: new_column_name}, inplace=True)
            return df
    # print(f"No column found with the key word '{key_word}'")    
    return df

def check_for_duplicates_by_key_word(df, key_word):
    # Check for duplicates in the specified column
    for column_name in df.columns:
        if key_word.lower() in column_name.lower():
            return df[column_name].duplicated().sum()
        
    return 'No such column found'

###############################################################
###         2. DATA VISUALISATION                           ###
###############################################################

def filter_data(df, 
                selected_country = "All",
                selected_year = "All", 
                selected_region = "All", 
                rank_column = 'Rank', 
                score_column = config.HAPPINESS_COLUMN,
                update_rank = True):
    
    df = df[((df['Country'] == selected_country) if selected_country != "All" else df['Country'].notna()) &
            ((df['Year'] == selected_year) if selected_year != "All" else df['Year'].notna()) &
            ((df['Region'] == selected_region) if selected_region != "All" else df['Region'].notna())]
    
    if update_rank: df[rank_column] = df[score_column].rank(ascending=False, method='dense')

    return df


def sort_dataframe(df, max_rows = 10, option = 'Top', 
                   score_column = config.HAPPINESS_COLUMN, 
                   show_all = False):
    # Sort the DataFrame based on the selected column and order
    if option == 'Top':
        df = df.sort_values(by=score_column, ascending=False).head(max_rows if not show_all else df.shape[0])
    elif option == 'Bottom':
        df = df.sort_values(by=score_column, ascending=True).head(max_rows if not show_all else df.shape[0])
    
    return df


def refresh_data(df, 
                selected_country = "All",
                selected_year = "2019", 
                selected_region = "All", 
                rank_column = 'Rank',
                score_column = config.HAPPINESS_COLUMN,
                max_rows = 10,
                option = 'Top',
                show_all = False,
                update_rank = True,
                update_sort = True):
    
    result = filter_data(df, selected_country, selected_year, selected_region, rank_column, score_column, update_rank)
    if update_sort: result = sort_dataframe(result, max_rows = max_rows, option = option, score_column = score_column, show_all = show_all)
    return result

def get_most_influential_compoment(df, components = config.CORRELATION_COLUMNS):
    # Calculate the correlation matrix
    corr = df[[config.HAPPINESS_COLUMN] + config.CORRELATION_COLUMNS].corr()

    # Get the correlation of the component with Happiness Score
    component_corr = corr[config.HAPPINESS_COLUMN][components]

    # Sort the components by their correlation with Happiness Score
    sorted_components = component_corr.sort_values(ascending=False)

    # Get the most influential component
    most_influential_component = sorted_components.index[0]

    return most_influential_component

def plot_correlation_matrix(df, component, figsize=(8, 6)):

    # Set up the matplotlib figure
    plt.figure(figsize=figsize)

    # Create a scatter plot for Happiness Score vs Health
    sns.scatterplot(data=df[[config.HAPPINESS_COLUMN,component]], x=component, y=config.HAPPINESS_COLUMN)

    # Customize the plot with titles and layout
    plt.title(component+' vs. '+config.HAPPINESS_COLUMN)
    plt.xlabel(component)
    plt.ylabel(config.HAPPINESS_COLUMN)
    plt.grid(True)

    return plt