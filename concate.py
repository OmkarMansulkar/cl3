from xmlrpc.server import SimpleXMLRPCServer

def concatenate(s1, s2):
    return s1 + s2

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(concatenate, "concatenate")
print("Server is running on port 8000...")
server.serve_forever()

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = proxy.concatenate(str1, str2)
print("Concatenated Result:",result)
