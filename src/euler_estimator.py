import matplotlib.pyplot as plt
plt.style.use('bmh')

class EulerEstimator:
    def __init__(self, derivatives):
        self.functions = derivatives
    
    def calc_derivative_at_point(self, initial_point):
        result_dict = {}
        for key in self.functions:
            result_dict[key] = self.functions[key](initial_point[0],initial_point[1])
            
        return result_dict

    def step_forward(self, point, step_size):
        new_dict = {}
        old_point = point[0]
        derivs = self.calc_derivative_at_point(point)
        for key in point[1]:
            new_dict[key] =  round(point[1][key]+step_size*derivs[key],2)
        return (old_point + step_size, new_dict)

    def calc_estimated_points(self, point, step_size, num_steps):
        points_list = [point]
        for num in range(num_steps):
            new_point = self.step_forward(point,step_size)
            points_list.append(new_point)
            point = new_point
        return points_list

    def plot(self, point, step_size, num_steps):
        points = self.calc_estimated_points(point,step_size,num_steps)
        x_vals=[]
        y_vals=[]
        for point in points:
            x_vals.append(point[0])
            y_vals.append(point[1])
        plt.style.use('bmh')
        plt.plot(x_vals,y_vals)
        plt.savefig('euler.png')