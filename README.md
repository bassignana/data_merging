# data_merging

The task is simple, in the folder DATASET there are two sub folders, 'diabetes-subset' and 'healthy-subjects'.
Inside them thare are folders numerated with ids i.e. everything present in folder 002 is related to personal id = 2.
For every id i need to create a single dataframe, containing all columns that are present in the files: glucose.csv, insulin.csv, date-time_Accel.csv, date-time_BB.csv, date-time_Breathing.csv, date-time_ECG.csv, date-time_RR.csv, date-time_Summary.csv.
Once i've created all merged dataframes, they must be saved as csv "idnumber.csv" and stored in a dictionary like { '001':df1, '002':df2, ...}


This single dataframe must be merged on the date+time columns: every csv has a date+time information, but in the single merged df, i want a single date-time column. Since for a single timestamp not all information will be available, the column merged without information needs to be filled with nans


The process must be recursive, if i have 4 ids or 40, it should scale just fine.
