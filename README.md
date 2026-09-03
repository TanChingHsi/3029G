# 3029G

---

## How to Run

This project has **zero external dependencies**. You do not need to install anything via `pip`.

1. Clone or download this repository.
2. Open your terminal or command prompt and navigate to the project directory:
   ```bash
   cd path/to/your/project
   ```
3. Run the script using Python:
   ```bash
   python sketch.py
   ```
4. Open the freshly generated `sketch.svg` file by double-clicking it to view it in any web browser, or drag it directly into an IDE like VS Code.

---

## Configuration & Customization

You can tweak the generation parameters directly inside `sketch.py`. Open the file and locate **The knobs** section to modify how the artwork renders:

### Grid & Layout
* **`COLS`** (`12`): The number of shapes generated horizontally across each row.
* **`ROWS`** (`54`): The number of shapes generated vertically down the grid. Adding more rows gives the chaos more space to compound.
* **`SQUARE`** (`40`): The baseline bounding box size for an individual shape (in SVG coordinate units).
* **`MARGIN`** (`60`): The breathing room or padding around the edges of the final canvas.

### Logic & Chaos
* **`CHAOS`** (`1.4`): A multiplier determining how aggressively the grid breaks down. `0` keeps the grid entirely perfect; `2` shatters it into a pile of rubble.
* **`STAR_RATIO`** (`0.75`): A float from `0.0` (only hexagons) to `1.0` (only four-pointed stars) controlling the structural mix of shapes.
* **`SEED`** (`5913`): The unique integer that initializes the pseudo-random generation. Using the exact same seed ensures the exact same placement, rotation, and distribution every time.
* **`RANDOMIZE`** (`True`): When set to `True`, the script will ignore the hardcoded `SEED` and `CHAOS` values and generate completely unique, unpredictable parameters on every single run.

### Styling & Output
* **`STROKE`** (`"#111111"`): The CSS-compatible hex color value code for the shape outlines.
* **`BACKGROUND`** (`"#faf8f4"`): The CSS-compatible hex color value code for the canvas background.
* **`STROKE_WIDTH`** (`1.4`): The thickness of the polygon line strokes in pixels.
* **`OUTPUT`** (`"sketch.svg"`): The destination filename where the vector graphic will save.

---


