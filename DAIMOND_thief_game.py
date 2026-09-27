print("======================================")
print("        💎 DIAMOND THEFT CASE 💎")
print("======================================")

print("\nA diamond worth ₹50,00,000 has been stolen!")
print("There are 5 suspects.")
print("You have to find the real thief.\n")

suspects = ["Rahul", "Amit", "Vijay", "Sameer", "Karan"]

print("Suspects:")
print("1.", suspects[0])
print("2.", suspects[1])
print("3.", suspects[2])
print("4.", suspects[3])
print("5.", suspects[4])

print("\n🔎 Investigation Started...")


# ======================================
#          SUSPECT DETAILS
# ======================================

suspect_details = {

    "Rahul": {
        "age": 28,
        "shirt": "Black",
        "pant": "Blue",
        "shoes": "White",
        "vehicle": "Bike"
    },

    "Amit": {
        "age": 29,
        "shirt": "Black",
        "pant": "Grey",
        "shoes": "Black",
        "vehicle": "Bike"
    },

    "Vijay": {
        "age": 27,
        "shirt": "Navy Blue",
        "pant": "Black",
        "shoes": "White",
        "vehicle": "Bike"
    },

    "Sameer": {
        "age": 30,
        "shirt": "Black",
        "pant": "Blue",
        "shoes": "Grey",
        "vehicle": "Scooter"
    },

    "Karan": {
        "age": 28,
        "shirt": "Dark Grey",
        "pant": "Black",
        "shoes": "Black",
        "vehicle": "Bike"
    }
}


# ======================================
#          ENTRY & EXIT DETAILS
# ======================================

suspect_details["Rahul"]["entry_gate"] = "North Gate"
suspect_details["Rahul"]["exit_gate"] = "East Gate"
suspect_details["Rahul"]["entry_time"] = "9:55 PM"
suspect_details["Rahul"]["exit_time"] = "10:35 PM"

suspect_details["Amit"]["entry_gate"] = "North Gate"
suspect_details["Amit"]["exit_gate"] = "South Gate"
suspect_details["Amit"]["entry_time"] = "10:00 PM"
suspect_details["Amit"]["exit_time"] = "10:30 PM"

suspect_details["Vijay"]["entry_gate"] = "West Gate"
suspect_details["Vijay"]["exit_gate"] = "South Gate"
suspect_details["Vijay"]["entry_time"] = "10:05 PM"
suspect_details["Vijay"]["exit_time"] = "10:40 PM"

suspect_details["Sameer"]["entry_gate"] = "West Gate"
suspect_details["Sameer"]["exit_gate"] = "East Gate"
suspect_details["Sameer"]["entry_time"] = "9:50 PM"
suspect_details["Sameer"]["exit_time"] = "10:25 PM"

suspect_details["Karan"]["entry_gate"] = "North Gate"
suspect_details["Karan"]["exit_gate"] = "East Gate"
suspect_details["Karan"]["entry_time"] = "10:05 PM"
suspect_details["Karan"]["exit_time"] = "10:35 PM"


# ======================================
#          ROUTE & ACTIVITIES
# ======================================

suspect_details["Rahul"]["route"] = [
    "North Gate",
    "Parking",
    "Lobby",
    "Cafe",
    "East Gate"
]

suspect_details["Rahul"]["activities"] = [
    "Parked his bike",
    "Bought a coffee",
    "Talked to a security guard"
]


suspect_details["Amit"]["route"] = [
    "North Gate",
    "Parking",
    "Lobby",
    "Security Area",
    "South Gate"
]

suspect_details["Amit"]["activities"] = [
    "Parked his bike",
    "Checked his phone",
    "Talked to a guard"
]


suspect_details["Vijay"]["route"] = [
    "West Gate",
    "Parking",
    "Lobby",
    "Vault Area",
    "South Gate"
]

suspect_details["Vijay"]["activities"] = [
    "Parked his bike",
    "Visited the lobby",
    "Looked around the vault area"
]


suspect_details["Sameer"]["route"] = [
    "West Gate",
    "Lobby",
    "Cafe",
    "Parking",
    "East Gate"
]

suspect_details["Sameer"]["activities"] = [
    "Ordered coffee",
    "Checked his phone",
    "Returned to the parking area"
]


suspect_details["Karan"]["route"] = [
    "North Gate",
    "Parking",
    "Lobby",
    "Vault Area",
    "East Gate"
]

