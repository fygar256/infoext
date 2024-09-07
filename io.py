#!/usr/bin/python3
import truerand
def main():
    self=None
    print(f"information source is /dev/random")
    print("self will get information")
    print(f"state of no information self={self}")
    print("self don't know anything.")
    i=truerand.rand(1)%2
    print(f"information source is {i}")
    self=i
    print(f"self has been given information")
    print(f"now, self got informatiom self={self}")

if __name__=="__main__":
    main()
    exit(0)

