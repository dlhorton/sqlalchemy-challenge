# sqlalchemy-challenge

# Honolulu Climate Analysis and Flask API

## Introduction

Welcome to Honolulu, Hawaii! This README guide outlines the steps for conducting a climate analysis and developing a Flask API to explore weather conditions in the area. Follow the instructions below for both the climate analysis and Flask API development.

## Part 1: Analyze and Explore the Climate Data

### Setup

1. Used the provided files (`climate_starter.ipynb` and `hawaii.sqlite`) for the climate analysis.
2. Connect to the SQLite database using SQLAlchemy's `create_engine()` function.
3. Reflected tables into classes using `automap_base()` and saved references to the classes named `Station` and `Measurement`.

### Precipitation Analysis

- Found the most recent date in the dataset - 2017-08-23
- Retrieved the previous 12 months of precipitation data.
count    2021.000000
mean        0.177279
std         0.461190
min         0.000000
25%         0.000000
50%         0.020000
75%         0.130000
max         6.700000

### Station Analysis

- Calculated the total number of stations in the dataset - 9
- Identified most Active Stations:
        Station: USC00519281, Count: 2772
        Station: USC00519397, Count: 2724
        Station: USC00513117, Count: 2709
        Station: USC00519523, Count: 2669
        Station: USC00516128, Count: 2612
        Station: USC00514830, Count: 2202
        Station: USC00511918, Count: 1979
        Station: USC00517948, Count: 1372
        Station: USC00518838, Count: 511
- Calculated the lowest, highest, and average temperatures for the most-active station.
        Temperature Statistics for Station USC00519281:
        Lowest Temperature: 54.0
        Highest Temperature: 85.0
        Average Temperature: 71.66378066378067
- Query and plot the previous 12 months of temperature observation (TOBS) data for the most-active station.


## Part 2: Design Climate App
Created app using Flask API

### Routes

- 'http://127.0.0.1:53212/': Homepage listing all available routes
- `/api/v1.0/precipitation`: Convert the last 12 months of precipitation data to a dictionary and return the JSON representation.
- `/api/v1.0/stations`: Return a JSON list of stations from the dataset.
- `/api/v1.0/tobs`: Query and return a JSON list of temperature observations for the previous year from the most-active station.
- `/api/v1.0/<start>`: Return JSON with the minimum, average, and maximum temperatures for dates greater than or equal to the specified start date.
- `/api/v1.0/<start>/<end>`: Return JSON with temperature statistics for dates within the specified start and end range.

Feel free to explore and plan your trip based on the climate insights provided by this Flask API! Safe travels and enjoy your vacation in Honolulu, Hawaii.
