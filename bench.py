from simple_benchmark import benchmark
import numpy as np
funcs = [sum, np.sum]
arguments = {i: [1]*i for i in [1, 10, 100, 1000, 10000, 100000]}
argument_name = 'list size'
aliases = {sum: 'Python sum', np.sum: 'NumPy sum'}
b = benchmark(funcs, arguments, argument_name, function_aliases=aliases)
print(b)