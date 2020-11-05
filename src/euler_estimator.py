class EulerEstimator:
    def __init__(self, derivative):
        self.function = derivative
    
    def calc_derivative_at_point(self, point):
        return self.function(point[0])
    def step_forward(self, point, step_size):
        return (point[0] + step_size, point[1] + (self.calc_derivative_at_point(point) * step_size))
    def calc_estimated_points(self, point, step_size, num_steps):
        steps = [point]
        for current_step in range(num_steps):
            steps.append(self.step_forward(point, step_size))
            point = self.step_forward(point, step_size)
            current_step += 1
        return steps

euler = EulerEstimator(derivative = (lambda t: t + 1))
print(euler.calc_derivative_at_point((1,4)))
print(euler.step_forward(point = (1,4), step_size = 0.5))
print(euler.calc_estimated_points(point=(1,4), step_size=0.5, num_steps=4))