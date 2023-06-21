#Plot the history of well colors (from Excel)
#Operations
#Open the Excel file
#Create a t x 16 x 3 matrix where t is the number of time-steps, 16 the number of wells and 3 the number of color channels
#Use imshow to display the matrix (BRG) -> CV2 format

import pandas
import cv2
import numpy as np
import matplotlib.pyplot as plt

uMAMA = input("Which uMAMA do you want to generate a plot for?: ")

try:
    df = pandas.read_csv('uMAMA_'+ uMAMA+ '/RGB_Data.csv', header= None)
except:
    print("ERROR!! No data to plot!! Run Main.py to collect data!!")
    quit()

t_steps = len(df.index) #CHANGE BASED ON NUMBER OF TIME STEPS


df = df.drop(0, axis=1)

dataset = []
for i in range(t_steps):
    row = []
    for j in range (0, 47, 3):
        tup = (round(df.iloc[i, j]), round(df.iloc[i, j+1]), round(df.iloc[i, j+2]))
        row.append(tup)
    dataset.append(row)

plt.imshow(dataset)

ax = plt.gca()
ax.set_xticks(np.arange(0, 16, 1))
ax.set_yticks(np.arange(0, t_steps, 1))
ax.set_xticklabels(np.arange(1, 17, 1))
ax.set_yticklabels(np.arange(1, t_steps + 1, 1))
ax.set_xticks(np.arange(-.5, 16, 1), minor=True)
ax.set_yticks(np.arange(-.5, t_steps, 1), minor=True)
ax.set_xlabel("Well Number", size = 15)
ax.set_ylabel("Time Point", size = 15)
ax.grid(which = "minor", color='black', linestyle='-', linewidth=1)

plt.savefig('uMAMA_'+ uMAMA+ '/Well_History.png')
plt.show()



    
