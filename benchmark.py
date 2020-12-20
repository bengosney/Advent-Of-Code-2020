import importlib
import os
import os.path
import timeit


def benchmark(mod):
    importlib.reload(mod)


number = 10
times = {}
for name in os.listdir("."):
    if name.startswith("day_"):
        name = name.replace(".py", "")
        print(f"Benchmarking {name}")
        mod = importlib.import_module(name)
        times[name] = timeit.timeit("benchmark(mod)", globals=locals(), number=number)

print("=" * 80)
for k, v in sorted(times.items()):
    print(k, v / number)
