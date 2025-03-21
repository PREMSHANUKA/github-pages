#-*- coding: utf-8 -*-
import csv
import pandas as pd


# step a: List of stations name
stations = ["ML0003","ML0037","ML0009"]

#step b: Initialise the counter 
rowN = 0

#step c: Clear projetc_data.csv by opening it in writing mode
with open("project_data.csv", "w") as file:
    pass

#step d: Loop through years and quarters
for i in range(2014, 2020):
    for j in range(1, 5):
        filename = f"{i}-Q{j}-Central.csv"
        # step f: Check the existence of the file before processing
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row[1] in stations: #Verify the station's relevence
                        row[0] = f"{i}Q{j}" # Modify the first column to reflect the quarter of the year
                        out_row = [rowN] + row #Add rowN as the first column
                        rowN += 1
                        with open("project_data.csv", "a", newline="") as outfile:
                            writer = csv.writer(outfile)
                            writer.writerow(out_row)
        except FileNotFoundError:
            print(f"File {filename} not found...")

#step h: Define the column
col = ["Quarter", "Station", "Date", "Weather", "Time", "Day", "Drop1", "Direction", "Drop2", "Mode", "Count"]

#step i: Open a Pandas Dataframe and read project_data.csv
dataframe = pd.read_csv("project_data.csv", names=col)

#step j: Clean the data frame 
dataframe.drop(columns=["Drop1", "Drop2"], inplace=True)
dataframe["Full_time"] = dataframe["Date"] + " " + dataframe["Time"]

#step k: Sace the cleaned data to excel file
dataframe.to_excel("CycleData.xlsx", sheet_name="Sheet1", index=False)
