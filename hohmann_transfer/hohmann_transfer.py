# Imports
import math
import sys

# Configuration
sys.tracebacklimit = 0

# Return the delta vs and time of flight for a spacecraft changing orbit
def delta_v_and_time_of_flight(central_body_mass, orbital_distance_a, orbital_distance_b, output_unit):
    G = 6.67430e-11 # Gravitational constant in m^3 kg^(-1) s^-2)
    try:
        # Convert to floats for calculation
        central_body_mass = float(central_body_mass)
        orbital_distance_a = float(orbital_distance_a); orbital_distance_b = float(orbital_distance_b)

        # The gravitational parameter, G*mass of central body
        GM = G*central_body_mass

        # The orbital periods, the square root of 4*pi*orbital_distance^3 divided by GM
        orbital_period_a, orbital_period_b = [math.sqrt((4 * (math.pi ** 2) * (orbital_distance ** 3)) / GM) for orbital_distance in (orbital_distance_a, orbital_distance_b)]

        # The semi-major axis of the transfer orbit, the distance from its center to furthest side
        semi_major_axis = (orbital_distance_a + orbital_distance_b)/2

        # The period of the transfer orbit, the square root of 4*pi^2*semi_major_axis^3/GM
        transfer_orbit_period = math.sqrt((4*(math.pi**2)*(semi_major_axis**3))/GM)

        # The orbiting body velocity, 2*pi*orbital_distance_a/period
        orbital_velocity_a, orbital_velocity_b = [(2 * math.pi * orbital_distance) / orbital_period for orbital_distance, orbital_period in zip((orbital_distance_a, orbital_distance_b), (orbital_period_a, orbital_period_b))]

        # The velocity of the elliptical orbit at its perihelion, 2*pi*semi_major_axis/period * the square root of (2*semi_major_axis/orbital_distance_a)-1
        perihelion_velocity = ((2*math.pi*semi_major_axis)/transfer_orbit_period)*math.sqrt((2*semi_major_axis/orbital_distance_a)-1)

        # The velocity of the ellptical orbit at its aphelion, (2*pi*semi_major_axis)/period * the square root of (2*semi_major_axis/orbital_distance_b)-1
        aphelion_velocity = ((2*math.pi*semi_major_axis)/transfer_orbit_period)*math.sqrt((2*semi_major_axis/orbital_distance_b)-1)

        # Delta V1, the amount of velocity needed to switch from first orbit to transfer orbit to travel to the destination planet
        delta_v1, delta_v2 = [(perihelion_velocity - orbital_velocity_a), (orbital_velocity_b - aphelion_velocity)]

        # Time of flight for the spacecraft to get from body 1 to body 2
        time_of_flight = 0.5*transfer_orbit_period
        time_of_flight_days = time_of_flight/86400
        time_of_flight_years = time_of_flight_days/365
        if output_unit == "years":
            final_time_of_flight = time_of_flight_years
        else:
            final_time_of_flight = time_of_flight_days
        return [delta_v1, delta_v2, final_time_of_flight]
    except ValueError:
        return None

# Interface
while True:
    # Input the values in the terminal
    central_body_mass = input("Central body mass (kg): ")
    orbital_distance_a = input("Initial orbital radius (meters): ")
    orbital_distance_b = input("Final orbital radius (meters): ")
    output_unit = input("Output type for time of flight (years or days): ")

    # Compute the delta vs and time of flight
    hohmann_transfer_calculation = delta_v_and_time_of_flight(central_body_mass, orbital_distance_a, orbital_distance_b, output_unit)

    # Print out the results or ask to input valid values
    if hohmann_transfer_calculation not None:
        print(f"\nDelta V1 is approximately {hohmann_Transfer_Calculations[0]:.2f} meters per second.")
        print(f"\nDelta V2 is approximately {hohmann_Transfer_Calculations[1]:.2f} meters per second.")
        print(f"\nDelta V is approximately {hohmann_Transfer_Calculations[0] + hohmann_Transfer_Calculations[1]:.2f} meters per second.")
        if output_unit == "years":
            print(f"\nThe time of flight is approximately {hohmann_Transfer_Calculations[2]:.2f} years.")
        else:
            print(f"\nThe time of flight is approximately {hohmann_Transfer_Calculations[2]:.2f} days.")
    else:
        print(f"\nInvalid input. Please enter valid numerical values and units.")

    # Ask to do another calculation
    another_calculation = input("\nCalculate another hohmann transfer? (yes/no): ")
    if another_calculation.lower() != "yes":
        break