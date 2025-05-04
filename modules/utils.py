import modules.config as config
import pandas as pd
import os

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

def check_for_duplicates_by_key_word(df, key_word):
    # Check for duplicates in the specified column
    for column_name in df.columns:
        if key_word.lower() in column_name.lower():
            return df[column_name].duplicated().sum()
        
    return 'No such column found'
