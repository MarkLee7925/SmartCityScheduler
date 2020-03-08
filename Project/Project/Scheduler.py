# File name: Scheduler.py
# Author: Mark Lee
# Date created: 09/01/2020
# Date last modified: 07/03/2020
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

    def __init__(self, date_time, BinID, level, type):
        self.date_time = date_time
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
    def sort_date_time(self, bin):
        sorted_entries = sorted(
            bin, key = lambda bin: datetime.strptime(bin['Created'], '%m/%d/%y %H:%M'), reverse=True
        )

    # Sort by location
    # Need to compute the shortest path from user to nearest bin - Phase Three
    #def sort_location(self, bin):

    # Sort by ID
    def sort_BinID(self, bin):
        bin.sort(key = str.lower, reverse = True)


    # Sort by level
    def sort_level(self, bin):
        for i in range(len(bin)):
            min_index = i
            for j in range(i + 1, len(bin)):
                if bin[min_index] > bin[j]:
                    min_index = j
        bin[i], bin[min_index] = bin[min_index], bin[i]

        #new_bin_cap = []
        #minimum = bin[0]  # arbitrary number in list
        #for x in bin:
        #    if x < minimum:
        #        minimum = x
        #new_bin_cap.append(minimum)
        #bin.remove(minimum)

        bin.get_level().sort(reverse = True)

    # Sort by type
    # Priority Order: Compost, Waste, Bottles and Cans, Paper
    def sort_type(self, i):
        def TypeCompost(self, bin):
            print("Sort Compost: rn")
            if self._type == "Compost":
                bin.sort(reverse=True)
            else:
                print("Invalid. Type must be Compost")

        def TypeWaste(self, bin):
            print("Sort Compost: rn")
            if self._type == "Waste":
                bin.sort(reverse=True)
            else:
                print("Invalid. Type must be Waste")


        def TypeBottlesAndCans(self, bin):
            print("Sort Compost: rn")
            if self._type == "Bottles and Cans":
                bin.sort(reverse=True)
            else:
                print("Invalid. Type must be Bottles and Cans.")


        def TypePaper(self, bin):
            print("Sort Compost: rn")
            if self._type == "Paper":
                bin.sort(reverse=True)
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
        return len(self.bin) == []

    # Insert element in queue
    def insert(self, bin):
        self.queue.append(bin)

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
    def display_entries(self, bin):
        for i in range(len(bin)):
            print(bin[i])

    # Default errors
    def errorMessage(self):
        print("Cannot sort. Please try again.")

# Display list of all database entries
#def display_schedule(self):

def main():
    # Create a dynamic list of database entries
    # Implemented via Priority Queue
    bin = []

    # Append new entries when received
    bin.append(Schedule(datetime, "12345", 10, "Waste"))
    bin.append(Schedule(datetime, "23403", 8, "Paper"))
    bin.append(Schedule(datetime, "01322", 5, "Compost"))

    # Create list of trucks
    truck = []

    # Append truck entries
    #truck.append(self, "32423", )

if __name__  == "__main__":
    main()
