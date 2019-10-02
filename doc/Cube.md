### Uniform distribution inside cube

#### Mathematical form

1. Generate 3 random numbers (x, y, z) uniform between 0 and cube length

#### Python code

````
    import random
    import numpy as np

    x = random.uniform(0, length)
    y = random.uniform(0, length)
    z = random.uniform(0, length)

    print(x, y, z)
````

or for a centered cube :

````
    import random
    import numpy as np

    demiLength = length/2

    x = random.uniform(-demiLength, demiLength)
    y = random.uniform(-demiLength, demiLength)
    z = random.uniform(-demiLength, demiLength)

    print(x, y, z)
````

#### Result

![Cube_in_uniformity](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/cube_in_uniformity.png)

### Uniform distribution on the surface of the cube

#### Mathematical form

1. Generate a random number between 1 and 6 (for each face of the cube)
2. Fix axis
3. Generate 2 random numbers (x, y) or (x, z) or (y, z) uniform between 0 and cube length

#### Python code

````
    import random
    import numpy as np

        demiLength = length / 2

        fixAxis = random.randint(1, 6)

        if fixAxis == 1:
            x = random.uniform(-demiLength, demiLength)
            y = random.uniform(-demiLength, demiLength)
            z = demiLength
        elif fixAxis == 2:
            x = random.uniform(-demiLength, demiLength)
            y = demiLength
            z = random.uniform(-demiLength, demiLength)
        elif fixAxis == 3:
            x = demiLength
            y = random.uniform(-demiLength, demiLength)
            z = random.uniform(-demiLength, demiLength)
        elif fixAxis == 4:
            x = random.uniform(-demiLength, demiLength)
            y = random.uniform(-demiLength, demiLength)
            z = -demiLength
        elif fixAxis == 5:
            x = random.uniform(-demiLength, demiLength)
            y = -demiLength
            z = random.uniform(-demiLength, demiLength)
        elif fixAxis == 6:
            x = -demiLength
            y = random.uniform(-demiLength, demiLength)
            z = random.uniform(-demiLength, demiLength)

    print(x, y, z)
````

#### Result

![Cube_out_uniformity](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/cube_surface_uniformity.png)
