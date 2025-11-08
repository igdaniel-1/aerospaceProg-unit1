# Distance = Speed x Time
# Fuel Consumption = Distance / Fuel Efficiency
# Time to Destination = Distance / Speed


# Given Data
travel_time = 10  # hours
speed = 5000      # kilometers per hour
fuel_efficiency = 10  # kilometers per liter
first_name = "Sally"
last_name = "Ride"

def distance(travel_time,speed):
    return travel_time*speed

def fuel_consumed(distance, fuel_efficiency):
    return distance/fuel_efficiency

def time_to_destination(distance, speed):
    return distance/speed

def main():
    dist_travelled = distance(travel_time,speed)
    print("Astronaut: ", first_name, last_name)
    print("Distance Traveled: ",dist_travelled)
    print("Fuel Consumed: ", fuel_consumed(dist_travelled,fuel_efficiency))
    print("Time to Destination: ", time_to_destination(dist_travelled, speed))

main()
    