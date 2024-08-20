import OpenSeries as opseries
import math

print(opseries.bulat(2.3))
print(
    all(
        opseries.bulat(n, cek=True) == math.floor(n)
        for n in (1, -1, 0, -0, 1.1, -1.1, 1.0, -1.0, 1_000_000_000)
    )
)
