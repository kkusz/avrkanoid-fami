#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
xp = [
  -60
 ,-20
 ,0
 ,15
 ,40
 ,90
 ,150
 ,180
 ,193
 ,200
 ,210
 ,213
 ,214
 ,215
]

yp = [
  0
 ,155
 ,183
 ,188
 ,193
 ,204
 ,221
 ,255
 ,302
 ,348
 ,451
 ,489
 ,497
 ,511
]

xline = [-20, 215]
yline = [156,511]

xvals = np.linspace(-20,215,1024)
yinterp = np.interp(xvals,xp,yp)
ylineint = np.interp(xvals,xline,yline)

xvals2 = np.linspace(0,511,1024);
yinterp2 = np.interp(xvals2,yinterp,ylineint)
a = np.array([xvals2,yinterp2])

np.savetxt("data.csv",a,delimiter = ";")

# plt.plot(xp,yp,'o-', label="measured output value")
# plt.plot(xvals,yinterp,'-x')
# plt.plot(xvals,ylineint,'-', label="ideal output value")
# plt.legend(loc="upper left")
# plt.xlabel("Knob position (relative) [degrees]")
# plt.ylabel("Value read by ADC [0-512]")
# plt.title("Potentiometer reading based on knob position")

plt.plot(xvals2,yinterp2,'-x')
plt.title("Linearity compensation based on ADC reading")
plt.xlabel("Input value read from ADC [0-512]")
plt.ylabel("Output value sent to console [0-512]")
plt.show()
