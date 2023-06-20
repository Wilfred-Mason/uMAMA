import csv
import pandas

def addRow(uMAMA, data):
    DataFile = open('uMAMA_'+ uMAMA + '/RGB_Data.csv', 'a', newline="")
    DataFile.truncate()
    writer = csv.writer(DataFile)
    writer.writerow(data)

header = ["Date and Time", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48"]

if __name__ == "__main__":
    uMAMA = input("Which uMAMA's data do you want to edit?")
    try:
        df = pandas.read_csv('uMAMA_'+ uMAMA+'/RGB_Data.csv', names= header)
    except:
        print("Hmmmm I don't think you have taken a measurment of uMAMA "+ uMAMA +" yet")
        quit()
    print("Measurements taken at:")
    print("     Date and Time")
    print(df["Date and Time"])
    rowToDrop = int(input("Provide the index of the measurement you would like to delete: "))
    dropped = df.iloc[rowToDrop, 0]
    df = df.drop([rowToDrop])
    df.to_csv('uMAMA_'+ uMAMA+'/RGB_Data.csv', index= None, header= None)
    print("Measurement at: " + dropped + " was deleted")
