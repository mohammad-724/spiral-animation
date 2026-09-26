readme_url:  https://mohammad-724.github.io/spiral-animation/

# Python Spiral Code

A lightweight Python repository containing two distinct implementations of spiral logic: a visual **Turtle Graphics** renderer and a data-structure-focused **Matrix Traversal** algorithm.

## Features

* **Visual Rainbow Spiral:** Uses the built-in `turtle` library to draw a dynamic, colorful geometric spiral web on your desktop screen.
* **Spiral Matrix Traversal:** An optimized $O(M \times N)$ algorithm that flattens a 2D grid into a 1D array in a clockwise spiral order, frequently used in technical interview preparation.

## Getting Started

### Prerequisites
* **Python 3.x** (Tkinter must be installed for the Turtle graphics script).

### Installation
Clone this repository to your local machine:
```bash
git clone https://github.com
cd python-spiral-code
```

### Running the Scripts

To launch the interactive **Turtle graphics** visualizer:
```bash
python visual_spiral.py
```

To run the **matrix traversal** algorithm test case:
```bash
python matrix_spiral.py
```

## License
This project is open-source and available under the **MIT License**.


# Animated Rainbow Spiral

A simple Python animation project that generates a continuously expanding **rainbow spiral** using the built-in `turtle` graphics library and HSV color generation.

The project demonstrates basic animation, loops, geometric movement, color generation, and event-driven updates in Python.

## Preview

The program creates a colorful spiral on a black background, with the spiral continuously expanding while its color changes through the rainbow spectrum.

## Features

* Animated expanding spiral
* Continuously changing rainbow colors
* Black background for better visual contrast
* Smooth turtle-based animation
* No external libraries required
* Beginner-friendly Python implementation
* Uses event-driven animation with `ontimer()`

## Technologies Used

* **Python 3**
* **Turtle Graphics**
* **colorsys**

## Project Structure

```text
animated-rainbow-spiral/
│
├── spiral_animation.py
└── README.md
```

## How It Works

The program uses Python's `turtle` module to draw the spiral.

### 1. Turtle Graphics

A turtle object moves forward and turns by a fixed angle:

```python
t.forward(length)
t.right(angle)
```

The movement gradually increases, creating the expanding spiral effect.

### 2. Rainbow Colors

The `colorsys` module converts HSV values into RGB colors:

```python
rgb = colorsys.hsv_to_rgb(hue, 1, 1)
t.pencolor(rgb)
```

The hue value is continuously increased to produce changing rainbow colors.

### 3. Animation

The `screen.ontimer()` function repeatedly calls the animation function:

```python
screen.ontimer(animate, 10)
```

This allows the spiral to be drawn continuously without using a blocking loop.

## Requirements

Python 3.x is required.

The project uses only Python's standard library, so no additional package installation is necessary.

## Installation

Clone the repository:

```bash
git clone https://github.com/mohammad-724/animated-rainbow-spiral.git
```

Move into the project directory:

```bash
cd animated-rainbow-spiral
```

## Run the Program

Execute:

```bash
python spiral_animation.py
```

A new window will open and display the animated spiral.

## Customization

You can easily modify the animation.

### Change Animation Speed

Modify:

```python
screen.ontimer(animate, 10)
```

For example:

```python
screen.ontimer(animate, 20)
```

A larger value makes the animation update less frequently.

### Change Spiral Angle

Modify:

```python
angle = 15
```

For example:

```python
angle = 20
```

This changes the shape and tightness of the spiral.

### Change Spiral Growth

Modify:

```python
length += 0.5
```

A larger value makes the spiral expand faster.

## Learning Outcomes

This project demonstrates:

* Python functions
* Global variables
* Loops and conditional statements
* Turtle graphics
* Coordinate-based drawing
* Color generation using HSV
* Real-time animation
* Event-driven programming
* Basic mathematical visualization

## Future Enhancements

Possible improvements include:

* Mouse-controlled spiral animation
* Keyboard controls
* Adjustable animation speed
* Multiple simultaneous spirals
* Interactive color controls
* Rotating spiral patterns
* Background effects
* Saving the animation as a GIF or video
* User-controlled spiral parameters

## Author

**Mohammad Azmath Ali**

GitHub: **mohammad-724**

## License

This project is created for **educational and learning purposes**.
