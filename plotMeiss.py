import numpy as np
import matplotlib.pyplot as pyplot
import funcs


(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual5-meis-0.1.txt')
V = np.trim_zeros(V)
I = I[0:V.size]
R = R[0:V.size]
ti = ti[0:V.size]

Ts = funcs.rToT(R)

pyplot.plot(Ts, V/I, marker='x', label='0.1')


(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual18-meis-0.2.txt')
V = np.trim_zeros(V)
I = I[0:V.size]
R = R[0:V.size]
ti = ti[0:V.size]

Ts = funcs.rToT(R)

pyplot.plot(Ts, V/I, marker='x', label='0.2')


(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual14-meis-0.5-upanddown.txt')
V = np.trim_zeros(V)
V = V[2000:]
I = I[0:V.size]
R = R[0:V.size]
ti = ti[0:V.size]

Ts = funcs.rToT(R)

pyplot.plot(Ts, V/I, marker='x', label='0.5')


(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual19-meis-1.txt')
V = np.trim_zeros(V)
I = I[0:V.size]
R = R[0:V.size]
ti = ti[0:V.size]

Ts = funcs.rToT(R)

pyplot.plot(Ts, V/I, marker='x', label='1')

pyplot.legend()
pyplot.show()
