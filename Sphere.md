**Project is on going, mathematical forms are good but I need to finish the python code part, I'm also looking to improve my grammar and the clarity of the project so I'm doing a lot of tests of syntax and page layout**

**Feel free to contact me  if you need some help about coding or understanding !**

Uniform distribution of random points generation on the surface of a sphere or in the volume of the sphere is a school case.

Numerous ways are available, but my favorite is very simple, can be adapt easily on surface or in volume (less than a line of difference) and quick. 

# First method 

The idea is to pick points uniformely on a cube. And throw points not in the sphere.

## My opinion on this method

I don't like this method because we will lose some points and need to regenerate them. It will be quite slow, moreover a condition is necessary.
I wrote it down because it can be found 

## Mathematical form

1. Generate 3 random numbers (x, y, z) uniform between [-r_s and r_s]
2. If x² + y² + z² <= r²_s keep the point, if not throw it away and generate a new point

## Python code

```
import random

rs = 1

x = random.uniform(-rs, rs)
y = random.uniform(-rs, rs)
z = random.uniform(-rs, rs)

if x*x + y*y + z*z <= rs*rs:
    print(x, y, z)
```

## Conversion to sphere surface distribution

In this exemple we generate points inside the sphere of radius s. We can restrain the condition to keep only points on the surface of the sphere with the test :

x² + y² + z² = r²_s

But we will throw a lot of points, this method is not suitable to generate a large colletion of points.

# Second method

In this method we will use Archimedes's theorem to generate points over the surface of the sphere.

## My opinion

This method is very quick because we will not throw away points but unfortunately we can't generate points inside the sphere. Best point, it needs the generation of only 2 variables.

## Mathematical background

1. Generate a random number z uniform between [-r_s and r_s]
2. Generate a random number θ uniform between [0 and 2π]
3. x = sqrt(r_s² - z²) * cos(θ)
4. y = sqrt(r_s² - z²) * sin(θ)

## Python code

```
import random
import numpy as np

rs = 1

z = random.uniform(-rs, rs)
theta = random.uniform(0, 2*np.pi)

x = np.sqrt(rs*rs - z*z) * np.cos(theta)
y = np.sqrt(rs*rs - z*z) * np.sin(theta)

print(x, y, z)
```

## Conversion to volume distribution

It's maybe possible to generate uniform distribution inside a sphere by varying rs value between 0 and 1. But I doubt of the uniformity of the generator due to the square-root. If you have any information about that let me know.

# Third method

This method generate number in spherical coordinates and changed them into cartesian.

## My opinion

I love this method, it's easy to understand and to remember and also quick because we need to generate only 2 variables, but we have 3 quick operations to do. We can generate uniform distrubtion of coordinates on the sphere and inside with only one line difference.

## Mathematical background

1. Generate 1 random number θ uniform between [0 and 2π]
2. Generate 1 random number φ uniform between [0 and π]
3. x = r * sin(θ) cos(φ)
4. y = r * sin(θ) cos(φ)
5. z = r * cos(θ)

## Python code

```
import random
import numpy as np

rs = 1

theta = random.uniform(0, 2*np.pi)
phi = random.uniform(0, np.pi)

x = rs * np.sin(theta) * np.cos(phi)
y = rs * np.sin(theta) * np.sin(phi)
z = rs * np.cos(theta)

print(x, y, z)
```

## Conversion to volume distribution

We only need to induce variation in the radius of the sphere : 

1. Generate a random number r uniform between [0 and rs]

```
r = random.uniform(0, rs)
```

# Sources

This page is a condensed version of information found in this page
https://math.stackexchange.com/questions/87230/picking-random-points-in-the-volume-of-sphere-with-uniform-probability
