import numpy as np
import time as t
import json
from datetime import datetime

# --- Instance variables ---

time = 0
date = ""
location = ""
id = ""
capacity = 0
type = ["Waste", "Bottles", "Paper", "Compost"]  # Based on priority


class Schedule :

    # --- Initialize each database entry object ---

    def __init__(self, date_time, location, id, capacity, type):
        self.date_time = date_time
        self.location = location
        self.id = id
        self .capacity = capacity
        self.type = type

    # --- Getter and Setter methods ---

    # Get date and time of bin
    def getDateTime(self):
        return self._date_time

    # Set date and time of bin
    def setDateTime(self, dt):
        self._date_time = dt

    # Get location of bin
    def getLocation(self):
        return self._location

    # Set location of bin
    def setLocation(self, l):
        self._location = l

    # Get ID of bin
    def getID(self):
        return self._id

    # Set ID of bin
    def setID(self, i):
        self._id = i

    # Get capacity of bin
    def getCapacity(self):
        return self._capacity

    # Set capacity of bin
    def setCapacity(self, c):
        self._capacity = c

    # Get type of garbage in bin
    def getType(self):
        return self._type

    # Set type of garbage in bin
    def setType(self, t):
        self._type = t


    # --- Sorting based on attribute ---

    # Sort by date and time


    # Sort by location


    # Sort by ID
    def sortID(ent):
        for i in range(len(ent)):
            min_index = i
            for j in range(i + 1, len(ent)):
                if ent[min_index] > ent[j]:
                    min_index = j
        ent[i], ent[min_index] = ent[min_index], ent[i]

    # Sort by capacity


    # Sort by type


    # --- Other features ---

    # Get details of a database entry
    def getDetails(self):
        print(self._date_time, self._location, self._id, self._capacity, self._type)


# Create a dynamic list of database entries
ent = []
#n = len(ent)  # Length of list

# Append new entries when received

ent.append(Schedule(datetime, "Rye U", "12345", 10, "Waste"))
ent.append(Schedule(datetime, "Rye U", "23403", 15, "Paper"))

# Display list of all database entries
# def displayEntries(self):
for i in range(len(ent)):
    print(ent[i])