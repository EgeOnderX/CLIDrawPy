import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CLIDrawPy import CILF
def main():
    cilf = CILF(width=40, height=20, fps=30, background_char='.')
    cilf.clear()
    cilf.hide_cursor()
    try:
        CILF.draw_square(cilf, 5, 5, 10, '#')
        cilf.render()
        input("Press Enter to exit...")
    finally:
        cilf.show_cursor()
        print("\nExited cleanly.")

if __name__ == "__main__":
    main()
