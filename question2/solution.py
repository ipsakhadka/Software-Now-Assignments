# Importing libraries
import os 
from glob import glob
import pandas as pd
import numpy as np


'''Now, we will create a function to combine all csv files and create a dataframe
  There is information about 20 different years in 20 separate csv files. We will merge all those csvs in a single dataframe.
We will use the glob module which makes it easy to find all the pathnames matching a specified pattern, in this case, .csv .
'''

def load_data(path):
    csv_files= glob(os.path.join(path,"*.csv"))       #finding all csv files

    data=[]             

    for file_path in csv_files:                         #reading csv files
        df=pd.read_csv(file_path)
        data.append(df)

    df_combined=pd.concat(data,ignore_index=True)       #combining all data
    return df_combined



'''
Testing if dataframe is created 

df=load_data("question2_data")

print(df.shape)
print(df.head())

'''

# Now we will do the first task which is to calculate the seasonal averages for all stations across all years
#Function to calcualte seasonal average
def average_of_seasons(df):

    seasons={                                                #Australian seasons
        'Summer': ['December','January','February'],
        'Autumn': ['March','April','May'],
        'Winter': ['June','July'],
        'Spring': ['September','October','November']
    }
    
    seasonal_average={}                                      #to store average values for each season
    
    for season, months in seasons.items():                  #to access each seasons and months inside the dictionary
        season_temp=[]                                      #to store temperatures for a season

        for month in months:
            month_temp=df[month].dropna()                    #dropna() to drop all the NaN values as instructed in the question
            season_temp.extend(month_temp.tolist())          #adding month temperatures to the season temperatures

        if len(season_temp)>0:
            average=sum(season_temp)/len(season_temp)        #calculation of average
            seasonal_average[season]=average

    return seasonal_average


#Now, we will create a function to save the seasonal averages to a file

def save_seasonal_averages(seasonal_average, filename='question2_results/average_temp.txt'):
    

    with open(filename, 'w') as file:
        for season, temp in seasonal_average.items():         #to access all 4 seasons and their temperature
            file.write(f"{season}: {temp:.1f}°C\n")           #writing output as instructed by the sample provided in the question

'''

Testing if we get the desired outputs:

df=load_data("question2_data")
results=average_of_seasons(df)
save_seasonal_averages(results)


'''

#Now, we will proceed to finding the largest temperature ranges

#Creating a function to find temperature ranges

def calculate_temperature_ranges(df):

    station_temperature_range={}

    for station in df['STATION_NAME'].unique():                     #We are accessing each stations one by one. The unique functions provides us with all station names.
        data=df[df['STATION_NAME']==station]                        #We will create a new dataframe for each stations. This will help us in separating stations and their data, so we can find the temperature ranges.

        temperatures=[]                                             #to get all temperatures for a station
        
        for column in df.columns:                                           #to accesss only months columns
            if column not in ['STATION_NAME', 'STN_ID', 'LAT', 'LON']:

                month_temperatures=data[column].dropna().values             #accessing temperature for the month
                temperatures.extend(month_temperatures)

        if temperatures:        
            min_temperature=min(temperatures)                                   #lowest tempertaure
            max_temperature=max(temperatures)                                   #highest temperature

            temperature_range=max_temperature - min_temperature

            station_temperature_range[station] ={                                   #storing station results

                'min': min_temperature,
                'max': max_temperature,
                'range': temperature_range
            }
    
    #Now we will find the station with the largest temp range
            
    max_range=0 

    for data in station_temperature_range.values():                         #to find largest range
        if data['range']>max_range:
            max_range=data['range']

    all_stations_with_max_range=[]

    for station, data in station_temperature_range.items():                 #to find all stations with largest range
        if data['range']==max_range:
            all_stations_with_max_range.append((station,data))

    return all_stations_with_max_range



#We will save the stations with largest range in the file


def save_temperature_ranges(all_stations_with_max_range,filename='question2_results/largest_temp_range_station.txt'):
    
    with open(filename, 'w') as file:
        for station, data in all_stations_with_max_range:
            file.write(f"Station {station}: Range {data['range']:.1f}°C (Max: {data['max']:.1f}°C, Min: {data['min']:.1f}°C)\n")



'''

Testing for temperature range outputs

df=load_data("question2_data")
station_largest_ranges=calculate_temperature_ranges(df)
save_temperature_ranges(station_largest_ranges)

'''

