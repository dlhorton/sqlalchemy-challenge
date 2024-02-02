# Import the dependencies.

# Import necessary libraries and dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt



# Create engine and reflect database
engine = create_engine("sqlite:////workspaces/sqlalchemy-challenge/Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a Flask app
app = Flask(__name__)

# Create a route for the homepage
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-08-23<br/>"
        f"/api/v1.0/2017-08-23/2017-08-23"
    )

# Create a route for precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create a session
    session = Session(engine)

    # Calculate the date one year ago from the last date in the database
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query precipitation data for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Convert results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    # Close the session
    session.close()

    return jsonify(precipitation_data)

# Create a route for station data
@app.route("/api/v1.0/stations")
def stations():
    # Create a session
    session = Session(engine)

    # Query station data
    results = session.query(Station.station, Station.name).all()

    # Convert results to a list of dictionaries
    station_list = [{"station": station, "name": name} for station, name in results]

    # Close the session
    session.close()

    return jsonify(station_list)

# Create a route for temperature observations
@app.route("/api/v1.0/tobs")
def tobs():
    # Create a session
    session = Session(engine)

    # Find the most active station
    active_station = (
        session.query(Measurement.station, func.count(Measurement.station))
        .group_by(Measurement.station)
        .order_by(func.count(Measurement.station).desc())
        .first()
    )

    # Extract the most active station ID
    most_active_station_id = active_station[0]

    # Calculate the date one year ago from the last date in the database
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query temperature observations for the most active station in the last 12 months
    results = (
        session.query(Measurement.date, Measurement.tobs)
        .filter(Measurement.station == most_active_station_id)
        .filter(Measurement.date >= one_year_ago)
        .all()
    )

    # Convert results to a list of dictionaries
    tobs_list = [{"date": date, "tobs": tobs} for date, tobs in results]

    # Close the session
    session.close()

    return jsonify(tobs_list)

# Create a route for temperature statistics with optional start and end dates
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    # Create a session
    session = Session(engine)

    # Query temperature statistics based on start and end dates
    if end:
        results = (
            session.query(
                func.min(Measurement.tobs).label("TMIN"),
                func.avg(Measurement.tobs).label("TAVG"),
                func.max(Measurement.tobs).label("TMAX"),
            )
            .filter(Measurement.date >= start)
            .filter(Measurement.date <= end)
            .first()
        )
    else:
        results = (
            session.query(
                func.min(Measurement.tobs).label("TMIN"),
                func.avg(Measurement.tobs).label("TAVG"),
                func.max(Measurement.tobs).label("TMAX"),
            )
            .filter(Measurement.date >= start)
            .first()
        )

    # Convert results to a dictionary
    temperature_stats_dict = {
        "TMIN": results[0],
        "TAVG": results[1],
        "TMAX": results[2],
    }

    # Close the session
    session.close()

    return jsonify(temperature_stats_dict)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
