import functools
import time
# function returns a value based on the given arguments

def my_function(argument):
    return argument

my_function("arg")


# functions can be passed around and used as arguments
# its possible to define function inside other functions - inner functions

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

def do_twice(func):
    def wrapper(*args,**kwargs):
        print("before")
        func(*args,**kwargs)
        func(*args,**kwargs)
        print("after")
    return wrapper

@do_twice
def say_whee(name):
    print(f"Whee! {name}")

say_whee("Sam")


# introspection
print(say_whee) # <function do_twice.<locals>.wrapper at 0x10d29b790>
print(say_whee.__name__) # wrapper
#print(help(say_whee)) # Help on function wrapper in modeule: __main__: wrapper(*args, **kwargs)

def do_flip(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("before")
        func(*args,**kwargs)
        func(*args,**kwargs)
        print("after")
    return wrapper

@do_flip
def say_my_name(name):
    print(f"Hello {name}")

print(say_my_name) # <function say_my_name at 0x10d29b790>
print(say_my_name.__name__) # say_my_name
#print(help(say_my_name)) # Help on function say_my_name in modeule: __main__: say_my_name(name)

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

#print(make_greeting("Freja"))
#print()
#print(make_greeting("Luna", 1))



def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

#print(countdown(10))


# Making sure if user is logged in
from flask import Flask, g, request, redirect, url_for
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    pass


# Fancy decorators


# Decorating classes
# Some commonly used decorators that are even built-ins in Python are @classmethod, @staticmethod, and @property. The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected to a particular instance of that class.

def repeat(number):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for run in range(number):
                func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @debug
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])

tw = TimeWaster(10)
print(tw)

@do_twice
@debug
def do_loop(number):
    for i in range(number):
        print(i)

do_loop(2)

cycle_number = 3
@repeat(number = cycle_number)
def do_round(number):
    for round in range(number):
        print(f"round: {round}")

do_round(2)

def repeat_with_spice(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

@repeat_with_spice
def do_loop(number):
    for i in range(number):
        print(i)

do_loop(2)

@repeat_with_spice(num_times = 2)
def do_loop(number):
    for i in range(number):
        print(i)
do_loop(2)


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
@count_calls
@repeat_with_spice(num_times = 2)
def do_loop(number):
    for i in range(number):
        print(i)

do_loop(2)
print(do_loop.num_calls)
do_loop(2)
print(do_loop.num_calls)