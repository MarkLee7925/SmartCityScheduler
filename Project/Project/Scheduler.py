# File name: Scheduler.py
# Author: Mark Lee
# Date created: 09/01/2020
# Date last modified: 28/03/2020
# Python Version: 3.8.1x

# --- Imports ---

import numpy as np
import json
from datetime import datetime
from datetime import time
from random import randint
import schedule
import time
import smtplib
import sqlite3
from sqlite3 import Error
from pprint import pprint

# $ --- Global Variables ---
distance_json = 0
id_json = 0
binAr = []

# Import Priority Queue
try:
    from queue import PriorityQueue as PQ
except ImportError:
    from queue import PriorityQueue as PQ

# --- Instance variables ---

date_time = ""
level = 0
distance = 0
type = ["Compost", "Waste", "Bottles and Cans", "Paper"]

MAX_NUMBER_OF_ENTRIES = 15000  # $ - May change due to 64GB SD Card size


# $ Class to represent a Day -- dateTime:   -- id: bin id -- level: current level of bin -- maxLevel: highest
# level last week
# -- pickupDay: the day it will be picked up that week, monday = 0
class Day:
    def __init__(self, day, day_id, bins):
        self.day_id = day_id
        self.bins = bins
        self.day = day

    def get_dayId(self):
        return self.dateTime

    def get_day(self):
        return self.day

    # Get ID of bin
    def get_bins(self):
        return self.bins

    # Set ID of bin
    def set_bins(self, b):
        self.bins.append(b)

    def get_details(self):
        # Get details of a database entry
        details = "\n" + self.day + ": "

        for i in self.bins:
            details += "\n" + i.get_details()
        details += "\n"
        return details

# ----- Bin Class -----
class Bin:
    # $ Class to represent a Bin -- dateTime:   -- id: bin id -- level: current level of bin -- maxLevel: highest
    # level last week
    # -- pickupDay: the day it will be picked up that week, monday = 0
    def __init__(self, dateTime, id, level, _type, maxLevel, pickupDay):
        self.dateTime = dateTime
        self.id = id
        self.level = level
        self._type = _type
        self.maxLevel = maxLevel
        self.pickupDay = pickupDay

    def __repr__(self):
        return '({}, {}, {}, {})'.format(self.dateTime, self.id, self.level, self._type)

    # Initialize each entry in priority queue
    # Throwing error: Instance of 'Bin' has no 'queue'
    # Commented it so I can test the code
    # def __str__(self):
    #     return ' '.join([str(i)] for i in self.queue)

    # --- Getter and Setter methods ---

    # Get date and time of bin
    def get_date_time(self):
        return self.dateTime

    # Set date and time of bin
    def set_date_time(self, dt):
        self.dateTime = dt

    # Get ID of bin
    def get_binID(self):
        return self.id

    # Set ID of bin
    def set_binID(self, b):
        self.id = b

    # Get level of bin
    def get_level(self):
        return self.level

    # Set level of bin
    def set_level(self, l):
        self.level = l

    # Get max level of bin
    def get_maxLevel(self):
        return self.maxLevel

    # Set maxlevel of bin
    def set_maxLevel(self, l):
        self.maxLevel = l

    # Get type of garbage in bin
    def get_type(self):
        return self._type

    # Set type of garbage in bin
    def set_type(self, t):
        self._type = t

    def get_details(self):
        # Get details of a database entry
        details = "Bin: date_created: " + str(self.dateTime) + ", bin_id: " + str(self.id) + ", level: " + str(self.level) + ", max_level: " + str(self.maxLevel) + ", type: " + str(self._type) + ", pickup: " + str(self.pickupDay)
        return details

    # --- Annie --- Getting distance from db turning into level and returning it
    def update_level(self, l):
        if(l == 3):
            return self.set_level(3)
        else:
            return self.set_level(l+1)

    def delete(self):
        # Delete element from queue
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print("Cannot delete. Bin not found.")
            exit()

# --- Sorting based on attribute ---

