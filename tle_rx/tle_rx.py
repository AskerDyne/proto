# Imports
import json
import pytz
import subprocess
import sys
from colorama import Fore
from datetime import datetime
from skyfield.api import load, EarthSatellite

# Configuration
sys.tracebacklimit = 0

url = "https://tle.ivanstanojevic.me/api/tle/"

print_text = (f"{Fore.WHITE}")
print_failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]")
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]")
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]")

def tle_data(tle_data):
    try:
        # Load the ephemeris data if available!
        eph = load('de421.bsp')
        # Create the satellite object, getting current date/time in UTC and calculate relative position in lat/lon degrees
        satellite = EarthSatellite(tle_data["line1"], tle_data["line2"])
        current_time_utc = datetime.now(pytz.utc)
        date_time = load.timescale().utc(current_time_utc)
        satellite_position = satellite.at(date_time)
        latitude = satellite_position.subpoint().latitude.degrees
        longitude = satellite_position.subpoint().longitude.degrees
        return latitude, longitude

    except Exception as e:
        print(f"{print_failed}: an error occurred returning {e}")
        return None, None

try:
    curl_output = subprocess.check_output(["curl", url])
    curl_output = curl_output.decode("utf-8")
    data = json.loads(curl_output)

    print(f"{print_alert} LIVE DATA\n")
    for tle in data["member"]:
        satellite_name = tle["name"]
        sat_id = tle["satelliteId"]
        latitude, longitude = tle_data(tle)

        if latitude is not None and longitude is not None:
            latitude_str = str(latitude)
            longitude_str = str(longitude)
            print(f"{print_prompt} Satellite: {satellite_name} | ID: {sat_id}")
            print(f"Latitude: {latitude_str}, Longitude: {longitude_str}\n")
        else:
            print(f"{print_failed}: calculating position for {satellite_name}")

except subprocess.CalledProcessError as e:
    print(f"{print_failed}: an error occurred curling returning {e}")
except json.JSONDecodeError as e:
    print(f"{print_failed}: an error parsing JSON data returning {e}")
except Exception as e:
    print(f"{print_failed}: an error occurred returning {e}")