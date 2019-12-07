import os 
import cv2  
from PIL import Image  

path = "./images/"
  
def generate_video(vid_name): 
    image_folder = path
    video_name = vid_name
    
    images = [img for img in os.listdir(image_folder) 
              if img.endswith(".png") and not img.startswith('.')] 

    images = sorted(images)
    frame = cv2.imread(str(os.path.join(image_folder, images[0])))
  
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, 36.0, (width, height)) # 36 FPS for 10 seconds video
    
    f_n = 0
    for image in images:  
        print('Writing frame for day %s' % str(f_n))
        video.write(cv2.imread(os.path.join(image_folder, image))) 
        f_n += 1 
    
    cv2.destroyAllWindows()  
    video.release()