def sort_date_time(self):
    # ! - Sort by date and time
    global binAr
    sorted_entries = sorted(
        binAr, key=lambda bin: datetime.strptime(bin['Created'], '%m/%d/%y %H:%M'), reverse=True
    )


def sort_binID(self):
    # ! - Sort by ID
    global binAr
    global id_json
    binAr.sort(key=lambda i: i.id_json, reverse=True)


def sort_level():
    # ! - Sort by level
    global binAr
    binAr.sort(key=lambda l: l.level, reverse=True)


def sort_type(self, i):
    # Sort by type
    # Priority Order: Compost, Waste, Bottles and Cans, Paper
    global binAr

    def type_compost(self):
        print("Sort Compost: rn")
        if self._type == "Compost":
            binAr.sort(key=lambda t: t.type, reverse=True)
        else:
            print("Invalid. Type must be Compost")

    def type_waste(self, bin):
        print("Sort Compost: rn")
        if self._type == "Waste":
            bin.sort(key=lambda t: t.type, reverse=True)
        else:
            print("Invalid. Type must be Waste")

    def type_bottles_and_cans(self, bin):
        print("Sort Compost: rn")
        if self._type == "Bottles and Cans":
            bin.sort(key=lambda t: t.type, reverse=True)
        else:
            print("Invalid. Type must be Bottles and Cans.")

    def type_paper(self, bin):
        print("Sort Compost: rn")
        if self._type == "Paper":
            bin.sort(key=lambda t: t.type, reverse=True)
        else:
            print("Invalid. Type must be Paper.")

    sort_method = {
        0: type_compost,
        1: type_waste,
        2: type_bottles_and_cans,
        3: type_paper
    }

    sort_select = 0
    while (sort_select != 3):
        print("Compost")
        print("Waste")
        print("Bottles and Cans")
        print("Paper")
        selection = int(input("Select a sorting method: "))
        if (selection >= 0) and (selection < 4):
            sort_method[selection]()
    # $ Throwing Error: Instance of 'list' has no 'get' for "type"
    # Commented so i can test
    # return type.get(i, "Nothing")
    return 0

    # --- Priority Queue operations ---

def isEmpty(self):
    # ! - Check if queue is empty
    global binAr
    if len(binAr) == 0:
        print("No database entries found")
        return len(self.binAr) == []
    else:
        return len(binAr)

def insert(self, bin):
    # ! - Insert element in queue
    global binAr
    self.queue.append(binAr)

# --- Other features ---

def display_entries():
    # ! - Display all sorted database entries (using Pretty Print)
    global binAr
    for i in range(len(binAr)):
        print(binAr[i])


# Default errors
def errorMessage(self):
    print("Cannot sort. Please try again.")

# ----- @ - SQLite Database Connection -----
# ---
def create_connection(db_file):
    # @ - Create a database connection to the SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


# --- ANNIE ---


def select_all_tasks(conn):
    # @ - Query all rows in the tasks table
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    bin = cur.fetchall()

    for row in bin:
        print(row)


# --- ANNIE ---


def select_task_by_priority(conn, priority):
    # @ - Query tasks by priority
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()

    for row in rows:
        print(row)


# ----- Client Notifications -----

# --- DENZEL ---


def SendNotifyEmail(message):
    sender_email = "applicationsmartcity@gmail.com"
    password = "wvpxgjzlkprhcmtr"
    to = "marklee7925@gmail.com"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        print(message)
        server.sendmail(sender_email, to, message)
        server.quit()
        print("Email sent.")
    except:
        print("Error! Email Cant be Sent")


def checkBins():
    # $ Loop through bin entries and see which bins have level 3,
    # notify when bins are full and set their max levels to their current highest level
    print("\nCheck Bins")
    global binAr
    for i in binAr:
        if i.get_level() == 3:
            i.set_maxLevel(3)
        elif i.get_level() == 2:
            i.set_maxLevel(2)
        elif i.get_level() == 1:
            i.set_maxLevel(1)
        print(i.get_details())

