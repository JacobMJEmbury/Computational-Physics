import numpy as np
import matplotlib.pyplot as plt

# time t, column 1
data = np.zeros((1000, 2), dtype=complex)

# Make some example functions:

data[:, 0] = np.linspace(0.0, 10.0, 1000, endpoint=False) # Time 
print(data[:, 0]) # ????
omega_1 = np.pi * 5
omega_2 = np.pi * 3
data[:, 1] = np.sin((omega_1)*data[:,0]) # Function
data[:, 1] = np.sin((omega_1)*data[:,0]) + np.sin((omega_2)*data[:,0]) 


# DFT function
def DFT(data):
    N = len(data[:, 0])
    T = data[N-1, 0] - data[0, 0]
    delta_t = T/N

    #Define bins: (p)

    f_p = np.zeros((N, 2), dtype=complex)

    # Define p bin index:
    f_p[:, 0] = np.linspace(-N/2 + 1, N/2, N)

    # Define f_p for each bin index:
    for index_p, p in enumerate(f_p[:, 0]):
        for n in range(N):
            f_p[index_p, 1] = f_p[index_p, 1] + (data[n, 1]*np.exp(2j*np.pi*p*n/N))

    return f_p

# Plot graph here...
f_p = DFT(data)

fig, (ax_time, ax_freq) = plt.subplots(2, 1, figsize=(8, 6))

ax_time.plot(data[:, 0], data[:, 1], marker="o")
ax_time.set_xlabel("t")
ax_time.set_ylabel("f(t)")
ax_time.set_title("Signal")

N = len(data[:, 0])
T = data[N-1, 0] - data[0, 0]
delta_t = T/N

ax_freq.stem(2*np.pi*f_p[:, 0]/(N*delta_t), np.abs(f_p[:, 1]))
ax_freq.set_xlabel("p")
ax_freq.set_ylabel("|f_p|")
ax_freq.set_title("DFT")

fig.tight_layout()
plt.show()