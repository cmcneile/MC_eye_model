# https://stackoverflow.com/questions/47485235/i-want-to-make-evenly-distributed-sphere-in-vtk-python

# https://docs.pyvista.org/version/stable/

#
#  https://mathworld.wolfram.com/Ellipsoid.html
#

a = 1
b = 2
c = 3

print("Parameters of Ellipsoid")
print("a = ", a)
print("b = ", b)
print("c = ", c)

import numpy as np
import pyvista as pv

num_pts = 1000
indices = np.arange(0, num_pts, dtype=float) + 0.5

phi = np.arccos(1 - 2*indices/num_pts)
theta = np.pi * (1 + 5**0.5) * indices

x =  a*np.cos(theta) * np.sin(phi) 
y =  b*np.sin(theta) * np.sin(phi)
z =  c*np.cos(phi)

point_cloud = pv.PolyData(np.c_[x, y, z])
surface = point_cloud.delaunay_3d().extract_surface()
surface.plot(show_edges=True, color=True, show_grid=True)

fout="ellipsoid_a=" + str(a) + "_b=" + str(b) + "_c=" + str(c) + ".stl"
surface.save(fout)

print("stl file written to ", fout)

