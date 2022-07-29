import time
import os
import pyvisa

rm = pyvisa.ResourceManager()

# delay between deactivations
delay = 20

# CONFIGURATION - CAEN HiVolta
caen_channel = 7
caen_DELAY = 0.3

caen = rm.open_resource("ASRL/dev/ttyACM0::INSTR")
keysight = rm.open_resource("USB0::10893::3842::MY56006348::0::INSTR")

# CAEN HiVolta deactivation
caen.query(f"$CMD:SET,CH:{caen_channel},PAR:OFF", caen_DELAY)
print(f"\nCAEN HiVolta deactivated on channel {caen_channel}")

time.sleep(delay)

# Keysight N6705C deactivation
keysight.write("OUTP OFF,(@1,3,4)")
print("Keysight N6705C deactivated on channels 1, 3, 4\n")
