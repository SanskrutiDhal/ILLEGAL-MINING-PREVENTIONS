import time
import math

# Define the checkpoint polygons
checkpoint1 = [
    (24.334862, 72.874935),
    (24.335565, 72.876068),
    (24.334168, 72.877315),
    (24.333127, 72.875506)
]

checkpoint2 = [
    (24.333639, 72.871824),
    (24.334494, 72.873737),
    (24.332783, 72.875056),
    (24.331907, 72.873131)
]

checkpoint3 = [
    (24.330439, 72.866456),
    (24.332159, 72.868343),
    (24.330439, 72.870410),
    (24.328701, 72.868281)
]

# Function to check if a point is inside the main fence (similar to is_inside_polygon)
def is_inside_main_fence(latitude, longitude, main_fence_coordinates):
    n = len(main_fence_coordinates)
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = main_fence_coordinates[i]
        xj, yj = main_fence_coordinates[j]

        intersect = ((yi > latitude) != (yj > latitude)) and (longitude < (xj - xi) * (latitude - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
        j = i

    return inside

# Function to check which checkpoints have been passed
def check_checkpoints(latitude, longitude, checkpoints):
    passed_checkpoints = []
    missed_checkpoints = []

    for i, checkpoint in enumerate(checkpoints):
        if is_inside_fence(latitude, longitude, checkpoint):
            passed_checkpoints.append(i + 1)
        else:
            missed_checkpoints.append(i + 1)

    return passed_checkpoints, missed_checkpoints

# Simulate the vehicle's movement
def simulate_vehicle(main_fence, checkpoints, coordinates_list):
    vehicle_inside_main_fence = False
    passed_checkpoints = []
    reached_checkpoint1 = False
    reached_checkpoint2 = False
    iteration=0

    for coordinate in coordinates_list:
        iteration += 1
        latitude, longitude = coordinate
        print(f"\nVehicle coordinates: Latitude {latitude:.6f}, Longitude {longitude:.6f}")

        # Check if the vehicle is inside the main fence
        if is_inside_fence(latitude, longitude, main_fence):
            vehicle_inside_main_fence = True

        if vehicle_inside_main_fence:
            # Check which checkpoints have been passed
            passed_checkpoints, missed_checkpoints = check_checkpoints(latitude, longitude, checkpoints)

            if passed_checkpoints:
                print(f"Vehicle passed through checkpoints: {', '.join(map(str, passed_checkpoints))}")

            # All checkpoints cleared
            if len(passed_checkpoints) == len(checkpoints):
                print("Vehicle passed all checkpoints. Simulation complete.")
                break

            # Check if the vehicle has reached checkpoint 1
            if 1 in passed_checkpoints:
                reached_checkpoint1 = True
            if 2 in passed_checkpoints:
                reached_checkpoint2 = True
            if iteration > 3 and 1 not in passed_checkpoints and not reached_checkpoint1:
                print("Vehicle missed checkpoint 1")
            if iteration > 4 and 2 not in passed_checkpoints and not reached_checkpoint2:
                print("Vehicle missed checkpoint 2")


        time.sleep(1)  # Simulate movement with a 1-second delay

# List of predefined coordinates
coordinates_list = [
    (24.339009, 72.878742),
    (24.337026, 72.873862),
    (24.336400, 72.872618),
    (24.334, 72.876),#checkpoint1
    (24.330439, 72.868281),#checkpoint3
    (24.333, 72.874)#checkpoint2
]

# Start the vehicle simulation
simulate_vehicle(main_fence_coordinates, checkpoints, coordinates_list)
