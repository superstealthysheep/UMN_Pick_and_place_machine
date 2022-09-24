# Import the csv module
import csv

# Velocity of the arm measured in mm/s
velocity = 100

raised_z = 100  # TODO: Configure this!
lowered_z = 10  # TODO: Configure this!

# Access our .csv and .txt files
csv_file = open('centroid.csv')
instructions = open("instructions.txt", "w")

# Configure how to read our .csv file
csvReader = csv.reader(csv_file, delimiter=',')
csv_labels = {"x": 1, "y": 2, "rotation": 4}

for row in csvReader:
    # Move to specifed (x, y) position of the component
    instructions.write("{" + f'"cmd":"lmove", "x":{csv_labels["x"]}, "y":{csv_labels["y"]}, "z":{raised_z},  "rel":0, "vel":{velocity}' + "}\n")
    # Lower down to the pcb
    instructions.write("{" + f'"cmd":"lmove", "z":{lowered_z}, "rel":0, "vel":{velocity}' + "}\n")
    # HERE WE WANT TO DISABLE THE SUCTION
    # Raise back up
    instructions.write("{" + f'"cmd":"lmove", "z":{lowered_z}, "rel":0, "vel":{velocity}' + "}\n")
