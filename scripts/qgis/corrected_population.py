"""
Corrected Population Calculation for SDG 11.2.1 Accessibility Analysis

This script calculates the corrected population density by intersecting transport buffers
with population hexagons, weighting by the proportion of area intersected.

Usage:
    Run in QGIS Python console with the required layers loaded.
"""

import json
import os
from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsProject, QgsField, QgsVectorLayer

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

def add_field_if_not_exists(layer, field_name, field_type):
    """Add a field to the layer if it doesn't exist."""
    if field_name not in [field.name() for field in layer.fields()]:
        layer.dataProvider().addAttributes([QgsField(field_name, field_type)])
        layer.updateFields()
        print(f"Added field '{field_name}' to layer '{layer.name()}'.")

def calculate_corrected_population():
    """Main function to calculate corrected population."""
    try:
        # Get the intersection layer
        layer = get_layer_by_name(config['layers']['intersection_result'])

        # Add corrected population field if needed
        add_field_if_not_exists(layer, config['fields']['population_corrected'], QVariant.Double)

        # Get field indices
        pop_idx = layer.fields().indexFromName(config['fields']['population'])
        total_surf_idx = layer.fields().indexFromName(config['fields']['surface_total'])
        inter_surf_idx = layer.fields().indexFromName(config['fields']['surface_intersection'])
        corr_pop_idx = layer.fields().indexFromName(config['fields']['population_corrected'])

        # Start editing
        layer.startEditing()

        # Process each feature
        for feature in layer.getFeatures():
            population = feature[pop_idx]
            total_surface = feature[total_surf_idx]
            intersection_surface = feature[inter_surf_idx]

            # Calculate corrected population
            if total_surface > 0:
                corrected_population = (intersection_surface / total_surface) * population
            else:
                corrected_population = 0.0

            # Update the feature
            feature[corr_pop_idx] = corrected_population
            layer.updateFeature(feature)

        # Commit changes
        layer.commitChanges()
        print("Successfully updated corrected population field.")

        # Calculate and print total
        total_corrected = sum(f[config['fields']['population_corrected']] for f in layer.getFeatures())
        print(f"Total Corrected Population (SDG 11.2): {total_corrected:,.0f} inhabitants")

    except Exception as e:
        print(f"Error in calculate_corrected_population: {str(e)}")
        layer.rollBack()  # Roll back changes on error

if __name__ == "__main__":
    calculate_corrected_population()
