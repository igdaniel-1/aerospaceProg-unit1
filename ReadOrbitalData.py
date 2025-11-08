# Unit 1 - Question 5


# DATA
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Orbital periods (in Earth years)
orbital_periods = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]

# Axial tilts (in degrees)
axial_tilts = [0.03, 177.36, 23.44, 25.19, 3.13, 26.73, 82.23, 28.32]

file = open("orbital_details.txt", "w")

file.write("PLANET_NAME\t ORBITAL_PERIOD\t AXIAL_TILT\n")

for planet in range(len(planet_names)):
# for planet in len(planet_names):
    planet_data = str(planet_names[planet])+ "\t" + str(orbital_periods[planet]) +"\t" + str(axial_tilts[planet]) + "\n"
    file.write(planet_data)