# File name: Scheduler.py
# Author: Mark Lee
# Date created: 09/01/2020
# Date last modified: 15/01/2020
# Python Version: 3.8.1

# ----- Imports -----

import numpy as np
import json
from datetime import datetime

# ----- Instance variables -----

time = 0
date = ""
location = ""
id = ""
capacity = 0
type = ["Waste", "Bottles", "Paper", "Compost"]  # Based on priority


# ----- Schedule class -----

class Schedule:

    # --- Initialize each database entry object ---

    def __init__(self, date_time, location, id, capacity, type):
        self.date_time = date_time
        self.location = location
        self.id = id
        self.capacity = capacity
        self.type = type

    # --- Getter and Setter methods ---

    # Get date and time of bin
    def get_date_time(self):
        return self._date_time

    # Set date and time of bin
    def set_date_time(self, dt):
        self._date_time = dt

    # Get location of bin
    def get_location(self):
        return self._location

    # Set location of bin
    def set_location(self, l):
        self._location = l

    # Get ID of bin
    def get_id(self):
        return self._id

    # Set ID of bin
    def set_id(self, i):
        self._id = i

    # Get capacity of bin
    def get_capacity(self):
        return self._capacity

    # Set capacity of bin
    def set_capacity(self, c):
        self._capacity = c

    # Get type of garbage in bin
    def get_type(self):
        return self._type

    # Set type of garbage in bin
    def set_type(self, t):
        self._type = t

    # --- Sorting based on attribute ---

    # Sort by date and time

    # Sort by location

    # Sort by ID
    def sort_id(ent):
        for i in range(len(ent)):
            min_index = i
            for j in range(i + 1, len(ent)):
                if ent[min_index] > ent[j]:
                    min_index = j
        ent[i], ent[min_index] = ent[min_index], ent[i]

    # Sort by capacity

    # Sort by type
    # Priority Order: Waste, Bottles, Paper, Compost

    # --- Other features ---

    # Get details of a database entry
    def get_details(self):
        print(self._date_time, self._location, self._id, self._capacity, self._type)


# Create a dynamic list of database entries
ent = []
# n = len(ent)  # Length of list

# Append new entries when received

ent.append(Schedule(datetime, "Rye U", "12345", 10, "Waste"))
ent.append(Schedule(datetime, "Rye U", "23403", 15, "Paper"))

# Display list of all database entries
# def display_entries(self):
for i in range(len(ent)):
    print(ent[i])
