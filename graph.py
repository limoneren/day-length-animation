import numpy as np
import matplotlib.pyplot as plt
import data
from matplotlib.animation import FuncAnimation
import matplotlib
import matplotlib.animation as manimation
import os

def download_all_data(baseUrl):
    return data.get_all_months_data(baseUrl)

def plot_single_day(f_num, all_months_data):
    date = all_months_data.iloc[f_num,0]
    sun_up_time = all_months_data.iloc[f_num,1]
    sun_down_time = all_months_data.iloc[f_num,2]
    total = all_months_data.iloc[f_num,3]

    sun_up_hours = int(sun_up_time.split(':')[0])
    sun_up_minuties = int(sun_up_time.split(':')[1])

    sun_down_hours = int(sun_down_time.split(':')[0])
    sun_down_minuties = int(sun_down_time.split(':')[1])

    x = [i for i in range(1440)] # num of minutes in a day
    left_curve_start = sun_up_hours * 60 + sun_up_minuties
    left_curve_ends = left_curve_start + 150
    right_curve_ends = sun_down_hours * 60 + sun_down_minuties
    right_curve_start = right_curve_ends - 150
    
    sun_up_xcoord = left_curve_start
    sun_down_xcoord = right_curve_ends
    title_date = date
    total_hours = total
    sun_up_hour = sun_up_time
    sun_down_hour = sun_down_time

    y1 = []
    y2 = []
    y3 = []
    for i in range(1440):
        if i < left_curve_start:
            y1.append(0)
            y2.append(0)
            y3.append(0)
        elif i >= left_curve_start and i < left_curve_ends:
            y1.append((i - left_curve_start)**2)
            y2.append(0)
            y3.append(0)
        elif i >= left_curve_ends and i < right_curve_start:
            y1.append(0)
            y2.append((left_curve_ends - left_curve_start)**2)
            y3.append(0)
        elif i >= right_curve_start and i < right_curve_ends:
            y1.append(0)
            y2.append(0)
            y3.append(((i - right_curve_start) - (left_curve_ends - left_curve_start))**2)
        elif i >= right_curve_ends:
            y1.append(0)
            y2.append(0)
            y3.append(0)

    y = np.vstack([y1, y2, y3])
    fig, ax = plt.subplots(facecolor = '#212E39')

    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['bottom'].set_color('white')
    ax.set_yticklabels([])
    ax.patch.set_facecolor('#212E39')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='x',direction='out', width=0, labelsize ='large')
    plt.gca().axes.get_yaxis().set_visible(False)

    pal = ["#FFBD01", "#FFBD01", "#FFBD01", "#FFBD01"]
    plt.stackplot(x, y1, y2, y3, colors=pal)

    sun_up_lbl = 'SUN UP\n'+sun_up_hour
    sun_down_lbl = 'SUN DOWN\n'+sun_down_hour
    plt.xticks([-100, sun_up_xcoord, sun_down_xcoord, 1540], ('00:00', sun_up_lbl, sun_down_lbl,'23:59'))

    total_lbl_x = 0.5 + (((right_curve_ends + left_curve_start)/2 - 720) / 1600.0)
    total_hours_lbl_x = total_lbl_x

    plt.text(0.5,0.8,'DATE',fontsize=15, color='white',horizontalalignment='center',transform=ax.transAxes)
    plt.text(0.5,0.72,title_date,fontsize=18, color='white',fontweight='bold',horizontalalignment='center',transform=ax.transAxes)
    plt.text(total_lbl_x,0.4,'TOTAL',fontsize=14, color='#212E39',horizontalalignment='center',transform=ax.transAxes)
    plt.text(total_hours_lbl_x,0.32,total_hours,fontsize=17, color='#212E39',fontweight='bold',horizontalalignment='center',transform=ax.transAxes)

    label = ax.get_xticklabels()[0]
    label.set_fontsize(5)
    label_2 = ax.get_xticklabels()[3]
    label_2.set_fontsize(5)

    bottom, top = plt.ylim() 
    plt.ylim((bottom, top * 1.5))

    f_num = str(f_num)
    if len(f_num) == 1:
        f_num = '00' + f_num
    elif len(f_num) == 2:
        f_num = '0' + f_num
    
    if not os.path.exists('./images/'):
        os.makedirs('./images/')
    
    fig_name = './images/'+str(f_num)+'.png'
    print('Saving day %s plot' % str(f_num))
    plt.savefig(fig_name, facecolor=fig.get_facecolor(), bbox_inches='tight',dpi = 300)
    #plt.show()
    plt.close()

def save_all_days_plots(baseUrl):
    all_months_data = download_all_data(baseUrl)
    for i in range(365):
        plot_single_day(i,all_months_data)


