def greet(name):
    print("Hello", name)
def execute_callback(callback):
    callback("Alice")
execute_callback(greet)
def process(value, callback):
    print(callback(value))
process(5,lambda x:x*x)
