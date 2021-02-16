import sys
sys.path.append('src')
from euler_estimator import *
import matplotlib.pyplot as plt
import math

# alphas, betas
def alpha_n(t,x):
    V = x['V']
    return (0.01*(10-V)) / (math.exp(0.1*(10-V)) - 1)
def alpha_m(t,x):
    V = x['V']
    return (0.1*(25-V))/(math.exp(0.1*(25-V)) - 1)
def alpha_h(t,x):
    V = x['V']
    return 0.07*math.exp(-V/20)

def beta_n(t,x):
    V = x['V']
    return 0.125*math.exp(-V/80)
def beta_m(t,x):
    V = x['V']
    return 4*math.exp(-V/18)
def beta_h(t,x):
    V = x['V']
    return 1/(math.exp(0.1*(30-V)) + 1)

# constants
V_0 = 0
n_0 = alpha_n(0,{'V':0}) / (alpha_n(0,{'V':0}) + beta_n(0,{'V':0}))
m_0 = alpha_m(0,{'V':0})/(alpha_m(0,{'V':0}) + beta_m(0,{'V':0}))
h_0 = alpha_h(0,{'V':0})/(alpha_h(0,{'V':0}) + beta_h(0,{'V':0}))

C = 1.0
V_Na = 115
V_K = -12
V_L = 10.6

# main variables
def dV_dt(t,x):
    s = stim(t)
    Na_curr = I_Na(t,x)
    K_curr = I_K(t,x)
    L_curr = I_L(t,x)
    return (1/C) * (s - Na_curr - K_curr - L_curr)

def dn_dt(t,x):
    n = x['n']
    return (alpha_n(t,x) * (1-n)) - (beta_n(t,x) * n)

def dm_dt(t,x):
    m = x['m']
    return (alpha_m(t,x) * (1-m)) - (beta_m(t,x) * m)

def dh_dt(t,x):
    h = x['h']
    return (alpha_h(t,x) * (1-h)) - (beta_h(t,x) * h)

# currents and stimulus
def I_Na(t,x):
    V = x['V']
    m = x['m']
    h = x['h']
    return 120*(m**3)*h*(V - V_Na) # g_bar_Na = 120
def I_K(t,x):
    V = x['V']
    n = x['n']
    return 36*(n**4)*(V - V_K) # g_bar_K = 36
def I_L(t,x):
    V = x['V']
    return 0.3*(V - V_L) # g_bar_L = 0.3

def stim(t):
    if 10<=t<=11 or 20<=t<=21 or 30<=t<=40 or 50<=t<=51 or 53<=t<=54 or 56<=t<=57 or 59<=t<=60 or 62<=t<=63 or 65<=t<=66:
        return 150
    return 0

# implementation
derivatives = {
    'V': dV_dt,
    'n': dn_dt,
    'm': dm_dt,
    'h': dh_dt}
model = EulerEstimator(derivatives)

initial_vals = {'V': V_0, 'n': n_0, 'm': m_0, 'h': h_0}
init_point = (0, initial_vals)

point_list = model.calc_estimated_points(init_point, 0.01, 80)
t_list = [point[0] for point in point_list]
stim_list = [stim(t) for t in t_list]

plt.style.use('bmh')
plt.plot(t_list, [point[1]['V'] for point in point_list], label="Voltage")
plt.plot(t_list, stim_list, label="Stimulus", lw=0.4)
plt.savefig("hodgkin_huxley_model.png")