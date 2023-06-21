# uMAMA
Repository for the development and research of a microfluidic biosignature detection device in the Whyte Lab at Mcgill

# Standard Operating Procedure: uMAMA
## Hardware Setup
**Equipment list**:
1. uMAMA module
2. USB cables for camera and arduino
3. USB hub for field computer

### Instructions
1. Turn field computer on
2. Plug USB hub into field computer (make sure the USB hub switch is on)
3. Plug camera and arduino USB cables into USB hub
4. Wait 1 minute for the camputer to recognize the devices

## Software Setup
**List of Executable Python Scripts**
1. **Main.py**:
   This is your main script that will be used to take measurments with the uMAMA unit
   Run this everytime you need to take a new measurment. The script will prompt you to select
   the uMAMA that you are taking a measurment of and it will allow you to select sampling
   spots for the colours. This script will also save data into the RBG_Data.csv file in the
   respective uMAMA folder. It will also save the photo taken with its date in its folder with the
   format (uMAMA_#_MM-DD-YYYY_HH-MM-SS)
3. **Reset.py**:
   This is the script that will delete previously recorded data.
   You can either select which uMAMA's data to delete or you can delete all uMAMA data.
   This script should be run only before the first uMAMA measurment to delete all data.
4. **EditData.py**:
   This is the script that allows you to edit previous uMAMA data. It allows you to delete
   measurments for the uMAMAs. The script will prompt you for which uMAMA's data you want to
   edit. It will then display a list of all uMAMA measurments with their dates
   in the format (MM-DD-YYYY_HH-MM-SS)
6. **GenerateFigure.py**:
   This script allows you to generate a colour plot using the uMAMA data. It will prompt you
   for which uMAMA's data you would like to visualize. It will save the figure in their respective uMAMA
   folder.

### Intructions
**First Time Measrument**
**Steps**
1. Open Windows PowerShell
2. Enter the uMAMA directory via
   `cd uMAMA`
3. Run the reset script via
   `Python Reset.py`
4. When prompted for which uMAMA's data to delete, enter "a" for all
5. When prompted to confirm the request, enter "y" for yes
6. All the data is now cleared
7. Next, ensure that all uMAMA folders are present. There should be 12 folders with the format (uMAMA_#). Create new folders and edit folder naming in case of any mistakes.
8. You are now good to take your first measurement!

**Trouble Shooting**
  If the `Reset.py` script returns any errors, you can manually delete all data by entering
  each uMAMA folder and deleting its content (DO NOT DELETE THE uMAMA FOLDERS)
  
  
