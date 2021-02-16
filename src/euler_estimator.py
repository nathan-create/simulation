import matplotlib.pyplot as plt
plt.style.use('bmh')

class EulerEstimator:
    def __init__(self, derivatives):
        self.functions = derivatives
    
    def calc_derivative_at_point(self, point):
        result_dict = {}
        for key in self.functions:
            result_dict[key] = self.functions[key](point[0],point[1])
        return result_dict

    def step_forward(self, point, step_size):
        t = point[0]
        old_x = point[1]
        deriv = self.calc_derivative_at_point(point)
        new_x = {}
        for key in old_x:
            new_x[key] = old_x[key] + (deriv[key] * step_size)
        new_point = (t + step_size, new_x)
        return new_point

    def calc_estimated_points(self, point, step_size, max_val):
        point_list = [point]
        count = 0
        while count < max_val:
            next_point = self.step_forward(point, step_size)
            point_list.append(next_point)
            point = next_point
            count += step_size
        return point_list

    def plot(self, point, step_size, end_value):
        x_vals=[]
        y_vals={}
        plt.style.use('bmh')
        for key in point[1]:
            y_vals[key]=[]
        while True:
            if point[0]>end_value:
                break
            for key in point[1]:
                y_vals[key].append(point[1][key])
            x_vals.append(point[0])
            point=self.step_forward(point,step_size)
        
        for key in y_vals:
            plt.plot(x_vals,y_vals[key])
        plt.savefig('euler.png')