### Uniform distribution inside cylinder

#### Mathematical form

1. Generate 1 random number (r) uniform between 0 and radius length
2. Generate 1 random number (θ) uniform between 0 and 2π
3. Generate 1 random number (z) uniform between 0 and cylinder length
4. x = sqrt(r) * cos(θ)
5. y = sqrt(r) * sin(θ)

#### Python code

````
    import random
    import numpy as np

    r = random.uniform(0, radius)
    theta = random.uniform(0, 2*np.pi)
    x = np.sqrt(r) * np.cos(theta)
    y = np.sqrt(r) * np.sin(theta)
    z = random.uniform(0, length)

    print(x, y, z)
````

#### Result

![Cylinder_in_uniformity](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/cylinder_in_uniformity.png)<br/>
![Cylinder_in](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/cylinder_in.png)

### Uniform distribution on the surface of the cylinder

#### Mathematical form

1. Generate 1 random number (θ) uniform between 0 and 2π
2. Generate 1 random number (z) uniform between 0 and cylinder length
3. x = radius * cos(θ)
4. y = radius * sin(θ)

#### Python code

````
    import random
    import numpy as np

    theta = random.uniform(0, 2*np.pi)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = random.uniform(0, length)

    print(x, y, z)
````

#### Result

![Cylinder_out_uniformity](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/cylinder_out_uniformity.png)<br/>
![Cylinder_out](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/cylinder_out.png)
