PENCIL = 0
ERASER = 1

def get_current_color(mode, color):
    if mode == PENCIL:
        return color
    elif mode == ERASER:
        return (255, 255, 255)
