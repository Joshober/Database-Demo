
try:
    import subprocess


    def install_library(library_name):
        try:
            __import__(library_name)
        except ImportError:
            print(f"The '{library_name}' library is not installed. Installing...")
            subprocess.check_call(["pip", "install", library_name])
            print(f"The '{library_name}' library has been installed.")


    # Usage:
    install_library("pandas")
    install_library("pandasgui")
    install_library("sqlite3")
    import os
    import pandas as pd
    import sqlite3
    import pandasgui

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "search.db")

    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()

    # Fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    table_names = cursor.fetchall()


    def MakeTables():
        # Iterate over table names and read each table into a DataFrame
        dataframes = {}
        for table_name in table_names:
            query = f"SELECT * FROM {table_name[0]}"
            dataframes[table_name[0]] = pd.read_sql(query, connection)
        return dataframes


    def OnebyOne(dataframes):
        for table_name, dataframe in dataframes.items():
            pandasgui.show(dataframe)


    # Show tables all in the same
    pandasgui.show(**MakeTables())

    # Show tables one at a time
    # OnebyOne(MakeTables())
    input("Enter any key to Exit")
    connection.close()
except Exception as e:
    print("An error occurred:", e)
    input("Press Enter to exit...")