# File name: Scheduler.py
# Author: Mark Lee
# Date created: 09/01/2020
# Date last modified: 28/02/2020
# Python Version: 3.8.1x

# ----- Imports -----

import numpy as np
import json
from datetime import datetime

# Import Priority Queue
try:
    from queue import PriorityQueue as PQ
except ImportError:
    from queue import PriorityQueue as PQ

# ----- Instance variables -----

date_time = ""
location = ""
BinID = ""
level = 0
# neighbourhood_id = ""
type = ["Compost", "Waste", "Bottles and Cans", "Paper"]

MAX_LEVEL = 3
MAX_LEVEL_ORGANICS = 10
MAX_NUMBER_OF_ENTRIES = 15000    # May change due to 64GB SD Card size

# ----- Schedule class -----

class Schedule:

    # --- Initialize each database entry object ---

    def __init__(self, date_time, location, BinID, level, type):
        self.date_time = date_time
        self.location = location
        self.BinID = BinID
        self.level = level
        self.type = type

    # Initialize each entry in priority queue
    def __str__(self):
        return ' '.join([str(i)] for i in self.queue)

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
    def get_BinID(self):
        return self._BinID

    # Set ID of bin
    def set_BinID(self, b):
        self._BinID = b

    # Get level of bin
    def get_level(self):
        return self._level

    # Set level of bin
    def set_capacity(self, l):
        self._level = l

    # Get type of garbage in bin
    def get_type(self):
        return self._type

    # Set type of garbage in bin
    def set_type(self, t):
        self._type = t

    # --- Sorting based on attribute ---

    # Sort by date and time
    def sort_date_time(self, ent):
        sorted_entries = sorted(
            ent, key = lambda ent: datetime.strptime(ent['Created'], '%m/%d/%y %H:%M'), reverse=True
        )

    # Sort by location
    # Need to compute the shortest path from user to nearest bin - Phase Three
    #def sort_location(self, ent):

    # Sort by ID
    def sort_BinID(self, ent):
        ent.sort(key = str.lower, reverse = True)


    # Sort by level
    def sort_level(self, ent):
        for i in range(len(ent)):
            min_index = i
            for j in range(i + 1, len(ent)):
                if ent[min_index] > ent[j]:
                    min_index = j
        ent[i], ent[min_index] = ent[min_index], ent[i]

        #new_ent_cap = []
        #minimum = ent[0]  # arbitrary number in list
        #for x in ent:
        #    if x < minimum:
        #        minimum = x
        #new_ent_cap.append(minimum)
        #ent.remove(minimum)

        ent.get_level().sort(reverse = True)

    # Sort by type
    # Priority Order: Compost, Waste, Bottles and Cans, Paper
    def sort_type(self, i):
        def TypeCompost(self, ent):
            print("Sort Compost: rn")
            if self._type == "Compost":
                ent.sort(reverse=True)
            else:
                print("Invalid. Type must be Compost")

        def TypeWaste(self, ent):
            print("Sort Compost: rn")
            if self._type == "Waste":
                ent.sort(reverse=True)
            else:
                print("Invalid. Type must be Waste")


        def TypeBottlesAndCans(self, ent):
            print("Sort Compost: rn")
            if self._type == "Bottles and Cans":
                ent.sort(reverse=True)
            else:
                print("Invalid. Type must be Bottles and Cans.")


        def TypePaper(self, ent):
            print("Sort Compost: rn")
            if self._type == "Paper":
                ent.sort(reverse=True)
            else:
                print("Invalid. Type must be Paper.")


        SortMethod = {
            0: TypeCompost,
            1: TypeWaste,
            2: TypeBottlesAndCans,
            3: TypePaper
        }

        sortSelect = 0
        while (sortSelect != 3):
            print("Compost")
            print("Waste")
            print("Bottles and Cans")
            print("Paper")
            Selection = int(input("Select a sorting method: "))
            if (Selection >= 0) and (Selection < 4):
                SortMethod[Selection]()

        return type.get(i, "Nothing")

    # --- Priority Queue operations ---

    # Check if queue is empty
    def isEmpty(self):
        return len(self.ent) == []

    # Insert element in queue
    def insert(self, ent):
        self.queue.append(ent)

    # Delete element from queue
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print("Cannot delete. Entry not found.")
            exit()

    # --- Other features ---

    # Get details of a database entry
    def get_details(self):
        print(self._date_time, self._location, self._BinID, self._level, self._type)

    # Print all database entries
    def display_entries(self, ent):
        for i in range(len(ent)):
            print(ent[i])

    # Default errors
    def errorMessage(self):
        print("Cannot sort. Please try again.")

# Display list of all database entries
#def display_schedule(self):

def main():
    # Create a dynamic list of database entries
    # Implemented via Priority Queue
    ent = []

    # Append new entries when received
    ent.append(Schedule(datetime, "Rye U", "12345", 10, "Waste"))
    ent.append(Schedule(datetime, "Rye U", "23403", 8, "Paper"))
    ent.append(Schedule(datetime, "Rye U", "01322", 5, "Compost"))
    ent.append(Schedule(datetime, "Rye U", "94943", 9, "Bottles and Cans"))

if __name__  == "__main__":
    main()
