"""
name = input("What's your name? ")

if name == "Abraham":   # instaed of listing all the name with many lines of elif, we can just use or and == operator in one line
    print("Nathan")
elif name == "Glory":
    print("Nathan")
elif name == "Lydia":
    print("Nathan")
elif name == "Fayemi":
    print("Nathan")
else:
    print("who?")     
"""

"""
name = input("What's your name? ")

match name:
    case "Abraham":
        print("Nathan")
    case "Glory":
        print("Nathan")
    case "Lydia":
        print("Nathan")
    case "Fayemi":
        print("Nathan")
    case _:
        print("who?")    # default case if none of the above cases match
"""        

name = input("What's your name? ")
match name:
    case "Abraham" | "Glory" | "Lydia" | "Fayemi":
        print("Nathan")
    case "David" | "Rachel" | "Emily":
        print("Leah")    
    case _:
        print("who?")