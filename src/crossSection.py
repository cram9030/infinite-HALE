import numpy as np
import geom.cuboct

vox_pitch = 0.0762 #m
cord = 2*0.3048 #m

#Create 2-D bounding box for voxelization
#Estimate number of voxels in cord length
size_x = round(cord/vox_pitch);
size_y = round(0.3*size_x);

mat_matrix = []

for i in range(0,size_y):
    temprow = []
    for j in range(0,size_x):
        #This is just temporary it will be replaced with intertools.permutations later
        if (i==1)|((i==0)&(j==2)):
            temprow.append([1])
        else:
            temprow.append([0])
    mat_matrix.append(temprow)

node_frame_map = np.zeros((size_x,size_y,1,6))
nodes,frames,node_frame_map,dims = geom.cuboct.from_material(mat_matrix,vox_pitch)

