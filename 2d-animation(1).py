import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.gridspec as gs

t0 = 0
t_end = 12
dt = 0.02
t = np.arange(t0,t_end+dt,dt)

#x component
a = 1500
b = 600
# x_movement = a + b*t
x_movement = (a+40*t) + (b+20*t) * np.sin(2*np.pi*0.1*t*t)

#y component
c = 800
d = -400
# y_movement = c + d*t
y_movement = (c+40*t) + (d+20*t) * np.cos(2*np.pi*0.5*t*t)

#Animation
frame_num = len(t)

def movement(pt):
    #Subplot 1
    plane_1.set_data([x_movement[pt]-40,x_movement[pt]+60],[y_movement[pt],y_movement[pt]])
    plane_2.set_data([x_movement[pt]+5,x_movement[pt]+10],[y_movement[pt]+25,y_movement[pt]+8])
    plane_3.set_data([x_movement[pt]-25,x_movement[pt]-20],[y_movement[pt]+25,y_movement[pt]+8])
    plane_traj.set_data(x_movement[0:pt],y_movement[0:pt])
    arrow_1 = ax1.arrow(0,0,a,c,length_includes_head = True,head_width = 40,head_length = 80, color = "g", linewidth =2)
    arrow_2 = ax1.arrow(0,0,x_movement[pt],y_movement[pt],length_includes_head = True,head_width = 40,head_length = 80, color = "g", linewidth =2)
    arrow_3 = ax1.arrow(a,c,x_movement[pt]-a,y_movement[pt]-c,length_includes_head = True,head_width = 40,head_length = 80, color = "blue", linewidth =2)
    arrow_4 = ax1.arrow(a,c,x_movement[pt]-a,0,length_includes_head = True,head_width = 40,head_length = 80, color = "red", linewidth =2)
    arrow_5 = ax1.arrow(x_movement[pt],c,0,y_movement[pt]-c,length_includes_head = True,head_width = 40,head_length = 80, color = "red", linewidth =2)

    #Subplot 2
    line2_blue.set_data(t[0:pt],x_movement[0:pt])
    arrow2_red = ax2.arrow(t[pt],a,0,x_movement[pt]-a,length_includes_head = True,head_width = 0.2,head_length = 100, color = "red", linewidth =2) 

    #Subplot 3
    line3_blue.set_data(t[0:pt],y_movement[0:pt])
    arrow3_red = ax3.arrow(t[pt],c,0,y_movement[pt]-c,length_includes_head = True,head_width = 0.2,head_length = 100, color = "red", linewidth =2)

    return plane_1,plane_2,plane_3,plane_traj,arrow_1,arrow_2,arrow_3,arrow_4,arrow_5,line2_blue,line3_blue,arrow2_red,arrow3_red

fig = plt.figure(figsize=(12,9), facecolor=(0.9,0.9,0.9))
gs1 = gs.GridSpec(2,2)

#Subplot 1
ax1 = fig.add_subplot(gs1[0,:])
plane_1, = ax1.plot([],[],"-k",linewidth = 7)
plane_2, = ax1.plot([],[],"-k",linewidth = 5)
plane_3, = ax1.plot([],[],"-k",linewidth = 5)
plane_traj, = ax1.plot([],[],"--k",linewidth = 2)
plt.xlim(0,3000)
plt.ylim(0,1500+100)
# plt.ylim(0,c*+100)
plt.xticks(np.arange(0,3001,500))
plt.yticks(np.arange(0,1601,200))
plt.xlabel("position-x [m]")
plt.ylabel("position-y [m]")
plt.grid(True)

#Subplot 2
ax2 = fig.add_subplot(gs1[1,0])
line2_blue, = ax2.plot([],[],"-b",linewidth = 2) #label = "X =" + str(a) + " + " + str(b) + "t")
plt.xlim(t[0],t[-1])
plt.ylim(0,3000)
plt.xticks(np.arange(t[0],t[-1]+dt,2))
plt.yticks(np.arange(0,3001,500))
plt.xlabel("time [s]")
plt.ylabel("position-x [m]")
plt.legend(bbox_to_anchor =(0.98,0.15))
plt.grid(True)


#Subplot 3
ax3 = fig.add_subplot(gs1[1,1])
line3_blue, = ax3.plot([],[],"-b",linewidth = 2) #label = "X =" + str(c) + " + " + str(d) + "t")
plt.xlim(t[0],t[-1])
plt.ylim(0,1500+100)
plt.xticks(np.arange(t[0],t[-1]+dt,2))
plt.yticks(np.arange(0,1500+101,200))
plt.xlabel("time [s]")
plt.ylabel("position-y [m]")
plt.legend(bbox_to_anchor =(0.98,0.15))
plt.grid(True)

animation_code = ani.FuncAnimation(fig,movement,frames=frame_num,interval = 20, blit = True, repeat = True)

plt.show()