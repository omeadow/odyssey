# Import the class from client module (a python file) within the http package (the folder, has __init__.py to identify it as a package)
# Initial commands from https://realpython.com/ref/stdlib/http/

from http.client import HTTPConnection

# Instatiate a connection. 
# 'host' parameter is mandatory, could accept arguments of any type in theory!
#  
conn = HTTPConnection("www.example.com")

class MyHTTPConnection:

    def __init__(self, host):
        





conn.request("GET", "/")

response = conn.getresponse()
print(response.status)

print(response.read())

