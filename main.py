import time
from core.image_buffer import clear_image, create_image
from core.tools import ERASER, PENCIL
from input.input_handler import mouse_callback
from config import *
import cv2
import numpy as np

color = VERMELHO
mode = PENCIL
brush_size = 1

image = create_image(WIDTH, HEIGHT, BRANCO)

state = {
    "image": image,
    "mode": mode,
    "color": color,
    "pixel_size": PIXEL_SIZE,
    "brush_size": brush_size
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
    
    
    # vermelho ou azul
    if key == ord('1'):
        color = VERMELHO
    
    elif key == ord('2'):
        color = AZUL
     
    # pincel ou borracha
    if key in (ord('e'), ord('E')):
        if(mode == PENCIL):
            mode = ERASER
        else:
            mode = PENCIL
            
    # aumentar e diminuir pincel
    if key == ord("+") or key == ord("="):
        brush_size += 1
        if brush_size > 10:
            brush_size = 10
    
    elif key == ord("-"):
        brush_size -= 1
        if brush_size < 1:
            brush_size = 1
        
    state["brush_size"] = brush_size
    
    # apagar a tela
    if key in (ord('c'), ord('C')):
        clear_image(image, BRANCO)
        
    # salvar imagem
    if key in (ord('s'), ord('S')):
        filename = f"save/drawing_{int(time.time())}.png"
        cv2.imwrite(filename, screen)
        print(f"Imagem salva como {filename}")
    
    # apertar Esc       
    if key == 27:
        break
    
    elif cv2.getWindowProperty("Paint", cv2.WND_PROP_VISIBLE) < 1:
        break
    
cv2.destroyAllWindows()
