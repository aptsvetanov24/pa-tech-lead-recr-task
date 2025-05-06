import modules.config as config
import pandas as pd
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

def update_rank_column(df, 
                       selected_country = "All",
                       selected_year = "All", 
                       selected_region = "All", 
                       rank_column = 'Rank',
                       score_column = 'Happiness Score'):
    
    df = df[((df['Country'] == selected_country) if selected_country != "All" else df['Country'].notna()) &
            ((df['Year'] == selected_year) if selected_year != "All" else df['Year'].notna()) &
            ((df['Region'] == selected_region) if selected_region != "All" else df['Region'].notna())]
    
    df[rank_column] = df[score_column].rank(ascending=False, method='dense')
    return df


def sort_dataframe(df, max_rows = 10, option = 'Top', 
                   score_column = 'Happiness Score', 
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
                score_column = 'Happiness Score',
                max_rows = 10,
                option = 'Top',
                show_all = False):
    
    result = update_rank_column(df, selected_country, selected_year, selected_region, rank_column, score_column)
    result = sort_dataframe(result, max_rows = max_rows, option = option, score_column = score_column, show_all = show_all)
    return result

