import colour
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import *
import colour

# SDS_COLOURCHECKERS
#https://colour.readthedocs.io/en/latest/generated/colour.SDS_COLOURCHECKERS.html

cc_name='cc_ohta'
cc_name='ColorChecker N Ohta'
print(f'color checker: {cc_name}')
for i, (k, v) in enumerate(colour.SDS_COLOURCHECKERS[cc_name].items()):
    print(f'[{i}] {k}')

fig, ax = colour.plotting.plot_multi_sds(
        [colour.SDS_COLOURCHECKERS['ColorChecker N Ohta'][color].copy()
        for color in ['red', 'orange', 'purple', 'green', 'cyan', 'magenta']])
fig.savefig('colorchecker_reflection.png')
#plt.show()

#with colour.utilities.suppress_warnings(
#    colour_runtime_warnings = True,
#    colour_usage_warnings = True,
#    colour_warnings = True,
#    python_warnings = True ):
#    from colour import *
#    from colour.plotting import *
#    from colour.models import *
#    from colour.recovery import *
#    from colour.colorimetry import *
#    from colour.utilities import *

#with colour.utilities.suppress_warnings(colour_runtime_warnings = True, colour_usage_warnings = True, colour_warnings = True, python_warnings = True ):
#    plot_multi_sds(
#        [SDS_COLOURCHECKERS['ColorChecker N Ohta'][color].copy()
#        for color in ['red', 'orange', 'purple', 'green', 'cyan', 'magenta']])
#    plt.show()
