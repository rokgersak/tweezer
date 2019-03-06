import ForceCalc as forcecalc
import SynthActiveTrajectory as sat

#   A minimal workflow example; trap stiffnesses in tuple "kValues" need to be provided.

kValues = (2.5e-6,0.5e-6)
values = forcecalc.read_input("test.dat")
sat.SAT2("test.dat",1000,0.005, kValues[0], kValues[1], 2, 1, 1e-6, 1e-6, 0.5e-6, 9.7e-4, 300, 2)

#   In this case, the calculated values are not recorded.

forcecalc.force_calculation(values[:,0], values[:,1], values[:,2], values[:,3], values[:,4], kValues, 300)