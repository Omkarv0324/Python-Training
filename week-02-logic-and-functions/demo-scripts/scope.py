"""Session 2.4 demo — local vs global scope."""

message = "global"       # global variable


def change():
    message = "local"    # this is a NEW local variable
    print("inside:", message)


change()
print("outside:", message)   # still "global"


# Functions can READ globals, but assigning makes a local unless you say otherwise.
counter = 0


def increment():
    global counter       # explicitly use the global (use sparingly!)
    counter = counter + 1


increment()
increment()
print("counter:", counter)   # 2
