from sklearn.preprocessing import OneHotEncoder

import pandas as pd
import numpy as np

def remove_symbol(time):
    if 'h' in time:
        time = time.split('h')
        return int(time[0])
    else:
        return 0

def remove_symbol_2(time):
    if 'm' in time:
        tempo = time.split()
        time = tempo[-1].strip('m').strip()
        return int(time)
    else:
        return 0



def dataset_cleaner(df: pd.DataFrame):

    df['Total_Stops'] = df['total_stops'].map({'non-stop': 0, '2 stops': 2, '1 stop': 1, '3 stops': 3, '4 stops': 4})
    # Separating date of journey in month and day
    df['Journey_day'] = df['date_of_journey'].dt.day
    df['Journey_month'] = df['date_of_journey'].dt.month

    # Separating depature time in hour and minutes
    df['Dep_hour'] = pd.to_datetime(df['dep_time'], format='%H:%M').dt.hour
    df['Dep_minute'] = pd.to_datetime(df['dep_time'], format='%H:%M').dt.minute

     # Separating the arrival time in hour and minutes
    df['Arrival_hour'] = pd.to_datetime(df['arrival_time']).dt.hour
    df['Arrival_minute'] = pd.to_datetime(df['arrival_time']).dt.minute

    # Applaying remove symbol function to remove the 'h' from the hour 
    # Saving the hour in a new colunm
    df['Duration_hour'] = df['duration'].apply(remove_symbol)

    # Applying remove symbol 2 to remove the 'm' from minutes and saving in a new column
    df['Duration_minute'] = df['duration'].apply(remove_symbol_2)

    # Iniciating OneHotEncoder to handle categorical features
    ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')


    cat_prep = ohe.fit_transform(df[['airline', 'source', 'destination']])


    # Turn the transformed feature into dataframe and concat them together
    cat_ohe = pd.DataFrame(data=cat_prep, columns=[col for col in ohe.get_feature_names_out()])
    

    data = pd.concat([df, cat_ohe], axis=1)
    
    # Drop Columns that is not necessery
    data.drop(
    columns=[col for col in data.select_dtypes(include=['object', 'datetime64']).columns],
    inplace=True
    )
    data.drop(columns=['id', 'date_of_journey'], inplace=True)
    

    return data
