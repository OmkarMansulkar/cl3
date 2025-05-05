from xmlrpc.server import SimpleXMLRPCServer

def compute(num1, num2, op):
    if op == "add":
        return num1 + num2
    elif op == "sub":
        return num1 - num2
    elif op == "mul":
        return num1 * num2
    elif op == "div":
        return num1 / num2 if num2 != 0 else "Division by zero error"
    else:
        return "Invalid operation"

server = SimpleXMLRPCServer(("localhost", 8000))
print("Server running on port 8000...")
server.register_function(compute, "compute")
server.serve_forever()



import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operation (add, sub, mul, div): ").strip().lower()

result = proxy.compute(n1, n2, op)
print(f"Result: {result}")

