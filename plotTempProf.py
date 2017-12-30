import numpy as np
import matplotlib.pyplot as pyplot


(T, V, R, ti, ti_temp, temps) = np.loadtxt('tramp80-180-temprofile.txt')

T = np.trim_zeros(T)
V = V[0:T.size]
R = R[0:T.size]
ti = ti[0:T.size]

ramp_index = []
for ti_ramp_pt in ti_temp:
    for i, time in enumerate(ti):
        if time > ti_ramp_pt:
            ramp_index.append(i)
            break

ramp_index = np.array(np.trim_zeros(ramp_index))
av_T = np.zeros([ramp_index.size])
av_V = np.zeros([ramp_index.size])
av_R = np.zeros([ramp_index.size])

for i,v in enumerate(ramp_index):
    av_T[i] = np.abs(np.average(T[v-10:v]))
    av_V[i] = np.abs(np.average(V[v - 10:v]))
    av_R[i] = np.average(R[v-10:v])


fit = np.polyfit(av_R, av_T, 1)
xs = np.linspace(av_R[0], av_R[-1], 100)
pyplot.plot(xs, fit[1] + xs*fit[0])
print(fit)



pyplot.plot(av_R, av_T, marker='x')

pyplot.show()