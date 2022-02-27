import AAA
import BBB
import numpy as np


size = 257
s = np.zeros((size, size))
s = AAA.main(s, size)
BBB.imout(s, size)
BBB.objout(s, size)
print("Task finished")
