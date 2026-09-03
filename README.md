# 3029G
COLS: Controls the width of the grid by defining how many geometric shapes are rendered horizontally across each row.

ROWS: Controls the height of the grid and the length of the progression. Because the structural damage builds up line-by-line, adding more rows allows the chaos to compound further down the canvas.

SEED: An integer that initializes the pseudo-random number generator. Using the exact same seed ensures the exact same placement, rotation, and distribution of shapes every single time the script runs.CHAOS: A multiplier determining how aggressively the grid deconstructs as it moves downward. Setting this to 0 leaves the grid completely perfect, while setting it to 2 completely shatters the pattern into a pile of rubble.

STAR_RATIO: A float from 0.0 to 1.0 that adjusts the mix of shapes. Setting this to 0.0 renders only hexagons, 1.0 renders only four-pointed stars, and anything in between creates a mixed distribution.

RANDOMIZE: A boolean switch. If set to True, the script ignores the hardcoded SEED and CHAOS values and generates completely unique random parameters on every single execution.

SQUARE: The baseline bounding box size for an individual shape, measured in SVG coordinate units.

MARGIN: The padding or breathing room around the edges of the final canvas, preventing the shapes from touching the very edge of the image frame.STROKE: The CSS-compatible hex color value code used to paint the lines of the polygons.