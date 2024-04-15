import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import matplotlib.animation as ani

#time component
t0 = 0
t_end = 60
dt = 0.02
t = np.arange(t0,t_end+dt,dt)

water_tank1 = np.zeros(len(t))
volume_Tank2= np.zeros(len(t))
volume_Tank3 = np.zeros(len(t))
ymax = 100

#water tank 1
for i in range(len(t)):
    if t[i] <= 22.5 :
        water_tank1[i] = 50 + 2*t[i]
        time = t[i]
    elif (t[i] <= 32.5) & (t[i] > 22.5):
        water_tank1[i] = 95
        time1 = t[i]
    elif (t[i] <= 32.5 + np.sqrt(45)) & (t[i] > 32.5):
        water_tank1[i] = 95 - (t[i]-time1)**2
        time2 = t[i]
    elif (t[i] <= 42.5 + np.sqrt(45)) & (t[i] > 32.5 + np.sqrt(45)):
        water_tank1[i] = 50 + 1 * np.sin(2*np.pi*1*(t[i]-(time2)))
    else:
        water_tank1[i] = 50

 #water tank 2
    if t[i]<=27.5:
        volume_Tank2[i]=40+2*t[i]
    elif t[i]<=32.5:
        volume_Tank2[i]=95
        temp21=i
    elif t[i]<=32.5+45**0.5:
        volume_Tank2[i]=95-(t[i]-t[temp21])**2
        temp22=i
    elif t[i]<=37.5+45**0.5:
        volume_Tank2[i]=50+3*np.sin(2*np.pi*1*(t[i]-t[temp22]))
        temp23=i
    elif t[i]<=42.5+45**0.5:
        volume_Tank2[i]=50+np.sin(2*np.pi*2*(t[i]-t[temp23]))
    else:
        volume_Tank2[i]=50


#wank 3
    if t[i]<=32.5:
        volume_Tank3[i]=30+2*t[i]
        temp31=i
    elif t[i]<=32.5+45**0.5:
        volume_Tank3[i]=95-(t[i]-t[temp31])**2
        temp32=i
    elif t[i]<=42.5+45**0.5:
        volume_Tank3[i]=50-np.sin(2*np.pi*1*(t[i]-t[temp32]))
    else:
        volume_Tank3[i]=50

#Animation
frame_num = len(t)
fig = plt.figure(figsize=(12,9), facecolor=(0.9,0.9,0.9))
gs1 = gs.GridSpec(2,3)

def wateranimation(pt):
    tank1_line.set_data([-radius,radius],[water_tank1[pt],water_tank1[pt]])
    # tank1_water.set_data([0,0],[0,water_tank1[pt]-0.5])
    #Alt 2
    tank1_water.set_height(water_tank1[pt])

    tank2_line.set_data([-radius,radius],[volume_Tank2[pt],volume_Tank2[pt]])
    tank2_water.set_data([0,0],[0,volume_Tank2[pt]-0.5])

    tank3_line.set_data([-radius,radius],[volume_Tank3[pt],volume_Tank3[pt]])
    tank3_water.set_data([0,0],[0,volume_Tank3[pt]-0.5])

    tank1_subplot4.set_data(t[0:pt],water_tank1[0:pt])
    tank2_subplot4.set_data(t[0:pt],volume_Tank2[0:pt])
    tank3_subplot4.set_data(t[0:pt],volume_Tank3[0:pt])

    tank1_subplot5.set_data(t[0:pt],water_tank1[0:pt])
    tank2_subplot5.set_data(t[0:pt],volume_Tank2[0:pt])
    tank3_subplot5.set_data(t[0:pt],volume_Tank3[0:pt])


    return tank1_line,tank1_water,tank2_line,tank2_water,tank3_line,tank3_water,tank1_subplot4,tank2_subplot4,tank3_subplot4,\
    tank1_subplot5,tank2_subplot5,tank3_subplot5

radius = 5

#Subplot 1
ax0 = fig.add_subplot(gs1[0,0])
tank1_line, = ax0.plot([],[],"red",linewidth = 3)
# tank1_water, = ax0.plot([],[],"-b",linewidth = 250,solid_capstyle ="butt")
#Alt 2 making animation tank1_water 
tank1_water = plt.Rectangle([-5,0],10,0,facecolor = "blue")
ax0.add_patch(tank1_water)

plt.xlim(-radius,radius)
plt.ylim(0,100)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(0,ymax+1,10))
plt.title("Tank 1")
plt.ylabel("tank volume [m^3]") 

#Subplot 2
ax1 = fig.add_subplot(gs1[0,1])
tank2_line, = ax1.plot([],[],"red",linewidth = 3)
tank2_water, = ax1.plot([],[],"-b",linewidth = 250,solid_capstyle = "butt")
plt.xlim(-radius,radius)
plt.ylim(0,100)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(0,ymax+1,10))
plt.title("Tank 2")
plt.ylabel("tank volume [m^3]") 

#Subplot 3
ax2 = fig.add_subplot(gs1[0,2])
tank3_line, = ax2.plot([],[],"red",linewidth = 3)
tank3_water, = ax2.plot([],[],"-b",linewidth = 250,solid_capstyle = "butt")
plt.xlim(-radius,radius)
plt.ylim(0,100)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(0,ymax+1,10))
plt.title("Tank 3")
plt.ylabel("tank volume [m^3]") 

#Subplot 4
ax3 = fig.add_subplot(gs1[1,0:2])
tank1_subplot4, = ax3.plot([],[],"-b",linewidth = 3,label = "Tank 1")
tank2_subplot4, = ax3.plot([],[],"green",linewidth = 3,label = "Tank 2")
tank3_subplot4, = ax3.plot([],[],"red",linewidth = 3,label = "Tank 3")
plt.xlim(t[0],t[-1])
plt.ylim(0,100)
plt.xticks([0,22.5,27.5,32.5,32.5+45**0.5,37.5+45**0.5,42.5+45**0.5,60])
plt.yticks(np.arange(0,101,10))
plt.ylabel("tank volume[m^3]")
plt.legend(bbox_to_anchor=(1,1))
plt.grid(True)

#Subplot 5
ax4 = fig.add_subplot(gs1[1,2])
tank1_subplot5, = ax4.plot([],[],"-b",linewidth = 3)
tank2_subplot5, = ax4.plot([],[],"green",linewidth = 3)
tank3_subplot5, = ax4.plot([],[],"red",linewidth = 3)
plt.xlim(0.9*39.2,1.1*49.2)
plt.ylim(47,53)
plt.xticks([0,22.5,27.5,32.5,32.5+45**0.5,37.5+45**0.5,42.5+45**0.5,60])
plt.yticks(np.arange(0,101,10))
plt.axis([38,50,47,53])
plt.grid(True)

watertank_animation = ani.FuncAnimation(fig,wateranimation,interval = 2,blit = True,repeat = True, frames= frame_num)

plt.show()