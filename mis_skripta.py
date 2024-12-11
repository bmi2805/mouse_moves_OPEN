import ctypes
import time


# Struktura za dimenzije ekrana
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def get_mouse_position():
    """Dohvaća trenutnu poziciju miša."""

    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y


def set_mouse_position(x, y):
    """Postavlja poziciju miša."""
    ctypes.windll.user32.SetCursorPos(x, y)


def mouse_moved_up(initial_position):
    """Provjerava je li miš pomaknut prema gore."""
    current_x, current_y = get_mouse_position()
    return current_y < initial_position[1]


def move_mouse_left_right():
    """Pomjera miš lijevo-desno sporijim tempom."""
    screen_width = ctypes.windll.user32.GetSystemMetrics(0)
    screen_height = ctypes.windll.user32.GetSystemMetrics(1)

    start_position = get_mouse_position()

    while True:
        if mouse_moved_up(start_position):
            print("Miš je pomaknut prema gore. Skripta se zaustavlja.")
            break

        # Pomjeri miš na lijevi rub
        set_mouse_position(0, screen_height // 2)
        time.sleep(2.0)
        if mouse_moved_up(start_position):
            print("Miš je pomaknut prema gore. Skripta se zaustavlja.")
            break

        # Pomjeri miš na desni rub
        set_mouse_position(screen_width - 1, screen_height // 2)
        time.sleep(2.0)
        if mouse_moved_up(start_position):
            print("Miš je pomaknut prema gore. Skripta se zaustavlja.")
            break


if __name__ == "__main__":
    print("Skripta pokrenuta. Pomaknite miš prema gore da biste je zaustavili.")
    try:
        move_mouse_left_right()
    except KeyboardInterrupt:
        print("Skripta prekinuta.")
