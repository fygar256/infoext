Information Externalities. Small computer simulation model

The externalities of information.

When we are born, we are born knowing nothing, and as we grow, we gain and lose information.

This program simulates the moment when a newly born human being gains information for the first time.

This is the information version of existentialism.

It is written in python, but all it is doing is selecting one of the two by a random number and assigning it to the variable “self”.

It is written in python. /io.py to run it.

It uses my truerand module.

io.py
```
#! /usr/bin/python3
import truerand
def main():.
    self=None
    print(f “information source is /dev/random”)
    print(“self will get information”)
    print(f “state of no information self={self}”)
    print(“self don't know anything.”)
    i=truerand.rand(1)%2
    print(f “information source is {i}”)
    self=i
    print(f “self has been given information”)
    print(f “now, self got informatiom self={self}”)

if __name__==“__main__”: main()
    main()
    exit(0)

```

Execution result

```
$ io.py
information source is /dev/random
self will get information
state of no information self=None
self don't know anything.
information source is 1
self has been given information
now, self got informatiom self=1
$
```

From this we can say that the assumption that when there is no information at all, the person coming from the other side has a 50%50% probability of being a programmer is incorrect. This is because in this program, the probability of i's decision is external to self.
This is objective objectivity. This is the objectivity of information.

You can treat genuine random numbers and perfect random numbers as the same thing, but since genuine random numbers are not perfect random numbers, the probability of the decision of i would not be exactly 1/2,1/2. Since the genuine random number is a random number from environmental noise, pooled by /dev/random/, its value is affected by the environment in which the hardware is located, to be precise. Since they are good quality random numbers, they can be treated as perfect random numbers.

I heard there was a theory like this in information philosophy.

Existentialism, simply put, is another.

I don't think existentialism is very good, but I thought I would put this on the site to see if it is also true.

Existentialism is different from existential thought. I am an essentialist and I think the essence of everything is important. Sartre is wrong.

Death, the opposite of birth, is good if you assign None to self. For resurrection, you can assign information to self again.

I made this on the theme of death and resurrection.

dr.py

```
#! /usr/bin/python3
import time
def main():
    self=1
    print(“self is living but about to die.\n”)
    print(f “state of information self={self}”)
    print(“for a while self living.”)
    time.sleep(3)
    print(“”)
    self=None
    print(f “self has died. state of information self={self}”)
    print(“for a while self is dead.”)
    print(“self will revive.\n”)
    time.sleep(3)
    self=1
    print(f “self revived. state of information self={self}”)
    print(“end”)

if __name__==“__main__”: if __name__==“__main__”: if
    main()
    exit(0)
```

Execution result

```
$ dr.py
self is living but about to die.

state of information self=1
for a while self living.

self has died. state of information self=None
for a while self is dead.
state of information self=None for a while self is dead. self will revive. self revived.

self revived. state of information self=1
end
```

What the heck.

The Internet also has an information externality, and even if we look at the Internet as a whole, we can see that information exists outside of the Internet, and that the Internet is not everything. The Internet as a whole is an open system, but if you take a single site, you will find that some parts of it are so suffocating that they could be called closed.

In general, there is an externality of information, and the total amount of information in an open system is infinite.

haiku: Snow cat and I know nothing, Kotaro.

In classical probability theory, it is correct to assume that in a single coin toss, the probability of getting a heads up and a tails up is equally 1/2.

Translated with DeepL.com (free version)
