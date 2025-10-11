"""
Author: James Michelson
Purpose: Calculates the volume, Surface area and storage efficiency of cans.
"""

from math import pi

def main():

    can_name = "#1 picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "8Z Short", "#10", "#211", "#300", "#303"
    can_radius = 6.83, 7.73, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10
    can_height = 10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    can_cost = 0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42

    best_efficiency = -1

    for i in range(len(can_name)):
        volume = compute_volume(can_radius[i], can_height[i])
        surface_area = compute_surface_area(can_radius[i], can_height[i])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)

        print(" ")
        print(f"Can Name: {can_name[i]}")
        print(f"Volume: {volume:.2f}")
        print(f"Surface Area: {surface_area:.2f}")
        print(f"Storage Efficiency: {storage_efficiency:.2f}")
        print(" ")
    pass

def compute_volume(radius: float, height: float):
    volume = pi * radius**2 * height
    return volume

def compute_surface_area(radius: float, height: float):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume: float, surface_area: float):
    storage_efficiency = volume / surface_area
    return storage_efficiency

main()