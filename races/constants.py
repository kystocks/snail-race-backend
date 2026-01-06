"""
Shared constants for JScargot backend
These values should match the frontend constants
"""

# Valid snail colors - must match frontend SNAIL_COLORS
SNAIL_COLORS = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('orange', 'Orange'),
    ('purple', 'Purple'),
]

# Extract just the color values for validation
SNAIL_COLOR_VALUES = [color[0] for color in SNAIL_COLORS]
