# z_0 = 0
# z_{n+1} = z^2_{n} + c

import numpy as np
import matplotlib.pyplot as plt


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):

    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))

    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))

    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        # works even if c is a matrix because of numpy tricks
        z = z**2 + c

    return abs(z) <= 2


def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


def main():
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
    members = get_members(c, num_iterations=20)

    plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
