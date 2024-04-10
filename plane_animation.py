import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib.animation as ani
import numpy as np

#time component
t0 = 0
t_end = 2
dt = 0.005
t = np.arange(t0,t_end+dt,dt)

#x component
a = 400
b = 2
x = a*t**b

#y component
height = 2
y = np.ones(len(t)) * 2

#speed component
if  b < 1 :
    t[0] = t[1]
speed = b*a*t**(b-1)

#Animation
frame_count = int(len(t))

mark_ax0 = np.zeros(frame_count)
n = 20
for i in range(0,frame_count):
    if i == n:
        mark_ax0[i] = x[i]
        n = n +20
    else:
        mark_ax0[i] = x[n-20]

def animate(pt):
    #subplot 1
    plane_traj.set_data(mark_ax0[0:pt+1], y[0:pt+1])
    plane_ground.set_data([x[pt],x[pt]],[0,y[pt]])
    plane_part1.set_data([x[pt]-40,x[pt]+20],[y[pt],y[pt]])
    plane_part2.set_data([x[pt]-20,x[pt]],[y[pt]+0.3,y[pt]])
    plane_part3.set_data([x[pt]-20,x[pt]],[y[pt]-0.3,y[pt]])
    plane_part4.set_data([x[pt]-35,x[pt]-25],[y[pt]+0.15,y[pt]])
    plane_part5.set_data([x[pt]-35,x[pt]-25],[y[pt]-0.15,y[pt]])
    time_counter_ax0.set_text(str(round(t[pt],1)) + " hours")
    x_counter_ax0.set_text(str(int(x[pt])) + " km")

    #subplot 2
    x_vs_time.set_data(t[0:pt],x[0:pt])
    h_line.set_data([t[0],t[pt]],[x[pt],x[pt]])
    v_line.set_data([t[pt],t[pt]],[0,x[pt]])

    #subplot 3
    speed_line.set_data(t[0:pt],speed[0:pt])
    speed_ground.set_data([t[pt],t[pt]],[0,speed[pt]])
    speed_text.set_text(str(round(speed[pt],1)) + "km/hours") 

    return plane_traj,plane_ground,plane_part1,plane_part2,plane_part3,plane_part4,plane_part5, time_counter_ax0, x_counter_ax0,x_vs_time, h_line,v_line,speed_line,speed_ground,speed_text

plt.style.use("ggplot")
fig =plt.figure(figsize=(12,8), dpi= 120, facecolor=(0.8,0.8,0.8))
gs1 = gs.GridSpec(2,2)

#subplot 1
x_tick = np.arange(x[0],x[-1]+1,x[-1]/4)
y_tick = np.arange(0,y[-1]+2,1)

ax0 = fig.add_subplot(gs1[0,:])
plane_traj, = ax0.plot([],[],"r:o",linewidth = 2)
plane_ground, = ax0.plot([],[],"k:o",linewidth = 2)
plane_part1, = ax0.plot([],[],"k",linewidth = 10)
plane_part2, = ax0.plot([],[],"k", linewidth = 4)
plane_part3,= ax0.plot([],[],"k", linewidth = 4)
plane_part4, = ax0.plot([],[],"k", linewidth = 4)
plane_part5, = ax0.plot([],[],"k", linewidth = 4)
building_1, = ax0.plot([150,150],[0,0.5],"k",linewidth = 3)
building_2, = ax0.plot([400,400],[0,0.7],"k", linewidth = 5)
building_4, = ax0.plot([750,750],[0,1],"k", linewidth = 4)
building_5, = ax0.plot([1300,1350],[0,0.7],"k", linewidth = 7)

box_time_ax0 = dict(boxstyle = "circle", lw = 1, ec = "red")
time_counter_ax0 = ax0.text(1400,0.5,"", fontsize = 10, bbox = box_time_ax0)

box_x_ax0 = dict(boxstyle = "square", ec ="k", lw =1)
x_counter_ax0 = ax0.text(900,0.5,"",size = 20, bbox = box_x_ax0)

plt.xticks(x_tick, ["0 km","400 km","800 km", "1200 km","1600 km"])
plt.yticks(y_tick, ["0 km", "1 km","2 km","3 km"]) 
plt.xlabel("x-distance")
plt.ylabel("y-distance")
plt.title("Airplane Animation")
plt.title("By Alfred Setiawan", loc="left", fontsize = 9)
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0] + 1)
plt.grid(True)

#subplot 2
sub2_xticks = np.arange(t[0],t[-1]+dt,t[-1]/4)
sub2_yticks = np.arange(x[0],x[-1]+1,x[-1]/4)

ax1 = fig.add_subplot(gs1[1,0])
x_vs_time, = ax1.plot([],[],"-b",linewidth = 4, label = "x vs time")
h_line, = ax1.plot([],[],"r:o", linewidth = 2, label = "x")
v_line, = ax1.plot([],[],"g:o", linewidth = 2, label = "time")

plt.xticks(sub2_xticks)
plt.yticks(sub2_yticks)
plt.xlim(t[0],t[-1])
plt.ylim(x[0],x[-1])
plt.xlabel("time(hours)")
plt.ylabel("x-distance(km)")
plt.legend(loc = "upper left", fontsize = 10)
plt.grid(True)
plt.title("time vs x-distance")

#subplot 3
sub3_xticks = np.arange(t[0],t[-1]+dt,t[-1]/4)
sub3_yticks = np.arange(0,speed[-1]*2+1,speed[-1]*2/4)

ax2 = fig.add_subplot(gs1[1,1])
speed_line, = ax2.plot([],[],"-b",linewidth = 4, label = "speed")
speed_ground, = ax2.plot([],[],"b:o",linewidth = 2,label ="time")

speed_text = ax2.text(1.4,speed[-1]*0.2,"", fontsize = 10)

plt.xlim(t[0],t[-1])
plt.ylim(0,speed[-1])
plt.xticks(sub3_xticks)
plt.yticks(sub3_yticks)
plt.xlabel("time(hours)")
plt.ylabel("speed(km/h)")
plt.grid(True)
plt.title("time vs speed")
plt.legend(loc="upper left")

plane_ani = ani.FuncAnimation(fig,animate,frames= frame_count, interval = 2, blit = True, repeat = True)

plt.show()


