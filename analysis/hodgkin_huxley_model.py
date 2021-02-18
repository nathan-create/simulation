import sys
sys.path.append('src')
from euler_estimator import *
import matplotlib.pyplot as plt
import math


def alpha_n(t, x):
    V = x['V']
    return (0.01 * (10 - V)) / (math.exp(0.1 * (10 - V)) - 1)

def alpha_m(t, x):
    V = x['V']
    return (0.1 * (25 - V)) / (math.exp(0.1 * (25 - V)) - 1)

def alpha_h(t, x):
    V = x['V']
    return 0.07 * math.exp(-V / 20)

def beta_n(t, x):
    V = x['V']
    return 0.125*math.exp(-V / 80)

def beta_m(t, x):
    V = x['V']
    return 4 * math.exp(-V / 18)

def beta_h(t, x):
    V = x['V']
    return 1 / (math.exp(0.1 * (30 - V)) + 1)

V_0 = 0
n_0 = alpha_n(0, {'V': 0}) / (alpha_n(0, {'V': 0}) + beta_n(0, {'V': 0}))
m_0 = alpha_m(0, {'V': 0})/(alpha_m(0, {'V': 0}) + beta_m(0, {'V': 0}))
h_0 = alpha_h(0, {'V': 0})/(alpha_h(0, {'V': 0}) + beta_h(0, {'V': 0}))

C = 1.0
V_Na = 115
V_K = -12
V_L = 10.6


def dV_dt(t, x):
    s = stimulus(t)
    Na_curr = I_Na(t, x)
    K_curr = I_K(t, x)
    L_curr = I_L(t, x)
    return (1/C) * (s - Na_curr - K_curr - L_curr)

def dn_dt(t, x):
    n = x['n']
    return (alpha_n(t, x) * (1-n)) - (beta_n(t, x) * n)

def dm_dt(t, x):
    m = x['m']
    return (alpha_m(t, x) * (1-m)) - (beta_m(t, x) * m)

def dh_dt(t, x):
    h = x['h']
    return (alpha_h(t, x) * (1-h)) - (beta_h(t, x) * h)

def I_Na(t, x):
    V = x['V']
    m = x['m']
    h = x['h']
    return 120 * (m ** 3) * h * (V - V_Na)

def I_K(t, x):
    V = x['V']
    n = x['n']
    return 36 * (n ** 4) * (V - V_K)

def I_L(t, x):
    V = x['V']
    return 0.3 * (V - V_L)

def stimulus(t):
    if 10 <= t <= 11 or 20 <= t <= 21 or 30 <= t<= 40 or 50 <= t<= 51 or 53 <=t<= 54 or 56 <= t <= 57 or 59 <= t <= 60 or 62 <= t <= 63 or 65 <= t <= 66:
        return 150

    return 0

derivatives = {
    'V': dV_dt,
    'n': dn_dt,
    'm': dm_dt,
    'h': dh_dt
}
hodgkin_huxley_neuron_model = EulerEstimator(derivatives)

init_values = {'V': V_0, 'n': n_0, 'm': m_0, 'h': h_0}
init_point = (0, init_values)

point_list = hodgkin_huxley_neuron_model.calc_estimated_points(init_point, 0.01, 8000)
t_vals = [point[0] for point in point_list]
stim_vals = [stimulus(t) for t in t_vals]

plt.style.use('bmh')
plt.plot(t_vals, [point[1]['V'] for point in point_list], label="Voltage")
plt.plot(t_vals, stim_vals)
plt.savefig("hodgkin_huxley_neuron_model.png")