def clientSchedule():
    # $ Iterate through the bins and check the max level if level 1 schedule it to Friday,
    # if level = 2 schedule to Thursday, if level = 3 schedule to Wednesday
    # When scheduling is finished will have to make it so they get the correct schedule
    global binAr
    wBin = [bin1,bin2,bin3]
    tBin = [bin1,bin2,bin3]
    fBin = [bin1,bin2,bin3]

    print("\nSchedule Created")

    for i in binAr:
        if i.maxLevel == 3:
            i.pickupDay = 2

            for x in wBin:
                if x.get_binID() == i.get_binID:
                    wBin[wBin.index(x)] = i
                    break
                else:
                    wBin[wBin.index(x)] = x

            if i in tBin:
                tBin.remove(i)
            if i in fBin:
                fBin.remove(i)

        elif i.maxLevel == 2:
            i.pickupDay = 3

            for x in wBin:
                if x.get_binID() == i.get_binID:
                    wBin[wBin.index(x)] = i
                    break
                else:
                    wBin[wBin.index(x)] = x

            if i in wBin:
                wBin.remove(i)
            if i in fBin:
                fBin.remove(i)

        elif i.maxLevel == 1:
            i.pickupDay = 4

            for x in wBin:
                if x.get_binID() == i.get_binID:
                    wBin[wBin.index(x)] = i
                    break
            else:
                wBin[wBin.index(x)] = x

            if i in tBin:
                tBin.remove(i)
            if i in wBin:
                wBin.remove(i)
        print(i.get_details())

    wednesday = Day("Wednesday", 2, wBin)
    thursday = Day("Thursday", 3, tBin)
    friday = Day("Friday", 4, fBin)
    SendNotifyEmail(wednesday.get_details() + thursday.get_details() + friday.get_details())

# ----- MARK, ANNIE -----

# $ Since we're using the global variable we don't need to use self
# it was throwing and error cause we're not actually using what was sent
def update_entries():
    # ! - Update the bin levels for each entry
    global binAr
    print("\nEntries updated")
    entry_level = 0
    # Iterate through all database entries
    for j in binAr:
        j.update_level(j.get_level())#  Update query in database - ANNIE
        print(j.get_details())
        # If bin(s) is/are at max level (3), send notification to client


# --- MARK ---


def distance_to_level(distance_json):
    # ! - Convert distance (in cm) into level
    # Return an integer that makes a level
    # Takes a bin id and returns an integer representing a level
    print("Level was Found")

    bin_level = 0
    if distance_json >= 0 and distance_json < 25:
        bin_level = 1
    elif distance_json >= 25 and distance_json < 50:
        bin_level = 2
    elif distance_json >= 50 and distance_json <= 75:
        bin_level = 3
    else:
        return -1
    # Update bin level
    # Send prompt to client
    print(bin_level)
    return bin_level


# ----- Main Program -----

# --- MARK, ANNIE ---
# $ It's using vatiables that aren't instantiated and it's throwing errors
def main(id, level):
    global distance_json
    global id_json
    global binAr

    # ! - CALL ALL FUNCTIONS IN SPECIFIED ORDER (will update later ...)

    # Establish SQLite database connection
    conn = create_connection('hcdata.db')
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn, 1)

        print("2. Query all tasks")
        select_all_tasks(conn)

    # Append each database element to a priority queue.
    # binAr.append(Bin(datetime, id_json, distance_json))
    # ! - Check if queue is binAr is empty first.
    binAr.isEmpty()
    sort_level()  # Sort bins by level
    display_entries()  # Display all database bin entries


