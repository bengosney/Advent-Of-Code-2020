import importlib
import os
import os.path
import timeit


def benchmark(mod):
    importlib.reload(mod)


times = {}
for name in os.listdir("."):
    if name.startswith("day_"):
        name = name.replace(".py", "")
        print(f"Benchmarking {name}")
        mod = importlib.import_module(name)
        times[name] = timeit.timeit("benchmark(mod)", globals=locals(), number=1)

print("=" * 80)
for k, v in sorted(times.items()):
    print(k, v)
