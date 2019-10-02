### Uniform distribution inside triangle

#### Mathematical form

1. Generate 2 random numbers (r and s) uniform between 0 and 1
2. 

#### Python code

````
    import random
    import numpy as np

    r = random.uniform(0, 1)
    s = random.uniform(0, 1)

    if r+s >= 1:
        r = 1-r
        s = 1-s

    x, y = base[0] + r * edge1length, base[1] + s * edge2length

    print(x, y)
````