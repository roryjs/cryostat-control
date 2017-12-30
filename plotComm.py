import numpy as np
import matplotlib.pyplot as pyplot
import funcs


(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual9-comm-0.2.txt')
V = np.trim_zeros(V)
I = I[0:V.size]
R = R[0:V.size]
ti = ti[0:V.size]

Ts = funcs.rToT(R)

pyplot.plot(Ts, V/I, marker='x')


(T, V, I, R, ti, ti_temp) = np.loadtxt('trampresidual10-comm-0.3.txt')
V = np.trim_zeros(V)
I = I[0:V.size]
R = R[0:V.size]
ti = ti[0:V.size]

Ts = funcs.rTotT(R)


pyplot.plot(Ts, V/I, marker='x')


pyplot.show()
