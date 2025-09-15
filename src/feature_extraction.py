# src/feature_extraction.py
import re

# Defined mappings for entities, allowed units, and abbreviations
entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'item_weight': {'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton'},
    'maximum_weight_recommendation': {'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {'centilitre', 'cubic foot', 'cubic inch', 'cup', 'decilitre', 'fluid ounce', 'gallon',
                    'imperial gallon', 'litre', 'microlitre', 'millilitre', 'pint', 'quart'}
}

# Consolidate all allowed units for quick lookup
allowed_units = {unit for entity in entity_unit_map for unit in entity_unit_map[entity]}

# Mapping for common unit abbreviations to their full forms
unit_abbreviation_map = {
    'cm': 'centimetre',
    'mm': 'millimetre',
    'm': 'metre',
    'g': 'gram',
    'kg': 'kilogram',
    'mg': 'milligram',
    'oz': 'ounce',
    'lbs': 'pound',
    'bs': 'pound',
    'lb': 'pound',
    'kv': 'kilovolt',
    'mv': 'millivolt',
    'v': 'volt',
    'w': 'watt',
    'kw': 'kilowatt',
    'cl': 'centilitre',
    'ml': 'millilitre',
    'l': 'litre',
    '\'': 'foot',
    '\"': 'inch',
    'c.m.': 'centimetre'
}

# Mapping for irregular plural forms to their singular
irregular_plurals = {
    'feet': 'foot', 'inches': 'inch', 'ounces': 'ounce'
}

def convert_abbreviation(unit):
    """
    Converts a unit abbreviation to its full form using the unit_abbreviation_map.
    """
    return unit_abbreviation_map.get(unit, unit)

def singularize(unit):
    """
    Converts plural unit forms to singular, handling irregular plurals first.
    """
    if unit in irregular_plurals:
        return irregular_plurals[unit]
    # Handle regular plurals by removing 's' if the singular form is in allowed_units
    if unit.endswith('s') and unit[:-1] in allowed_units:
        return unit[:-1]
    # Return as is if no conversion is needed
    return unit

def extract_dimensions(text):
    """
    Extracts numerical values and their corresponding units from a given text.
    It uses regular expressions to find patterns of numbers followed by units,
    then cleans and normalizes the units.
    """
    # Regex to find numbers (integers or decimals) followed by an optional space and letters (for units)
    pattern = re.compile(r'(?P<value>-?\d+(?:\.\d+)?)\s*(?P<unit>[a-zA-Z.]+)')
    matches = pattern.findall(text)

    dimensions = []
    for match in matches:
        value, _, unit = match # value is the number, unit is the text following it
        # Clean and process the unit: remove dots, strip whitespace, convert to lowercase
        cleaned_unit = unit.replace('.', '').strip().lower()
        cleaned_unit = convert_abbreviation(cleaned_unit) # Convert abbreviations
        cleaned_unit = singularize(cleaned_unit)         # Convert to singular form

        # Only add to dimensions if the cleaned unit is an allowed unit
        if cleaned_unit in allowed_units:
            dimensions.append((float(value), cleaned_unit))

    return dimensions