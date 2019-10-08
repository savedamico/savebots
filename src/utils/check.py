import numpy as np

allowed_size = np.linspace(5,30,25,dtype=int)
allowed_speed = np.linspace(1,20,20,dtype=int)
allowed_color = np.linspace(0,255,256,dtype=int)
allowed_x = np.linspace(0,600,601,dtype=int)
allowed_y = np.linspace(0,400,401,dtype=int)

def check_config_file(file):
    if file['size'] not in allowed_size:
        raise ValueError('Size value not allowed')    
    if file['speed'] not in allowed_speed:
        raise ValueError('Speed value not allowed')
    for key in file["color"]:
        if file["color"][key] not in allowed_color:
            raise ValueError('Color value not allowed')
    if file["start_position"]["x"] not in allowed_x:
        raise ValueError('Position value not allowed')
    if file["start_position"]["y"] not in allowed_y:
        raise ValueError('Position value not allowed')
    return