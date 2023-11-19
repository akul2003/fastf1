import fastf1

###############################################################################
# Load the race session


def session():
    session = fastf1.get_session(2023, "Las Vegas", 'R')
    session.load()
    laps = session.laps
    drivers = session.drivers
    drivers = [session.get_driver(driver)["Abbreviation"] for driver in drivers]
    return laps, drivers