from core.image_buffer import give_height_width


def fake_ir(image_gray):
    
    height = len(image_gray)
    width = len(image_gray[0])
    
    ir_image = []
        
    for y in range(height):
        row = []
        
        for x in range(width):
            intensity, _, _ = image_gray[y][x]
            
            r = intensity
            g = 0
            b = 255 - intensity
            
            row.append((r, g, b))
                
        ir_image.append(row)
        
    return ir_image  

def to_grayscale(image):
    height, width = give_height_width(image)
    
    new_image = []
    
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = image[y][x]
            intensity = (r + g + b) // 3
            row.append((intensity, intensity, intensity))
        new_image.append(row)
    
    return new_image
                