import os
import glob

uMAMA = input("Which uMAMA do you want to reset? (input = interger 1-12 or 'a' for all)")

command = input("This script will delete all previous data and photos.\nOnly run this script if you are taking your first measurement.\nAre you sure you want to reset? (y or n)")
if command == "n":
    quit()
elif command == "y":
    if uMAMA == "a":
        for i in range(1, 12):
            files = glob.glob("uMAMA_"+ str(i) + "/*")
            for file in files:
                os.remove(file)
    else:
        files = glob.glob("uMAMA_"+ uMAMA + "/*")
        for file in files:
            os.remove(file)