import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

#1

#массив с координатами треугольника

verts = [
   (1., 0.),
   (2., -5.),
   (2., 4.),
   (0., 0.),
]

#список комманд

codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,
]

#выполнение команд по точкам

path = Path(verts, codes)

fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='magenta', lw=3) #цвет фигуры, толщина рамки
ax.add_patch(patch)
ax.set_xlim(0, 5) #пределы по оси OX
ax.set_ylim(-5, 5) #пределы по оси OY
plt.show()

#2

verts = [
   (0., 0.),
   (0.2, 1.),
   (1., 0.8),
]

codes = [
    Path.MOVETO,
    Path.CURVE3, #комплексная команда которая будет строить кривую, она использует изначальную, специальную и конечную точки
    Path.CURVE3,
]

path = Path(verts, codes)

fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='yellow', lw=1)
ax.add_patch(patch)

xs, ys = zip(*verts)
ax.plot(xs, ys, 'x--', lw=2, color='blue', ms=10)

ax.text(-0.05, -0.05, 'P0')
ax.text(0.15, 1.05, 'P1')
ax.text(1.05, 0.85, 'P2')

ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
plt.show()

#3

import numpy as np
import matplotlib.patches as patches
import matplotlib.path as path

fig, ax = plt.subplots()
# получение случайно заполненного массива
np.random.seed(82345)

data = np.random.randn(1000)
n, bins = np.histogram(data, 100)

# преобразование массива
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n
nrects = len(left)

#построение фигуры

nverts = nrects*(1+3+1)
verts = np.zeros((nverts, 2))
codes = np.ones(nverts, int) * path.Path.LINETO
codes[0::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
verts[0::5, 0] = left
verts[0::5, 1] = bottom
verts[1::5, 0] = left
verts[1::5, 1] = top
verts[2::5, 0] = right
verts[2::5, 1] = top
verts[3::5, 0] = right
verts[3::5, 1] = bottom

#настройки параметров как в #1

barpath = path.Path(verts, codes)
patch = patches.PathPatch(barpath, facecolor='yellow',
                          edgecolor='blue', alpha=0.5)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())

plt.show()
