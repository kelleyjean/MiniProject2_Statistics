from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import division


def pop_correlation_coefficient(data_x, data_y):
    x = pop_stand_dev(data_x)
    y = pop_stand_dev(data_y)
    divisor = multiplication(x, y)

    # Covariance calculation:
    d = population_mean(data_x)
    e = population_mean(data_y)
    a = [(element - d) for element in data_x]
    b = [(element - e) for element in data_y]
    size = len(a)
    product = [a[i] * b[i] for i in range(size)]
    total = sum(product)
    covariance = division(size, total)

    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    return d