# --- MARK, DENZEL ---
if __name__ == "__main__":

    # $ Bin distance and ID will have to add for their date and time
    # distance = (distance_json['distance']) -- For testing purpose going to use dummy data instead
    # id = (id_json['id'])

    distance = 30  # First Dummy Bin
    id = 1
    distance2 = 60  # Second Dummy Bin
    id2 = 2
    distance3 = 20  # Third Dummy Bin
    id3 = 3
    distance4 = 35
    id4 = 4

    # Convert distance to level
    level1 = distance_to_level(distance)
    level2 = distance_to_level(distance2)
    level3 = distance_to_level(distance3)

    # $ Create 2 bins for testing
    # BIN(self, dateTime, id, level, _type, maxLevel, pickupDay):

    bin1 = Bin(datetime.now().strftime("%H:%M:%S"), id, level1, 0, 0, 0)
    bin2 = Bin(datetime.now().strftime("%H:%M:%S"), id2, level2, 1, 0, 0)
    bin3 = Bin(datetime.now().strftime("%H:%M:%S"), id3, level3, 2, 0, 0)


    print("Bins Were Created")
    print(bin1.get_details())
    print(bin2.get_details())
    print(bin3.get_details())

    # $ Add the bins to the global bin array
    binAr.append(bin1)
    binAr.append(bin2)
    binAr.append(bin3)

    #$ Every hour update the bins -- Send the array of bins to the update method go through them
    #and update the bins in the array -- Implement
    schedule.every().minute.do(update_entries)

    # $ Loop through bin entries and see which bins have level 3, if full notify and set their maxLevels
    # to what it currently is
    schedule.every().minute.do(checkBins)

    # $ Every Week (Sunday) notify clients of the schedule created
    schedule.every().minutes.do(clientSchedule)

    # $ run the schedule
    while 1:
        schedule.run_pending()
        time.sleep(15)

# -------- UPDATES: ----------

# Student A: Mark Lee (!)
# Student B: Denzel Edwards ($)
# Student C: Anne Li (@)
# Student D: Le Tran (&)

# --- March 25, 2020 - Denzel ($) ---
# I made a bunch of changes and this is just a summary I also included them
# at the end of the scheduler file:I made the bin array a global variable so
# it could be accessed everywhere so the different methods could access it
# $ - The changes I made: we create two bins and put them in the bin array
# every hour theyre updated (I didnt implement this)
# $ - Then we check the bins every hour in the array to see which bins are
# at level 3, if theyre at level 3 notify immediately and set its
# $ - max level for that week to 3, if we're at level 2 set its max level
# for the week to 2 (if its higher the next check itll be set
# $ - accordingly). After that every sunday we create a schedule by looking
# at the bins past max levels and scheduling it by day
# $ - according to which bins were the fullest. Monday = 0, tuesday = 1,
# etc.. and we assign them a pickup day if the max level reached
# $ - the week before was 3 schedule it wednesday(2), 2 then thursday(3),
# 1 then friday (4) and send an email to the client (have to make
# $ - the email more specified).

# --- March 27, 2020 - Mark (!) ---
# ! - Deleted the old "Schedule" class. All code have been transferred to Denzel's "Bin" class.
# ! - Convert all bin list to global binAr (bin array)
# ! - Instantiated global binAr for all methods using the bin array
# ! - Reorganized the methods as follows:
#   - Bin Class
#   - SQLite Database Connection
#   - Client Notifications
#   - Main Program
#   - Updates

# --- March 27, 2020 - Denzel ($) ---
# $ Edited the update_entries function deleted self and change it to j.update_levels for error correction.
# $ Put a comment over the main function

# --- March 28, 2020 - Denzel ($) ---
# Debugged the project so it can be run
# $ Made the email information global
# so that we could call the scheduler
# $ Added type to the Bin class parameters.
# $ # Throwing error: Instance of 'Bin' has no 'queue'
# Commented it so I can test the code:
# def __str__(self):
# $ Create update_level function in Bin class(Just empty class)
# $  #$ Throwing Error: Instance of 'list' has no 'get' for "type"
# Commented so i can test
# return type.get(i, "Nothing")
# $ Generally debugged the code so it can be run

# --- March 27, 2020 - Mark (!) ---
# ! - In main, need to verify if binAr is empty. If so, do not sort.
# ! - Display database entries using Pretty Print (method: display_entries())

# --- April 2, 2020 - Denzel ($) ---
#- Added random import
#- Included type as a parameter
#- Created getter and setter for max level
#- Remade get_details method
#- Put temporary implementation of update_level
#- deleted pretty print
#-created new bin and updated methods
#-