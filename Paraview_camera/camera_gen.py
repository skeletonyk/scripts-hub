import numpy as np
import math
import scipy.integrate as integrate
from scipy.integrate import odeint

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



# ---- The thing u need to change according to the input file -----
def rot_vec(time):
    time += 0.0000000001 
    # just to avoid all 0 case for calculating the view_up angle
    return np.array([np.pi/10 * math.sin(0.6 * time), 0, 0])
# -----------------------------------------------------------------

def func(y, t):
    return(np.cross(-rot_vec(t), y))

def write_head():
    f.write("""
### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1872, 947]

# get camera animation track for the view
cameraAnimationCue1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame""")
    return 0

# Main -------------------------------------------------------------
# Things u need to modify~
Unit_tot = 22000
output_fre = 128
step_length = 0.001
tot_unit = int(Unit_tot / output_fre)

cam_tran = np.array([2, 0, 0])
center_rot = np.array([20 , 20, 20])
camera_dist = 4.5
cam_0 = np.array([0.5, math.sin(math.pi/6), -math.cos(math.pi/6)]) * camera_dist

# Solving ODE for camera position~  --------------------------------
t = [i*output_fre*step_length for i in range(0, tot_unit + 1)]
cam_vec = odeint(func, cam_0, t)

# Specify view_up_0
view_up_0 = np.cross(np.abs(rot_vec(0)), cam_vec[0])
view_up = odeint(func, view_up_0, t)
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# writing eveything~
f = open('camera_sine.py', 'w')
write_head()

for i in range(0, tot_unit + 1):
    frame_nu = 5000 + i
    key_t_perc = float(i) /tot_unit 
    time = i*output_fre*step_length
    # ------------------------ 
    camera = center_rot + cam_vec[i] + cam_tran 


    f.write(
"""
# ====================================================================
keyFrame{frame_nu} = CameraKeyFrame()
keyFrame{frame_nu}.KeyTime = {key_t_perc}
keyFrame{frame_nu}.KeyValues = [0.0]
keyFrame{frame_nu}.Position = {camera}
keyFrame{frame_nu}.FocalPoint = {focus}
keyFrame{frame_nu}.ViewUp = {view_up}
keyFrame{frame_nu}.ViewAngle = 30.0
keyFrame{frame_nu}.ParallelScale = 0.97681
keyFrame{frame_nu}.PositionPathPoints = {camera}
keyFrame{frame_nu}.FocalPathPoints = {focus}
keyFrame{frame_nu}.PositionMode = 'Path'
keyFrame{frame_nu}.FocalPointMode = 'Path'
keyFrame{frame_nu}.ClosedFocalPath = 0
keyFrame{frame_nu}.ClosedPositionPath = 0
""".format(frame_nu = frame_nu, key_t_perc = key_t_perc, camera = camera.tolist(), focus = (center_rot + cam_tran).tolist(), view_up = view_up[i].tolist()) )

# Finalization
temp = list((sorted("keyFrame{}".format(s) for s in range(5000, 5000+tot_unit+1))))
temp = '[%s]' % ', '.join(map(str, temp))

f.write('''
# initialize the animation track
cameraAnimationCue1.TimeMode = 'Normalized'
cameraAnimationCue1.StartTime = 0.0
cameraAnimationCue1.EndTime = 1.0
cameraAnimationCue1.Enabled = 1
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.KeyFrames = {}
cameraAnimationCue1.DataSource = None
'''.format(temp ))

f.close()


# Plot --------------------------------------------------------------
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
cam_plot = center_rot + cam_vec + cam_tran
ax.plot(cam_plot[:,0], cam_plot[:, 1], cam_plot[:, 2], label='camera vector')
ax.legend()

plt.show()
