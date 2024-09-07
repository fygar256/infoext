#!/usr/bin/python3
import time
def main():
    self=1
    print("self is living but about to die.\n")
    print(f"state of information self={self}")
    print("for a while self living.")
    time.sleep(3)
    print("")
    self=None
    print(f"self has died. state of information self={self}")
    print("for a while self is dead.")
    print("self will revive.\n")
    time.sleep(3)
    self=1
    print(f"self revived. state of information self={self}")
    print("end")

if __name__=="__main__":
    main()
    exit(0)

