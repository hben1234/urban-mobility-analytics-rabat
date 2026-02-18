"""
Transport Accessibility Score Calculation for SDG 11.2.1

This script calculates the percentage of urban population with access to public transport
within the defined buffer distance, providing the SDG 11.2.1 indicator.

Usage:
    Run in QGIS Python console after calculating corrected population.
"""

import json
import os
from qgis.core import QgsProject

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'qgis_settings.json')
with open(config_path, 'r') as f:
    config = json.load(f)

def get_layer_by_name(name):
    """Get a layer by name from the current QGIS project."""
    layer = QgsProject.instance().mapLayersByName(name)
    if not layer:
        raise ValueError(f"Layer '{name}' not found in the project.")
    return layer[0]

def calculate_transport_score():
    """Calculate the transport accessibility score."""
    try:
        # Get layers
        layer_intersection = get_layer_by_name(config['layers']['intersection_result'])
        layer_total = get_layer_by_name(config['layers']['total_population'])

        # Sum accessible (corrected) population
        accessible_population = sum(f[config['fields']['population_corrected']] for f in layer_intersection.getFeatures())

        # Sum total urban population (using distinct values as per original logic)
        # Note: This assumes population field represents unique area populations
        distinct_populations = set()
        for f in layer_total.getFeatures():
            distinct_populations.add(f[config['fields']['population']])
        total_urban_population = sum(distinct_populations)

        # Calculate score
        if total_urban_population > 0:
            score = (accessible_population / total_urban_population) * 100
        else:
            score = 0.0

        # Print results
        print(f"Transport Accessibility Score (SDG 11.2.1): {score:.1f}%")
        print(f"Accessible Population: {accessible_population:,.0f}")
        print(f"Total Urban Population: {total_urban_population:,.0f}")

        return score

    except Exception as e:
        print(f"Error in calculate_transport_score: {str(e)}")
        return None

if __name__ == "__main__":
    calculate_transport_score()