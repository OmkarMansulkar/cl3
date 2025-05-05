from xmlrpc.server import SimpleXMLRPCServer

def is_palindrome(s):
    return s == s[::-1]

server = SimpleXMLRPCServer(("localhost", 9000))
print("Server running on port 9000...")
server.register_function(is_palindrome, "is_palindrome")
server.serve_forever()



import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
s = input("Enter a string: ")
result = proxy.is_palindrome(s)
print("Palindrome" if result else "Not a palindrome")
