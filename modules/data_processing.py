import pandas as pd
import modules.config as config
import modules.utils as utils



###############################################################
###         1. DATA PROCESSING   (Load and clean)           ###
###############################################################
# Set the columns existing in all the dataframes
existing_columns = config.ALL_COLUMNS
final_columns = config.FINAL_COLUMNS

#   Load the data from the CSV files
happiness_data = utils.load_data()

#  Iterate through the dfs in the dictionary
counter = 0
for key in happiness_data.keys():
    # Set the year column using the name of the files as key
    happiness_data[key]['Year'] = key

    # Rename the columns in the dataframe using the key word
    for col in existing_columns:
        happiness_data[key] = utils.rename_column_by_key_word(happiness_data[key], col)


    if counter == 0:
        # Set the first dataframe as the base for the final dataframe
        # Remove duplicate countries from the first dataframe
        unique_df1 = happiness_data[key].drop_duplicates(subset='Country')
    elif counter == 1:
        # Set the first dataframe as the base for the final dataframe
        # Remove duplicate countries from the second dataframe
        unique_df2 = happiness_data[key].drop_duplicates(subset='Country')
        # Concatenate 1st and 2nd dfs and remove duplicate countries from the concatenated dataframe
        tmp_df = pd.concat([unique_df1, unique_df2])
        unique_df = tmp_df.drop_duplicates(subset='Country')
        # Create dictionary with unique countries as keys and regions as values
        country_region_dict = unique_df.set_index('Country')['Region'].to_dict()
    else:
        # Add region column to the dfs without region column
        happiness_data[key]['Region'] = happiness_data[key]['Country'].map(country_region_dict)
        happiness_data[key] = utils.rename_column_by_key_word(happiness_data[key], 'Region')
            
    counter += 1

# Concatenate all dataframes into one and drop cases without region or country  
df = pd.concat([df_current[existing_columns] for df_current in happiness_data.values()])
df = df[df['Country'].notna() & df['Region'].notna()]
df = utils.rename_column_by_key_word_with_new_name(df, 'Rank', 'Rank per year')
df = utils.rename_column_by_key_word_with_new_name(df, 'Score', 'Happiness Score')
df['Rank'] = df['Happiness Score'].rank(ascending=False, method='dense')
df = df[final_columns]