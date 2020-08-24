# from Linear import Vector, dot
from typing import Callable
import matplotlib.pyplot as plt

#Estimating the Gradient

def difference_quotient(f: Callable[[float], float],
                        x: float,
                        h: float) -> float:
                        return (f(x+h) - f(x) / h)

def square(x: float) -> float:
    return x * x

def derivative(x: float) -> float:
    return 2 * x

xs = range(-10, 11)
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]

def actual_vs_estimates():
    plt.title("Actual Derivatives vs. Estimates")
    plt.plot(xs, actuals, 'rx', label = 'Actual')
    plt.plot(xs, estimates, 'b+', label = 'Estimate')
    plt.legend(loc = 9)
    plt.show()

actual_vs_estimates()