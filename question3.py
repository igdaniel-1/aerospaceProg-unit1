# Loops and Celestial Object Luminosities

# Objective:
# A: Print out all the names of the celestial bodies using a for loop
# B: Initialize an array variable to contain only the luminosities of the solar objects
# C: Iterate over the luminosities using a while loop 
# ....AND use a conditional print out all the celestial bodies 
# ....with a luminosity of less than 200 solar units

# init data
celestial_objects = {
    "Sirius": 25,  # Sirius is one of the brightest stars in the night sky
    "Andromeda Galaxy": 1000000,  # Andromeda Galaxy has a very high luminosity
    "Jupiter": 0.00006,  # Jupiter reflects sunlight but has low intrinsic luminosity
    "Pleiades": 100,  # The Pleiades star cluster is moderately luminous
    "Orion Nebula": 10000  # The Orion Nebula is a bright emission nebula
}

luminosities = []

for obj in celestial_objects.items():
    # A
    name = obj[0]
    print(name)
    # B
    value = obj[1]
    luminosities.append(value)

    # C
    print("Less than 200 solar units:")
    if value < 200:
        print(name)
