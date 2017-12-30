import numpy as np
import matplotlib.pyplot as pyplot
import funcs


(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual3-dud-0.txt')
V = np.trim_zeros(V)
I = I[0:V.size]
R = R[0:V.size]
ti = ti[0:V.size]

Ts = funcs.rToT(R)

pyplot.plot(Ts, V/I, marker='x', label='0.05')

(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual11-dud-0.2-decrease.txt')
start = 11
V = np.trim_zeros(V)

I = I[start:V.size]
R = R[start:V.size]
ti = ti[start:V.size]
V = V[start:]

Ts = funcs.rToT(R)

pyplot.plot(Ts, V/I, marker='x', label='0.2')

(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual13-dud-0.5-decrease.txt')
V = np.trim_zeros(V)
I = I[0:V.size]
R = R[0:V.size]
ti = ti[0:V.size]

Ts = funcs.rToT(R)


pyplot.plot(Ts, V/I, marker='x', label='0.5')

pyplot.legend()
pyplot.show()
