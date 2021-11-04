import os
import datetime as dt
import numpy as np
import pandas as pd

gluco_files = []
for subdir, dirs, files in os.walk('/Volumes/TOSHIBA EXT/D1NAMO'):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith("insulin.csv"):
            gluco_files.append(filepath)

print('Number of glucose files:', len(gluco_files))


#glucose
for i,file in enumerate(gluco_files):
    df = pd.read_csv(file)
    print(i)
    df['date'] = df['date'].replace(' ', '')
    df['time'] = df['time'].replace(' ', '')
    d = pd.to_datetime(df['date']).dt.date
    t = pd.to_datetime(df['time']).dt.time
    a = []
    for d, t in zip(d, t):
        a.append(dt.datetime.combine(d, t))
    df['dt'] = a
    df.drop(columns=['date', 'time', 'comments'], inplace=True)
    df.rename({'glucose':'bg', 'type':'bg_type'}, inplace=True)

#insuline
for i in gluco_files:
    df = pd.read_csv(file)
    print(i)
    df['date'] = df['date'].replace(' ', '')
    df['time'] = df['time'].replace(' ', '')
    d = pd.to_datetime(df['date']).dt.date
    t = pd.to_datetime(df['time']).dt.time
    a = []
    for d, t in zip(d, t):
        a.append(dt.datetime.combine(d, t))
    df['dt'] = a
    df.drop(columns=['date', 'time', 'comments'], inplace=True)
    df.rename({'fast_insulin':'fin', 'slow_insulin':'sin'}, inplace=True)


files = []
for subdir, dirs, files in os.walk('/Volumes/TOSHIBA EXT/D1NAMO/diabetes_subset/001/sensor_data'):
    for file in files:
        #print (os.path.join(subdir, file))
        filepath = subdir + os.sep + file

        if filepath.endswith("Accel.csv"):
            files.append(filepath)

print('Number of glucose files:', len(files))


files = []
directory = '/Volumes/TOSHIBA EXT/D1NAMO/diabetes_subset/001/sensor_data'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if f.endswith('DS_Store'):
        pass
    else:
        for csv in os.listdir(f):
            if csv.endswith("Accel.csv"):
                files.append(f + os.sep + csv)


df = pd.read_csv(files[0])
df = df.iloc[:100,:]
df['dt'] = pd.to_datetime(df['Time']) # todo remove microseconds
df.drop(columns=['Time'], inplace=True)









df = gluco_files[9]
df = pd.read_csv(df)

d = pd.to_datetime(df['date']).dt.date
t = pd.to_datetime(df['time']).dt.time
a = []
for d, t in zip(d,t):
    a.append(dt.datetime.combine(d,t))
df['dt'] = a

dt.datetime.combine(, )
df['time'] = df['time'].astype(str)
df.dtypes
df['time'] = np.where(len(df['time']) == 5, df['time'] + ':00', df['time'])
for v in df['time'].values:
    print(len(v))

