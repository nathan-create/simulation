import matplotlib.pyplot as plt
plt.style.use('bmh')

susceptible = 1000
infected = 1
recovered = 0
s_vals = []
i_vals = []
r_vals = []
t = []
for num in range(500):
    t.append(num)

def copy(num):
    copy = 0
    copy += num
    return copy

for num in range(len(t)):
    s_vals.append(susceptible)
    i_vals.append(infected)
    r_vals.append(recovered)

    s = copy(susceptible)
    i = copy(infected)
    r = copy(recovered)

    susceptible += -0.0003 * i * s
    infected += (0.0003 * s * i) - (0.02 * i)
    recovered += 0.02 * i

plt.plot(t, s_vals, label='S')
plt.plot(t, i_vals, label='I')
plt.plot(t, r_vals, label='R')
plt.savefig('sir_model.png')