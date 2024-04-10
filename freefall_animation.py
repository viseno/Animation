import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib.animation as animate
import numpy as np

#Time component
t0 = 0
t_end = 12
dt = 0.02
t = np.arange(t0,t_end+dt,dt)

#Free fall component 
gE = 9.8
gM = 3.7
gMo = 1.6
y_i = 100
n = 2

def free_fall(initial_y,gravity):
    y_pos = initial_y -1/2*gravity*t**2
    v = -2*1/2*gravity*t**(2-1)
    a = -2*(2-1)*1/2*gravity*t**(2-2)
    return y_pos,v,a

y_pos_1,v_1,a_1 = free_fall(y_i,gE)
y_pos_2,v_2,a_2 = free_fall(y_i,gM)
y_pos_3,v_3,a_3 = free_fall(y_i,gMo)

##### ini rumus kalo mau manual #####
# y_pos_1 = y_i -1/2*gE*t**n
# v_1 = -n*1/2*gE*t**(n-1)
# a_1 = -n*(n-1)*1/2*gE*t**(n-2)

# y_pos_2 = y_i -1/2*gM*t**n
# v_2 = -n*1/2*gM*t**(n-1)
# a_2 = -n*(n-1)*1/2*gM*t**(n-2)

# y_pos_3 = y_i -1/2*gMo*t**n
# v_3 = -n*1/2*gMo*t**(n-1)
# a_3 = -n*(n-1)*1/2*gMo*t**(n-2)
##### ini rumus kalo mau manual #####

#Circle component
rad_E = 5
rad_M = 5
rad_Mo = 5

def ling_maker(a):
    lingkaran = np.arange(0,361,1)
    lingkaran_rad = lingkaran*np.pi/180
    ling_x = a * np.cos(lingkaran_rad)
    ling_y = a * np.sin(lingkaran_rad)
    return ling_x, ling_y

ling_x_1, ling_y_1 = ling_maker(rad_E)
ling_x_2, ling_y_2 = ling_maker(rad_M)
ling_x_3, ling_y_3 = ling_maker(rad_Mo)

#Animation
frame_count = len(t)
radius = 5
clearance_x = 1.3
clearance_y = 10
xtick_1 = np.arange(-rad_E,rad_E+1,5)
ytick_1 = np.arange(-clearance_y,clearance_y+y_i+1,clearance_y)

