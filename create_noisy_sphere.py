# https://stackoverflow.com/questions/47485235/i-want-to-make-evenly-distributed-sphere-in-vtk-python

# https://docs.pyvista.org/version/stable/


import numpy as np
import pyvista as pv
import random

import mycommon

num_pts = 1000
indices = np.arange(0, num_pts, dtype=float) + 0.5

phi = np.arccos(1 - 2*indices/num_pts)
theta = np.pi * (1 + 5**0.5) * indices

R=2
# random error
sigma = 0.1


x =  R*np.cos(theta) * np.sin(phi) * (1  + random.gauss(0, sigma) )
y =  R*np.sin(theta) * np.sin(phi) * (1  + random.gauss(0, sigma) )
z =  R*np.cos(phi)                 * (1  + random.gauss(0, sigma) )

point_cloud = pv.PolyData(np.c_[x, y, z])
surface = point_cloud.delaunay_3d().extract_surface()
surface.plot(show_edges=True, color=True, show_grid=True)

##
outfile=  mycommon.output_dir + "/noisy_sigma=" + str(sigma) +  "_sphere_R=" + str(R) 
##------------------------

fout= outfile +  ".stl"
surface.save(fout)

print("Stl file written to ", fout)

# direct write of point cloud

dim = len(x)
points = np.zeros((dim, 3))

points[:,0] = x
points[:,1] = y
points[:,2] = z


np.save(outfile, points)
print('Point cloud saved to ', outfile + ".npy")
