# Unit 1 - Question 2

# Rocket Engine Performance Calculator

# Objective:
# Calculator must ask the user for the thrust and mass flow rate of the propellant
# Typecast the values as float variables
# Calculate the specific impulse of the rocket engine
# Calculate the exhaust velocity of the rocket
# Print out the values as strings

# Specific Impulse = Thrust / (Mass Flow Rate * 9.81)
# Exhaust Velocity = Specific Impulse * 9.81

def main():
    thrust = float(input("Thrust value: "))
    massFlowRate = float(input("Mass flow rate of the propellant: "))

    specificImpulse = thrust/(massFlowRate*9.81)

    print("Specific Impulse: ", specificImpulse)
    print("Exhaust Velocity: ", specificImpulse*9.81)

main()