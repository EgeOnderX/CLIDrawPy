# CLIDrawPy

CLIDrawPy is a tiny library written in pure Python for drawing ASCII shapes in the terminal and animating them.

---

## Features

- Draw pixels, lines, boxes, squares, and circles using ASCII characters  
- Render text at any position on the terminal screen  
- Animate shapes with configurable FPS (frames per second)  
- Clear and control terminal screen and cursor for smooth animations  
- Cross-platform support (Windows, Linux, macOS terminals)  

---

## Installation

Simply import `CLIDrawPy.py` into your project.

---

## License

MIT License

Copyright (c) 2025 Ege Önder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Inspiration

[CILFront](https://github.com/OwnderDuck/CILFront)

---

## Screenshots
<img width="686" height="371" alt="picture1" src="https://github.com/user-attachments/assets/791614d2-61d2-43d4-87e7-4f154f88c428" />

---

## Examples

`CLIDrawPy/examples/simplesquare.py`

# Methods and Descriptions

- `__init__(self, width=20, height=20, fps=60, background_char=' ')`  
  Constructor. Sets screen width, height, FPS, and background character.

- `clear(self, char=None)`  
  Clears the screen buffer. Optionally fills with a given character (default is background).

- `draw_pixel(self, x, y, ch)`  
  Draws a single character at coordinates (x, y).

- `draw_text(self, x, y, text)`  
  Draws text starting from coordinates (x, y).

- `draw_box(self, x1, y1, x2, y2, box_char='#', fill_char=None)`  
  Draws a rectangular box defined by corners. Optionally fills inside.

- `draw_line(self, x1, y1, x2, y2, ch='*')`  
  Draws a line between two points using the specified character.

- `draw_square(cilf, x, y, size, char='#')`  
  Draws a square. (Not a static method, expects instance as `cilf` parameter.)

- `draw_circle(self, cx, cy, radius, circle_char='o', fill_char=None)`  
  Draws a circle, optionally filled.

- `hide_cursor(self)`  
  Hides the terminal cursor (compatible with Windows and Unix).

- `show_cursor(self)`  
  Shows the terminal cursor.

- `move_cursor(self, x, y)`  
  Moves the terminal cursor to position (x, y) — 1-based indexing.

- `clear_screen(self)`  
  Clears the terminal screen (`cls` on Windows, `clear` on Unix).

- `render(self)`  
  Renders the current screen buffer to the terminal.

- `set_fps(self, fps)`  
  Sets the animation frames per second.

- `wait_frame(self, start_time)`  
  Waits to maintain FPS timing for animations.
