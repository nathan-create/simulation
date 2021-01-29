import matplotlib.pyplot as plt
plt.style.use('bmh')

deer = 100
wolves = 10
d_vals = []
w_vals = []
t = []
count = 0
while count <= 100:
    t.append(count)
    count += 0.001

for num in range(len(t)):
    d_vals.append(deer)
    w_vals.append(wolves)
    d = deer
    w = wolves
    deer += (0.0006 * d) - (0.00005 * d * w)
    wolves += (0.00002 * d * w) - (0.0009 * w)

plt.plot(t, d_vals, label='deer')
plt.plot(t, w_vals, label='wolves')
plt.savefig('predator_prey_model.png')