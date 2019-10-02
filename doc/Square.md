### Uniform distribution inside square

#### Mathematical form

1. Generate 2 random numbers (x, y) uniform between 0 and square length

#### Python code

````
    import random
    import numpy as np

    x = random.uniform(0, length)
    y = random.uniform(0, length)

    print(x, y)
````

or for a centered square :

````
    import random
    import numpy as np

    demiLength = length/2

    x = random.uniform(-demiLength, demiLength)
    y = random.uniform(-demiLength, demiLength)

    print(x, y)
````

#### Result

![Square_in](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/square_in.png)

### Uniform distribution on the edges of the square

#### Mathematical form

1. Generate 1 random number between 1 and 4 (for each edge of the square)
2. Fix axis
3. Generate 1 random number (x or y) uniform between 0 and square length

#### Python code

````
    import random
    import numpy as np

        demiLength = length / 2

        fixAxis = random.randint(1, 4)

        if fixAxis == 1:
            x = random.uniform(-demiLength, demiLength)
            y = demiLength
        elif fixAxis == 2:
            x = random.uniform(-demiLength, demiLength)
            y = -demiLength
        elif fixAxis == 3:
            x = demiLength
            y = random.uniform(-demiLength, demiLength)
        elif fixAxis == 4:
            x = -demiLength
            y = random.uniform(-demiLength, demiLength)

    print(x, y)
````

#### Result

![Square_out](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/square_out.png)
