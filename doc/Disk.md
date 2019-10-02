### Uniform distribution inside disk

#### Mathematical form

1. Generate 1 random number (r) uniform between 0 and radius
2. Generate 1 random number (θ) uniform between 0 and 2π
3. x = sqrt(r) * cos(θ)
4. y = sqrt(r) * sin(θ)

#### Python code

````
    r = random.uniform(0, radius)
    theta = random.uniform(0, 2*np.pi)
    x = np.sqrt(r) * np.cos(theta)
    y = np.sqrt(r) * np.sin(theta)
````

#### Result

![Disk_in](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/disk_in.png)

### Uniform distribution on the edge of the disk

#### Mathematical form

1. Generate 1 random number (θ) uniform between 0 and 2π
2. x = radius * cos(θ)
3. y = radius * sin(θ)

#### Python code

````
    theta = random.uniform(0, 2*np.pi)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
````

#### Result

![Disk_out](https://github.com/AymericFerreira/ubiquitous-umbrella/blob/master/doc/images/disk_out.png)
