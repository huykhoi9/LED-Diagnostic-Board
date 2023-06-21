import labjack.ljm as ljm

# Open a connection to the labjack device
handle = ljm.openS("T7", "USB", "ANY")

# Operations
channels = ["FIO0", "FIO1", "FIO2", "FIO3"]
ON = 1
OFF = 0

while True:
    # Ask the user to input the pin they want to configure:
    user_input = int(input("Enter pin: "))

    # Turn on or turn off the LED:
    if ljm.eReadName(handle, f"FIO{channels[user_input]}") == OFF:
        ljm.eWriteName(handle, f"FIO{channels[user_input]}", ON)
        print(f"{channels[user_input]} ON")
    else:
        ljm.eWriteName(handle, f"FIO{channels[user_input]}", OFF)
        print(f"{channels[user_input]} OFF")

# Close the connection
ljm.close(handle)

