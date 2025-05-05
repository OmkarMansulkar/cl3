from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n < 0:
        return "Factorial not defined by negative number"
    elif n==0 or n==1:
        return 1
    else:
        result=1
        for i in range(2,n+1):
            result*=i
        return result
    
server = SimpleXMLRPCServer(("localhost",8000))
print("The server is running on port 8000........")

server.register_function(factorial,"factorial")

server.serve_forever()
            
            
import xmlrpc.client

proxy=xmlrpc.client.ServerProxy("http://localhost:8000/")

number=int(input("Enter a number to find its factorial:"))

result=proxy.factorial(number)

print(f"The factorial of {number} is : {result}")
