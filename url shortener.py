import pyshorteners 

def Shortener():
    URL = str(input("Enter URL below:\n"))
    Short = pyshorteners.Shortener()/tinyurl.short(URL)
    print(Short)

def Execute(function):
    try:
        function()

    except Exception as Error:
        print(Error)

while True:
    cmd = str(input("~ "))
    if cmd == "quit":
        break
    if cmd == "short_url":
        Execute(Shortener)    