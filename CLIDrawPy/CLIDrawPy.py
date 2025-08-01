import os
import sys
import time

class CILF:
    def __init__(self, width=20, height=20, fps=60, background_char=' '):
        self.screen_width = width
        self.screen_height = height
        self.fps = fps
        self.background_char = background_char
        self.screen_buffer = [
            [background_char for _ in range(self.screen_width)] 
            for _ in range(self.screen_height)
        ]

    def clear(self, char=None):
        if char is None:
            char = self.background_char
        for y in range(self.screen_height):
            for x in range(self.screen_width):
                self.screen_buffer[y][x] = char

    def draw_pixel(self, x, y, ch):
        if 0 <= x < self.screen_width and 0 <= y < self.screen_height:
            self.screen_buffer[y][x] = ch

    def draw_text(self, x, y, text):
        if 0 <= y < self.screen_height:
            for i, ch in enumerate(text):
                px = x + i
                if 0 <= px < self.screen_width:
                    self.screen_buffer[y][px] = ch

    def draw_box(self, x1, y1, x2, y2, box_char='#', fill_char=None):
        for x in range(x1, x2 + 1):
            if 0 <= x < self.screen_width:
                if 0 <= y1 < self.screen_height:
                    self.screen_buffer[y1][x] = box_char
                if 0 <= y2 < self.screen_height:
                    self.screen_buffer[y2][x] = box_char
        for y in range(y1, y2 + 1):
            if 0 <= y < self.screen_height:
                if 0 <= x1 < self.screen_width:
                    self.screen_buffer[y][x1] = box_char
                if 0 <= x2 < self.screen_width:
                    self.screen_buffer[y][x2] = box_char
        if fill_char:
            for y in range(y1 + 1, y2):
                if 0 <= y < self.screen_height:
                    for x in range(x1 + 1, x2):
                        if 0 <= x < self.screen_width:
                            self.screen_buffer[y][x] = fill_char

    def draw_line(self, x1, y1, x2, y2, ch='*'):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        x, y = x1, y1

        while True:
            self.draw_pixel(x, y, ch)
            if x == x2 and y == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

    def draw_square(cilf, x, y, size, char='#'):
        # Üst ve alt kenarlar
        for i in range(size):
            cilf.draw_pixel(x + i, y, char)             # Üst kenar
            cilf.draw_pixel(x + i, y + size - 1, char)  # Alt kenar

        # Sol ve sağ kenarlar
        for j in range(1, size - 1):
            cilf.draw_pixel(x, y + j, char)             # Sol kenar
            cilf.draw_pixel(x + size - 1, y + j, char)  # Sağ kenar





    
    def draw_circle(self, cx, cy, radius, circle_char='o', fill_char=None):
        x = 0
        y = radius
        d = 1 - radius
        while y >= x:
            points = [
                (cx + x, cy + y), (cx - x, cy + y),
                (cx + x, cy - y), (cx - x, cy - y),
                (cx + y, cy + x), (cx - y, cy + x),
                (cx + y, cy - x), (cx - y, cy - x),
            ]
            for px, py in points:
                self.draw_pixel(px, py, circle_char)
            if fill_char:
                for fill_x in range(cx - x + 1, cx + x):
                    self.draw_pixel(fill_x, cy + y, fill_char)
                    self.draw_pixel(fill_x, cy - y, fill_char)
                for fill_x in range(cx - y + 1, cx + y):
                    self.draw_pixel(fill_x, cy + x, fill_char)
                    self.draw_pixel(fill_x, cy - x, fill_char)
            if d < 0:
                d += 2 * x + 3
            else:
                d += 2 * (x - y) + 5
                y -= 1
            x += 1

    def hide_cursor(self):
        # Windows ve Unix terminal uyumlu gizleme
        if os.name == 'nt':
            os.system('')  # ANSI kodlarını etkinleştir Windows'ta
            sys.stdout.write('\033[?25l')
            sys.stdout.flush()
        else:
            sys.stdout.write('\033[?25l')
            sys.stdout.flush()

    def show_cursor(self):
        if os.name == 'nt':
            os.system('')
            sys.stdout.write('\033[?25h')
            sys.stdout.flush()
        else:
            sys.stdout.write('\033[?25h')
            sys.stdout.flush()


    def move_cursor(self, x, y):
        # Terminalda kursörü konuma taşır (1-based)
        sys.stdout.write(f'\033[{y+1};{x+1}H')
        sys.stdout.flush()

    def clear_screen(self):
        # Terminal temizleme
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def render(self):
        self.move_cursor(0, 0)
        for row in self.screen_buffer:
            print(''.join(row))
        sys.stdout.flush()

    def set_fps(self, fps):
        self.fps = fps

    def wait_frame(self, start_time):
        frame_duration = 1.0 / self.fps
        elapsed = time.time() - start_time
        to_sleep = frame_duration - elapsed
        if to_sleep > 0:
            time.sleep(to_sleep)
