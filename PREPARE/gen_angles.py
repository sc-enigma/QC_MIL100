import os
import numpy as np
import shutil
from scipy.spatial.transform import Rotation as R

r1 = np.array([3.7561,  0.3700, 0.0000])
r2 = np.array([3.7561, -0.3700, 0.0000])
center = np.array([1.9561, 0.0, 0.0])
delta = 15 # degree

idx = 0

for thetta in range(0, 90, delta):
    # THETTA ROTATION
    axis_thetta = np.array([0, 1, 0])
    rot_thetta = R.from_rotvec(axis_thetta * np.radians(thetta)).as_matrix()
    delta_phi = int(delta / np.cos(np.radians(thetta)))  
    for phi in range(0, 90, delta_phi):
        # PHI ROTATION
        axis_phi = np.array([0, 0, 1])
        rot_phi = R.from_rotvec(axis_phi * np.radians(phi)).as_matrix()
        
        r1_rot = rot_phi @ (rot_thetta @ (r1 - center).T) + center
        r2_rot = rot_phi @ (rot_thetta @ (r2 - center).T) + center
        
        src = f"C:\\Projects\\QC_MIL100\\PROD_VAR_A\\MIL100_H2_1.8\\inp\\MIL100_H2_0.inp"
        dst = f"C:\\Projects\\QC_MIL100\\PROD_VAR_A\\MIL100_H2_1.8\\inp\\MIL100_H2_{idx}.inp"
        if not os.path.exists(dst):
            shutil.copy(src, dst)
        lines = []
        with open(dst, 'r') as file:
            lines = file.readlines()
            
        coords = [[float(v.split()[1]), float(v.split()[2]), float(v.split()[3])] for v in lines[5:129]]
        r1_dist = min([np.linalg.norm(r1_rot - c) for c in coords])
        r2_dist = min([np.linalg.norm(r2_rot - c) for c in coords])
        if r1_dist < 1.5 or r2_dist < 1.5:
            continue
            
        lines[3] = f"H    {r1_rot[0]:.4f}    {r1_rot[1]:.4f}    {r1_rot[2]:.4f}\n".replace(' -', '-')
        lines[4] = f"H    {r2_rot[0]:.4f}    {r2_rot[1]:.4f}    {r2_rot[2]:.4f}\n".replace(' -', '-')
        with open(dst, 'w') as file:
            file.writelines(lines)
        idx += 1
        print(idx, thetta, phi)