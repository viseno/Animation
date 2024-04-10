import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.gridspec as gs

#time component
t0 = 0
t_end = 16
dt = 0.05
t = np.arange(t0,t_end+dt,dt)

#horizontal moving cart
def sin_motion(amplitude,freq,time):
    degrees = 2*np.pi*freq*time
    sin_mo = amplitude*np.sin(degrees)
    return sin_mo

def cos_motion(amplitude,freq,time):
    degree = 2*np.pi*freq*time
    cos_mo = amplitude*np.cos(degree)
    return cos_mo

amp_b = 7
freq_b = 0.125
blue_cart = sin_motion(amp_b,freq_b,t)

amp_r = -7
freq_r = 0.125
red_cart = cos_motion(amp_r,freq_r,t)

#vertical moving cart
purple_cart = 13-2*(t-6)
green_cart = 13-2*(t-2)**2

#Animation
frame_num = len(t)
yi = 13

fig = plt.figure(figsize=(12,9),dpi=120,facecolor=(0.7,0.7,0.7))
gs1 = gs.GridSpec(2,2)

def motion(pt):
    #Subplot 1
    blue_motion.set_data(t[0:pt],blue_cart[0:pt])
    red_motion.set_data(t[0:pt],red_cart[0:pt])
    #Subplot 2 and 3
    blue_cart_motion.set_data([blue_cart[pt]-0.4,blue_cart[pt]+0.6],[3.5,3.5])
    red_cart_motion.set_data([red_cart[pt]-0.4,red_cart[pt]+0.6],[1.5,1.5])
    if t[pt] >= 2:
        green_cart_motion.set_data([3.5,3.5],[green_cart[pt]-0.4,green_cart[pt]+0.6])
        green_motion.set_data(t[int(2/dt):pt],green_cart[int(2/dt):pt])
    else:
        green_motion2.set_data(t[0:pt],yi)
        green_cart_motion.set_data([3.5,3.5],[yi-0.4,yi+0.6])
    if t[pt] >= 6:
        purple_cart_motion.set_data([-3.5,-3.5],[purple_cart[pt]-0.4,purple_cart[pt]+0.6])
        purple_motion.set_data(t[int(6/dt):pt],purple_cart[int(6/dt):pt])
    else:
        purple_cart_motion.set_data([-3.5,-3.5],[yi-0.4,yi+0.6])
        purple_motion2.set_data(t[0:pt],yi)
    return green_motion2,purple_motion2,blue_motion,red_motion,purple_motion,green_motion,blue_cart_motion,red_cart_motion,green_cart_motion,purple_cart_motion

#Subplot 1
ax1 =fig.add_subplot(gs1[0,0])
blue_motion, = ax1.plot([],[],"-b",linewidth = 3, label = "X_blue = " + str(amp_b) + "* sin(2pi*" + str(freq_b) + "*t)")
red_motion, = ax1.plot([],[],"red",linewidth = 3, label = "X_red = " + str(-amp_b) + "* cos(2pi*" + str(freq_b) + "*t)")
plt.xlim(0,t[-1])
plt.ylim(-amp_b-1,amp_b+1)
plt.xlabel("time[s]")
plt.ylabel("X[m]")
ax1.spines["bottom"].set_position("center")
ax1.xaxis.set_label_coords(0.5,0)
plt.legend(bbox_to_anchor = (1,1.15), fontsize = "medium")
plt.title("By Alfred Setiawan", loc="left", fontsize = 8)
plt.grid(True)

#Subplot 2
ax2 = fig.add_subplot(gs1[1,0])
green_motion, = ax2.plot([],[],"green",linewidth = 3)
green_motion2, = ax2.plot([],[],"g",linewidth = 3, alpha = 0.4)
purple_motion, = ax2.plot([],[],"purple",linewidth = 3)
purple_motion2, = ax2.plot([],[],"purple",linewidth = 3, alpha = 0.4)
plt.xlim(t[0],t[-1])
plt.ylim(-2,14)
plt.xticks(np.arange(t[0],t[-1]+1,2))
plt.yticks(np.arange(-2,t[-1],2))
plt.grid(True)
plt.xlabel("time[s]")
plt.ylabel("Y[m]")
ax2.spines["bottom"].set_position(("data",0))
ax2.xaxis.set_label_coords(0.5,0)

#Subplot 3
ax3 = fig.add_subplot(gs1[:,1])
blue_cart_motion, = ax3.plot([],[],"-b",linewidth = 28)
red_cart_motion, = ax3.plot([],[],"red",linewidth = 28)
green_cart_motion, = ax3.plot([],[],"g",linewidth = 26)
purple_cart_motion, = ax3.plot([],[],"purple",linewidth = 26)

purple_box = dict(boxstyle = "square", lw = 2, ec = "purple", fc = "white")
purple_text = ax3.text(-5,14.5,"13-2*(t-6)",color = "purple",bbox = purple_box)

green_box = dict(boxstyle = "square", lw = 2, ec = "green", fc = "white")
green_text = ax3.text(2,14.5,"13-2*(t-2)^2",color = "green", bbox = green_box)
#Crash zone 1 
crash_zone1_1 = ax3.plot([-4,-3],[3,3],"yellow",linewidth = 3)
crash_zone1_2 = ax3.plot([-4,-3],[4,4],"yellow",linewidth = 3)
crash_zone1_3 = ax3.plot([-4,-4],[3,4],"yellow",linewidth = 3)
crash_zone1_4 = ax3.plot([-3,-3],[3,4],"yellow",linewidth = 3)
#Crash zone 2
crash_zone2_1 = ax3.plot([-4,-3],[1,1],"yellow",linewidth = 3)
crash_zone2_2 = ax3.plot([-4,-3],[2,2],"yellow",linewidth = 3)
crash_zone2_3 = ax3.plot([-4,-4],[1,2],"yellow",linewidth = 3)
crash_zone2_4 = ax3.plot([-3,-3],[1,2],"yellow",linewidth = 3)
#Crash zone 3
crash_zone3_1 = ax3.plot([3,4],[3,3],"yellow",linewidth = 3)
crash_zone3_2 = ax3.plot([3,4],[4,4],"yellow",linewidth = 3)
crash_zone3_3 = ax3.plot([3,3],[3,4],"yellow",linewidth = 3)
crash_zone3_4 = ax3.plot([4,4],[3,4],"yellow",linewidth = 3)
#Crash zone 4
crash_zone4_1 = ax3.plot([3,4],[1,1],"yellow",linewidth = 3)
crash_zone4_2 = ax3.plot([3,4],[2,2],"yellow",linewidth = 3)
crash_zone4_3 = ax3.plot([3,3],[1,2],"yellow",linewidth = 3)
crash_zone4_4 = ax3.plot([4,4],[1,2],"yellow",linewidth = 3)

plt.xlim(-1-amp_b,amp_b+1)
plt.ylim(-2,14)
plt.xticks(np.concatenate([np.arange(-1-amp_b,0,1),np.arange(1,amp_b+2,1)]))
plt.yticks(np.concatenate([np.arange(-2,0,1),np.arange(1,15,1)]))
plt.xlabel("x position[m]")
plt.ylabel("y position[m]")
ax3.spines["left"].set_position("center")
ax3.spines["bottom"].set_position(("data",0))
ax3.xaxis.set_label_coords(0.5,-0.01)
ax3.yaxis.set_label_coords(0,0.5)
plt.grid(True)
plt.tight_layout()

sin_cos_ani = ani.FuncAnimation(fig,motion, frames= frame_num,interval = 20, blit = True, repeat = True)

plt.show()
