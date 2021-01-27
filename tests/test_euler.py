import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

#euler = EulerEstimator(derivatives = (lambda t: t+1))

#print("Testing derivative calculation")
#assert euler.calc_derivative_at_point((1,4)) == 2
#print("Passed")

#print("Testing step forward")
#assert euler.step_forward(point=(1,4), step_size=0.5) == (1.5,5)
#print("Passed")

#print("Testing estimated points")
#assert euler.calc_estimated_points(point=(1,4), #step_size=0.5, num_steps=4) == [(1, 4), (1.5, 5),(2, 6.25), (2.5, 7.75), (3, 9.5)]
#print("Passed")

#euler.plot(point=(-5,10), step_size=0.1, num_steps=100)


derivatives = {'A': (lambda t,x: x['A'] + 1),'B': (lambda t,x: x['A'] + x['B']),'C': (lambda t,x: 2*x['B'])}



initial_values = {'A': 0, 'B': 0, 'C': 0}
initial_point = (0, initial_values)
euler = EulerEstimator(derivatives = derivatives)

assert euler.calc_derivative_at_point(initial_point) == {'A':1,'B':0,'C':0}

point_2 = euler.step_forward(initial_point,0.1)
assert point_2 == (0.1,{'A':0.1,'B':0,'C':0}), point_2


assert euler.calc_derivative_at_point(point_2) == {'A':1.1,'B':0.1,'C':0}, euler.calc_derivative_at_point(point_2)

point_3 = euler.step_forward(point_2,-0.5)
assert point_3 == (-0.4,{'A':-0.45,'B':-0.05,'C':0}), point_3

assert euler.calc_estimated_points(point_3,2,3)==[(-0.4, {'A': -0.45, 'B': -0.05, 'C': 0.0}), (1.6, {'A': 0.65, 'B': -1.05, 'C': -0.2}), (3.6, {'A': 3.95, 'B': -1.85, 'C': -4.4}), (5.6, {'A': 13.85, 'B': 2.35, 'C': -11.8})]

euler.plot((0,{'A':0,'B':0,'C':0}),0.01,5)