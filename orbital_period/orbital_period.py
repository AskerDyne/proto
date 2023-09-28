# Imports
import math
import sys

# Configuration
sys.tracebacklimit = 0

def orbital_period(semi_major_axis, central_body_mass, semi_major_axis_unit, output_unit):
    G = 6.67430e-11  # Gravitational constant in m^3 kg^(-1) s^(-2)
    try:
        semi_major_axis = float(semi_major_axis)
        central_body_mass = float(central_body_mass)
        if semi_major_axis_unit.lower() == "au":
            semi_major_axis_meters = semi_major_axis * 1.496e11  # 1 AU = 1.496 x 10^11 meters
        elif semi_major_axis_unit.lower() == "km":
            semi_major_axis_meters = semi_major_axis * 1000.0  # 1 km = 1000 meters
        elif semi_major_axis_unit.lower() == "m":
            semi_major_axis_meters = semi_major_axis
        else:
            return None

        # Kepler's third law of planetary motion
        period_seconds = 2 * math.pi * math.sqrt(semi_major_axis_meters ** 3 / (G * central_body_mass))
        period_days = period_seconds / (60 * 60 * 24)
        if output_unit.lower() == "years":
            period_years = period_days / 365.25  # Avg approximate number of days in a year (inc. leap years)
            return period_years
        else:
            return period_days
    except ValueError:
        return None

# Interface
while True:
    semi_major_axis = input("Semi-major axis (S-Mjr) value: ")
    semi_major_axis_unit = input("Unit measurement for S-Mjr axis (AU, km, or m): ")
    central_body_mass = input("Enter the central body (CB) mass (kg or solar masses): ")
    output_unit = input("Output type (years or days): ")

    orbital_period_result = orbital_period(semi_major_axis, central_body_mass, semi_major_axis_unit, output_unit)

    if orbital_period_result is not None:
        if output_unit.lower() == "years":
            print(f"\nThe orbital period is approximately {orbital_period_result:.2f} years.")
        else:
            print(f"\nThe orbital period is approximately {orbital_period_result:.2f} days.")
    else:
        print("\nInvalid input. Please enter valid numerical values and units.")
    
    another_calculation = input("\nCalculate another orbital period? (yes/no): ")
    if another_calculation.lower() != "yes":
        break