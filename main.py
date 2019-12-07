from graph import save_all_days_plots
from video import generate_video
import sys

# sampleUrls
# https://www.sunrise-and-sunset.com/sv/sun/turkiet/istanbul/2019/
# https://www.sunrise-and-sunset.com/sv/sun/storbritannien/london/2019/
if __name__ == "__main__":
    baseUrl = sys.argv[1]
    save_all_days_plots(baseUrl)
    generate_video('day_length_animation.mp4')