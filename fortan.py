from scipy.io import FortranFile
import numpy as np
f = FortranFile('test.unf', 'w')
f.write_record(np.array([1,2,3,4,5], dtype=np.int32))
f.write_record(np.linspace(0,1,20).reshape((5,4)).T)
f.close()
f = FortranFile('test.unf', 'r')
print(f.read_ints(np.int32))
[1 2 3 4 5]
print(f.read_reals(float).reshape((5,4), order="F"))
[[0.         0.05263158 0.10526316 0.15789474]
 [0.21052632 0.26315789 0.31578947 0.36842105]
 [0.42105263 0.47368421 0.52631579 0.57894737]
 [0.63157895 0.68421053 0.73684211 0.78947368]
 [0.84210526 0.89473684 0.94736842 1.        ]]
f.close()
