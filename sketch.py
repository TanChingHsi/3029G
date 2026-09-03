"""
Schotter — after Georg Nees, 1968.

A grid of hexagons and four-pointed stars that falls apart as it descends. The top row is perfectly ordered;
each row after it is rotated and displaced a little more than the one before.
Nees plotted the original on a Zuse Graphomat; you are about to do it in a
language he did not have, on a machine he would have envied.

Run it:

    python sketch.py

It writes sketch.svg next to this file. Open that in a browser (or drag it into
VS Code). Nothing to install — this uses only what ships with Python.

Then change one of the numbers below, run it again, and commit. GitHub will show
you the two images side by side.
"""

import math
import random

# ---------------------------------------------------------------------------
# The knobs. These are yours. Change them, run again, look, commit.
# ---------------------------------------------------------------------------

COLS = 12            # shapes across
ROWS = 54            # shapes down — the chaos builds over this many rows
SEED = 5913          # any integer. Same seed = same image, every time, forever.
CHAOS = 1.4          # how fast order collapses. 0 = perfect grid. 2 = rubble.
STAR_RATIO = 0.75     # percentage of stars as a float from 0.0 (no stars) to 1.0 (all stars).
RANDOMIZE = True    # set True to generate a fresh seed and chaos value each run.
SQUARE = 40          # size of one square, in svg units
MARGIN = 60          # breathing room around the grid
STROKE = "#111111"   # line colour
BACKGROUND = "#faf8f4"
STROKE_WIDTH = 1.4

OUTPUT = "sketch.svg"

# ---------------------------------------------------------------------------
# The drawing.
# ---------------------------------------------------------------------------


def star(cx, cy, size):
    points = []
    for index in range(8):
        angle = -math.pi / 2 + index * math.pi / 4
        radius = size * (0.42 if index % 2 == 0 else 0.14)
        points.append(f'{cx + math.cos(angle) * radius:.2f},{cy + math.sin(angle) * radius:.2f}')
    return f'<polygon points="{" ".join(points)}" />'


def hexagon(cx, cy, size):
    points = []
    for index in range(6):
        angle = -math.pi / 2 + index * math.pi / 3
        radius = size * 0.36
        points.append(f'{cx + math.cos(angle) * radius:.2f},{cy + math.sin(angle) * radius:.2f}')
    return f'<polygon points="{" ".join(points)}" />'


def shapes(x, y, size, angle_deg, dx, dy, is_star):
    """One four-pointed star or hexagon, transformed about its own centre."""
    cx, cy = x + size / 2, y + size / 2
    transform = (
        f'translate({dx:.2f} {dy:.2f}) '
        f'rotate({angle_deg:.2f} {cx:.2f} {cy:.2f})'
    )

    polygon = star(cx, cy, size) if is_star else hexagon(cx, cy, size)
    return f'  {polygon[:-3]} transform="{transform}" />'


def randomizer():
    """Return a fresh seed and chaos value for a new composition."""
    rng = random.SystemRandom()
    return rng.randrange(1_000_000), rng.uniform(0, 2)


def draw(seed=SEED, chaos=CHAOS):
    if not 0 <= STAR_RATIO <= 1:
        raise ValueError("STAR_RATIO must be between 0.0 and 1.0")

    rng = random.Random(seed)
    parts = []

    for row in range(ROWS):
        # Disorder grows with depth. Squaring it keeps the top calm and lets the
        # bottom really come apart — the whole point of the piece.
        damage = chaos * (row / ROWS) ** 2

        for col in range(COLS):
            x = MARGIN + col * SQUARE
            y = MARGIN + row * SQUARE
            angle = rng.uniform(-1, 1) * damage * 45
            dx = rng.uniform(-1, 1) * damage * SQUARE * 0.5
            dy = rng.uniform(-1, 1) * damage * SQUARE * 0.5
            parts.append(shapes(x, y, SQUARE, angle, dx, dy, rng.random() < STAR_RATIO))

    width = COLS * SQUARE + MARGIN * 2
    height = ROWS * SQUARE + MARGIN * 2

    return "\n".join(
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
            f'height="{height}" viewBox="0 0 {width} {height}">',
            f'  <rect width="100%" height="100%" fill="{BACKGROUND}" />',
            f'  <g fill="none" stroke="{STROKE}" stroke-width="{STROKE_WIDTH}">',
            *parts,
            "  </g>",
            "</svg>",
        ]
    )


if __name__ == "__main__":
    seed, chaos = (randomizer() if RANDOMIZE else (SEED, CHAOS))
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(draw(seed, chaos))
    print(f"wrote {OUTPUT} — {COLS}x{ROWS} shapes, seed {seed}, chaos {chaos:.2f}")
    print("open it in a browser, then change a number and run me again")