suspect_details["Karan"]["activities"] = [
    "Parked his bike",
    "Visited the lobby",
    "Looked around the vault area"
]


# ======================================
#              CASE CLUES
# ======================================

clues = [
    "The thief entered between 10:00 PM and 10:10 PM.",
    "The thief used a two-wheeler.",
    "The thief entered through North or West Gate.",
    "The thief visited the Lobby after entering.",
    "The thief was near the Vault Area around 10:15 PM.",
    "The thief did not use the Cafe.",
    "The thief left through East or South Gate."
]


# ======================================
#            CCTV EVIDENCE
# ======================================

cctv = [
    "Camera 1: Person entered around 10:05 PM.",
    "Camera 2: Person stayed in the parking area.",
    "Camera 3: Person entered the Lobby.",
    "Camera 4: Person was near the Vault Area.",
    "Camera 5: Person exited through East or South Gate."
]


# ======================================
#            ACTUAL THIEF
# ======================================

real_thief = "Karan"
score = 100


# ======================================
#          INVESTIGATION MENU
# ======================================

investigating = True

while investigating:

    print("\n======================================")
    print("        🕵️ INVESTIGATION MENU")
    print("======================================")

    print("1. Check Suspects")
    print("2. Check CCTV Evidence")
    print("3. Check Gate Records")
    print("4. Check Routes & Activities")
    print("5. Check Case Clues")
    print("6. Make Final Guess")
    print("7. Exit Investigation")

    choice = input("\nEnter your choice: ")


    # ==================================
    #       1. CHECK SUSPECTS
    # ==================================

    if choice == "1":

        print("\n========== SUSPECT DETAILS ==========")

        for name in suspects:

            print("\nName:", name)
            print("Age:", suspect_details[name]["age"])
            print("Shirt:", suspect_details[name]["shirt"])
            print("Pant:", suspect_details[name]["pant"])
            print("Shoes:", suspect_details[name]["shoes"])
            print("Vehicle:", suspect_details[name]["vehicle"])


    # ==================================
    #       2. CHECK CCTV
    # ==================================

    elif choice == "2":

        print("\n========== CCTV EVIDENCE ==========")

        for evidence in cctv:
            print("-", evidence)


    # ==================================
    #       3. CHECK GATE RECORDS
    # ==================================

    elif choice == "3":

        print("\n========== GATE RECORDS ==========")

        for name in suspects:

            print("\nName:", name)
            print("Entry Gate:", suspect_details[name]["entry_gate"])
            print("Exit Gate:", suspect_details[name]["exit_gate"])
            print("Entry Time:", suspect_details[name]["entry_time"])
            print("Exit Time:", suspect_details[name]["exit_time"])


    # ==================================
    #       4. ROUTES & ACTIVITIES
    # ==================================

    elif choice == "4":

        print("\n========== ROUTES & ACTIVITIES ==========")

        for name in suspects:

            print("\nName:", name)

            print("Route:")

            for place in suspect_details[name]["route"]:
                print("->", place)

            print("Activities:")

            for activity in suspect_details[name]["activities"]:
                print("-", activity)


    # ==================================
    #       5. CHECK CLUES
    # ==================================

    elif choice == "5":

        print("\n========== CASE CLUES ==========")

        for i in range(len(clues)):
            print(i + 1, ".", clues[i])


    # ==================================
    #       6. FINAL GUESS
    # ==================================

    elif choice == "6":

        print("\n======================================")
        print("          🔎 FINAL GUESS")
        print("======================================")

        print("\nWho do you think is the thief?\n")

        for i in range(len(suspects)):
            print(i + 1, ".", suspects[i])

        guess = int(input("\nEnter suspect number: "))

        if guess >= 1 and guess <= 5:

            selected_suspect = suspects[guess - 1]

            print("\nYour guess:", selected_suspect)

            if selected_suspect == real_thief:

                print("\n🎉 CONGRATULATIONS!")
                print("You caught the diamond thief! 💎")
                print("Thief:", real_thief)
                print("Score:", score)

            else:

                score = 0

                print("\n❌ WRONG GUESS!")
                print("You accused the wrong person.")
                print("The real thief escaped! 🏃")
                print("Your Score:", score)

            investigating = False

        else:

            print("\n❌ Invalid suspect number!")


    # ==================================
    #       7. EXIT
    # ==================================

    elif choice == "7":

        print("\nInvestigation closed.")
        investigating = False


    else:

        print("\n❌ Invalid choice! Please try again.")