fig = plt.figure(figsize=(12,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs1 = gs.GridSpec(3,4)

def circle(pt):
    #Subplot 1
    if (y_pos_1[pt] >= rad_E) :    
        circle1_motion.set_data(ling_x_1,ling_y_1+y_pos_1[pt])
        v1_ani.set_data(t[0:pt],v_1[0:pt])
        a1_ani.set_data(t[0:pt],a_1[0:pt])
    if (y_pos_1[pt] >= 0) :
        y_pos1_ani.set_data(t[0:pt],y_pos_1[0:pt])
        

    #Subplot 2
    if (y_pos_2[pt] >= rad_M) :
        circle2_motion.set_data(ling_x_2,ling_y_2+y_pos_2[pt])
        v2_ani.set_data(t[0:pt],v_2[0:pt])
        a2_ani.set_data(t[0:pt],a_2[0:pt])
    if (y_pos_2[pt] >=0) :
        y_pos2_ani.set_data(t[0:pt],y_pos_2[0:pt])
        
    #Subplot 3
    if (y_pos_3[pt] >= rad_Mo) :
        circle3_motion.set_data(ling_x_3,ling_y_3+y_pos_3[pt])
        v3_ani.set_data(t[0:pt],v_3[0:pt])
        a3_ani.set_data(t[0:pt],a_3[0:pt])
    if (y_pos_3[pt] >= 0) :
        y_pos3_ani.set_data(t[0:pt],y_pos_3[0:pt])
        

    return circle1_motion,circle2_motion,circle3_motion,y_pos1_ani,y_pos2_ani,y_pos3_ani,v1_ani,v2_ani,v3_ani,\
    a1_ani,a2_ani,a3_ani

#Subplot 1
ax0 = fig.add_subplot(gs1[:,0])
circle1_motion, = ax0.plot([],[],"k",linewidth = 2)
subplot1_land = ax0.plot([-5,5],[-5,-5],"-b",linewidth = 38)
plt.ylabel("y[m]")
plt.title("Earth")
plt.title("By Alfred Setiawan", loc= "left", fontsize = 6)
plt.xlim(-rad_E*clearance_x,rad_E*clearance_x)
plt.ylim(-clearance_y,y_i+clearance_y)
plt.xticks(xtick_1)
plt.yticks(ytick_1)
plt.grid(True)

#Subplot 2
ax1 = fig.add_subplot(gs1[:,1])
circle2_motion, = ax1.plot([],[],"k",linewidth = 2)
subplot2_land = ax1.plot([-5,5],[-5,-5],"orange", linewidth = 38)
plt.title("Mars")
plt.xlim(-rad_M*clearance_x,rad_M*clearance_x)
plt.ylim(-clearance_y,y_i+clearance_y)
plt.xticks(np.arange(-rad_M,rad_M+1,5))
plt.yticks(np.arange(-clearance_y,clearance_y+y_i+1,clearance_y))
plt.grid(True)

#Subplot 3
ax2 = fig.add_subplot(gs1[:,2])
circle3_motion, = ax2.plot([],[],"k",linewidth = 2)
subplot2_land = ax2.plot([-5,5],[-5,-5],"grey", linewidth = 38)
plt.title("Moon")
plt.xlim(-rad_Mo*clearance_x,rad_Mo*clearance_x)
plt.ylim(-clearance_y,y_i+clearance_y)
plt.xticks(np.arange(-rad_Mo,rad_Mo+1,5))
plt.yticks(ytick_1)
plt.grid(True)

#Subplot 4
ax3 = fig.add_subplot(gs1[0,3])
y_pos1_ani, = ax3.plot([],[],"-b",linewidth = 2, label = "y position Earth = " + str(y_i) + " - " + str(1/2*gE) + "t^2[m]")
y_pos2_ani, = ax3.plot([],[],"orange", linewidth = 2, label = "y position Mars= " + str(y_i) + " - " + str(1/2*gM) + "t^2[m]")
y_pos3_ani, = ax3.plot([],[],"grey", linewidth = 2, label = "y position Moon= " + str(y_i) + " - " + str(1/2*gMo) + "t^2[m]")
plt.xlim(t[0],t[-1])
plt.ylim(0,y_pos_1[0])
plt.xticks(np.arange(t[0],t[-1]+1,t[-1]/6))
plt.yticks(np.arange(0,y_i + 1, y_i/5))
plt.legend(loc = "upper right", fontsize = 4)

#Subplot 5
ax4 = fig.add_subplot(gs1[1,3])
v1_ani, = ax4.plot([],[],"-b",linewidth = 2, label = "v on Earth = " + str(-gE) + "t [m/s]" ) 
v2_ani, = ax4.plot([],[],"orange", linewidth = 2, label = "v on Mars = " + str(-gM) + "t [m/s]" )
v3_ani, = ax4.plot([],[],"grey", linewidth = 2, label = "v on Moon = " + str(-gMo) + "t [m/s]" )
plt.xlim(t[0],t[-1])
plt.ylim(v_1[-1],v_1[0]+1)
plt.xticks(np.arange(t[0],t[-1]+1,t[-1]/6))
plt.yticks(np.arange(-120,21,20)) # kalo mau bagi 5 sama rata(v_1[0]-v_1[-1])/5)
plt.legend(loc = "upper right", fontsize = 4)

#Subplot 6
ax5 = fig.add_subplot(gs1[2,3])
a1_ani, = ax5.plot([],[],"-b",linewidth = 2, label = "a on Earth = " + str(-gE) + "[m/s^2]")
a2_ani, = ax5.plot([],[],"orange", linewidth = 2, label = "a on Mars = " + str(-gM) + "[m/s^2]")
a3_ani, = ax5.plot([],[],"grey",linewidth = 2, label = "a on Moon = " + str(-gMo) + "[m/s^2]")
plt.xlim(t[0],t[-1])
plt.ylim(a_1[0],0)
plt.xticks(np.arange(t[0],t[-1]+1,t[-1]/6))
plt.yticks(np.arange(-12,3,2))
plt.legend(loc = "upper right", fontsize = 4)
plt.xlabel("time [hours]")

plt.tight_layout()

circle1_ani = animate.FuncAnimation(fig,circle,frames=frame_count, interval = 2, repeat = True, blit =True)

plt.show()

