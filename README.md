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
2. **Reset.py**:
   This is the script that will delete previously recorded data.
   You can either select which uMAMA's data to delete or you can delete all uMAMA data.
   This script should be run only before the first uMAMA measurment to delete all data.
3. **EditData.py**:
   This is the script that allows you to edit previous uMAMA data. It allows you to delete
   measurments for the uMAMAs. The script will prompt you for which uMAMA's data you want to
   edit. It will then display a list of all uMAMA measurments with their dates
   in the format (MM-DD-YYYY_HH-MM-SS)
4. **GenerateFigure.py**:
   This script allows you to generate a colour plot using the uMAMA data. It will prompt you
   for which uMAMA's data you would like to visualize. It will save the figure in their respective uMAMA
   folder.

### Intructions
**First Time Measurement**
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

**Trouble Shooting:**
  If the `Reset.py` script returns any errors, you can manually delete all data by entering
  each uMAMA folder and deleting its content (DO NOT DELETE THE uMAMA FOLDERS)

**Taking a Measurement**
1. Open Windows PowerShell
2. Enter the uMAMA directory via
   `cd uMAMA`
3. Run the reset script via
   `Python Main.py`
4. Answer the prompt with which uMAMA you are taking a measurement of (integer between 1 and 12)
5. After a few seconds a window with an image should pop up. The window icon will look like this in your task bar:
  ![image](https://github.com/raghavbh5588/uMAMA/assets/115365995/4debfe6c-f6aa-4d85-b8e8-a21fc63f83db)
6. On the image window, select which spots to sample colour from using the left mouse click. You can undo your last selection with a right mouse click anywhere in the image window
7. When finished selecting 16 spots, click the "esc" key while the image window is slected
8. The script will extract the colours and save them into the RBG_Data.csv file in the
   respective uMAMA folder. It will also save the photo taken with its date in its folder with the
   format (uMAMA_#_MM-DD-YYYY_HH-MM-SS)

**Trouble Shooting:** If you see the error message `ERROR!! Oopsies!! I think you forgot to connect the arduino!` wait a minute for the computer to recognize the arduino. If after a minute it is still giving that error, you may need to change the COM Port. View the intructions for that in the "Changing COM Port" section. <br />
If you see the error message `ERROR!!!!! Hmmm, make sure the camera is connected!!` wait a minute for the computer to recognize the camera. If it gives the same message after a minute, the would mean the camera is malfunctioning and there likley is no solution. A last ditch effort could be to change the selected camera. View the "Changing Camera Selection" section.
If you run into more errors that do not have a clear error message, then run the `TakePhoto.py` script do that we can analyze the data upon return to Mcgill. Hopefully this won't happen!! Sorry if it does!!


**Editing Previous Data**
1. Open Windows PowerShell
2. Enter the uMAMA directory via
   `cd uMAMA`
3. Run the reset script via
   `Python EditData.py`
4. Answer the prompt with which uMAMA's data you want to edit (integer between 1 and 12)
5. The script will list all collected data and their time point in the format (MM-DD-YYYY_HH-MM-SS)
6. To the right of each measurement, an index is present
7. Answer the prompt with the index of the data point that you want to delete

**Trouble Shooting:** There should not be any errors that come up here but if one does, you can manually go into the uMAMA folder and delete the image and row from the CSV file

**Generating a Plot**
1. Open Windows PowerShell
2. Enter the uMAMA directory via
   `cd uMAMA`
3. Run the reset script via
   `Python GeneratePlot.py`
4. Answer the prompt with which uMAMA's data you want visualize (integer between 1 and 12)
5. A plot will pop up with the colour progression of each well's colour
6. The figure will be saved in the folder of each uMAMA

**Trouble Shooting:** There should not be any errors that come up here but if one does, follow the error messages. Date should be saved in the csv files at this point so plots can be generated back at Mcgill

**Taking a Measurement**
1. Open Windows PowerShell
2. Enter the uMAMA directory via
   `cd uMAMA`
3. Run the reset script via
   `Python TakePhoto.py`
4. Answer the prompt with which uMAMA you are taking a measurement of (integer between 1 and 12)
5. After a few seconds a window with an image should pop up. The window icon will look like this in your task bar:
  ![image](https://github.com/raghavbh5588/uMAMA/assets/115365995/4debfe6c-f6aa-4d85-b8e8-a21fc63f83db)
6. On the image window, click the "y" key if the image is good or click the "n" key to abort the program.
7. The image should save with its date in its folder with the format (uMAMA_#_MM-DD-YYYY_HH-MM-SS)

**Trouble Shooting:** If you see the error message `ERROR!! Oopsies!! I think you forgot to connect the arduino!` wait a minute for the computer to recognize the arduino. If after a minute it is still giving that error, you may need to change the COM Port. View the intructions for that in the "Changing COM Port" section. <br />
If you see the error message `ERROR!!!!! Hmmm, make sure the camera is connected!!` wait a minute for the computer to recognize the camera. If it gives the same message after a minute, the would mean the camera is malfunctioning and there likley is no solution. A last ditch effort could be to change the selected camera. View the "Changing Camera Selection" section.
