# Checking if SUMO is installed and the environment variable is declared
import os
import sys

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
    print("SUCCESS")
else:
    sys.exit("Please declare environment variable 'SIMO_HOME'")
    print("FALIURE")

# Now establishing the connection b/w SUMO and our Python script
import traci

# Declaring the path to the sumo-gui bin file
sumoBin = "/opt/sumo-1.7.0/bin/sumo-gui"
sumoCmd = [sumoBin, "-c", "reduced_sim.sumocfg"]

# Starting the interface 
traci.start(sumoCmd)
step = 0
while step < 1000:
    traci.simulationStep()
    step += 1

traci.close()