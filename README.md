# 🌍 World Happiness Dashboard

Hello!

This is an exploration app for happiness scores across the world.

## Set-up

- Fork the repo of the app from the following link: https://github.com/aptsvetanov24/pa-tech-lead-recr-task, or download the whole project on your local machine

- If you've forked the repo in your own GitHub account, open terminal/CMD on your local machine and navigate to the directory where you want to clone the repo, then write "git clone [link to the forked repo from your GitHub account]"

- Once you have all the app files on your local machine, you should create your virtual enviroment and install the libraries needed for the source code

- After you navigate to your app directory, create your virtual enviroment: "python -m venv env" (env is the name of the venv)

- Then you should activate the venv: ".\env\Scripts\activate". This should run the .\env\Scripts\activate.ps1 script and activate your env. However if you encounter any issues with the activation you can try "Set-ExecutionPolicy Unrestricted -Scope Process" and then again ".\env\Scripts\activate"

- Once you've activated your venv you should install the libraries used in the source code (also available in the requirements.txt file):
pandas==2.2.3
streamlit==1.45.0
st-pages==1.0.1
seaborn==0.13.2
matplotlib==3.10.1

- When all the points from above are done you can run the app with the following command "streamlit run .\happiness_comparator.py"

## App overview

- On the left side on your screen there is a navigation pane containing all 3 pages included in the app.

- "Happiness accross the world" is table containing columns such as year, country, happiness score etc. This table could be filtered by Year, Country and Region. You can also get the top/bottom N rows (ranked by happiness score) or just show all available rows (according to the filters above the table) by checking the "All rows" checkbox.

- "Happiness correlation" is scatter plot of happiness score vs one of the components health, freedom, generosity. When you select your filters from the first row, just below them you can see the most influlential component for the happiness score. And when you select one of the 3 components, scatter plot will be updated based on your 3 filters.

- "Happiness trends" is the last page that shows the happines trend through the years for all selected countries from the drop down menu above the plot.

## Code overview

1. **Main file** happiness_comparator.py contains only reference to the pages (from folder "pages") and their labels and icons in file ".streamlit/pages.toml".

2. **Folder ".streamlit"** contains .toml files:
   - "pages.toml" contains the path, name (title), and icon for each page.
   - "config.toml" contains the default colors and fonts of the pages.

3. **Folder "data"** contains the raw data (5 csv files for years 2015 ti 2019)

4. **Folder "modules** contains 3 python scripts:
   - "data_processing.py" loads and cleans the data before it is used in the app.
   - "config.py" contains some arguments used in other python scripts (utils.py and all the pages scripts).
   - "utils.py" contains functions used in the "data_processing.py" and all 3 pages scripts. 

5. **Folder "pages** contains all 3 pages scripts:
   - "page1.py" contains 3 drop down menus (selectbox) for Year, Country and Region data filtering. Also radio buttons for switchih between top/bottom scores, and "Maximum number of rows" field (number_input) which is active only if the "All rows" is not checked. The data is refreshed each time any of the 6 components is changed by the user via "refresh_data" from "modules/utils.py".

   - "page2.py" contains the same 3 drop downs as "page1.py". When filter is changed (again via "refresh_data" from "modules/utils.py") the text next to "Most influential for happiness based on the filters above is:" is updated.
   The scatter plot at the bottom is also updated the same way but also considering the components drop down menu above the plot (the one under "Happiness Score correlation with:").

   - "page3.py" contains one drop down with multiple selection (multiselect) and based on the selection the trends plot is updated via "plot_happiness_trends"  from "modules/utils.py".


## Other comments
I've tried to download "Docker Desktop" however I need admin access to my computer so I've written what I understood from reading some forums, and the content might be lame :D



