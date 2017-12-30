import numpy
import matplotlib.pyplot as pyplot

(T, V, I, R, ti, ti_temp) = numpy.loadtxt('trampresidual26-ceri-0.2.txt')

pyplot.figure(3)
pyplot.plot(R, numpy.gradient(V))


def moving_average(a, n=5):
    ret = numpy.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


av_r = moving_average(R)
av_v = moving_average(V)

pyplot.figure(4)
pyplot.plot(av_r, av_v, marker='x')
pyplot.figure(5)
pyplot.plot(av_r, numpy.gradient(av_v))

pyplot.figure(6)
pyplot.plot(R, numpy.gradient(V/I))

pyplot.figure(7)

def res_to_t(R):
    R0 = 100
    return (-R0 * 3.9083E-3 + (R0 * R0 * + 3.9083E-3 * 3.9083E-3 - 4 * R0 * -5.775E-7 * (R0 - R))**0.5) / (2 * R0 * -5.775E-7)
rs = res_to_t(R)
print(rs)
pyplot.plot(rs, V/I)

pyplot.show()
