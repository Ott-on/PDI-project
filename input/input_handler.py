import cv2
from core.image_buffer import draw_brush
from core.tools import get_current_color

drawing = False

def mouse_callback(event, x, y, flags, param):
    global drawing
    img = param["image"]
    mode = param["mode"]
    color = param["color"]
    PIXEL_SIZE = param["pixel_size"]

    grid_x = x // PIXEL_SIZE
    grid_y = y // PIXEL_SIZE
  
    current_color = get_current_color(mode, color)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        draw_brush(img, grid_x, grid_y, current_color, size=1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        draw_brush(img, grid_x, grid_y, current_color, size=1)
