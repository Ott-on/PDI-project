from core.image_buffer import create_image
from core.tools import ERASER, PENCIL
from input.input_handler import mouse_callback
from config import *
import cv2
import numpy as np

color = VERMELHO
mode = PENCIL

image = create_image(WIDTH, HEIGHT, BRANCO)

state = {
    "image": image,
    "mode": mode,
    "color": color,
    "pixel_size": PIXEL_SIZE
}

cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint", mouse_callback, param=state)

while True:
    
    state["mode"] = mode
    state["color"] = color
    
    screen = np.kron(
        np.array(image, dtype=np.uint8),
        np.ones((PIXEL_SIZE, PIXEL_SIZE, 1), dtype=np.uint8)
    )
    
    cv2.imshow("Paint", screen)
    
    key = cv2.waitKey(5) & 0xFF
    
    if key == ord('1'):
        color = VERMELHO
    
    elif key == ord('2'):
        color = AZUL
     
    elif key in (ord('e'), ord('E')):
        if(mode == PENCIL):
            mode = ERASER
        else:
            mode = PENCIL
               
    elif key == 27:
        break
    
    elif cv2.getWindowProperty("Paint", cv2.WND_PROP_VISIBLE) < 1:
        break
    
cv2.destroyAllWindows()
