from serial import *
import serial.tools.list_ports
import time
import os
import pyvisa

rm = pyvisa.ResourceManager()

# delay between activations
delay = 5

# CONFIGURATION - KEYSIGHT N6705C
# Channel 1
keysight_vset_ch1 = 2.4
keysight_iset_ch1 = 0.5
# Channel 3
keysight_vset_ch3 = 2.4
keysight_iset_ch3 = 0.15
# Channel 4
keysight_vset_ch4 = 3.3
keysight_iset_ch4 = 0.05

# CONFIGURATION - CAEN HiVolta
caen_vmax = 250
caen_imax = 10 
caen_channel = 7
caen_rup = 250
caen_rdwn = 250
caen_trip = 10
caen_imrange = 'HIGH'
caen_DELAY = 1
caen_DELAY_SETTLING = 1

# Keysight N6705C setting
keysight = rm.open_resource('USB0::10893::3842::MY56006348::0::INSTR')
keysight.write(f'VOLTage:LEVel {keysight_vset_ch1},(@1);:CURRent:LEVel {keysight_iset_ch1},(@1)')
keysight.write(f'VOLTage:LEVel {keysight_vset_ch3},(@3);:CURRent:LEVel {keysight_iset_ch3},(@3)')
keysight.write(f'VOLTage:LEVel {keysight_vset_ch4},(@4);:CURRent:LEVel {keysight_iset_ch4},(@4)')

# CAEN HiVolta setting
caen = rm.open_resource('ASRL/dev/ttyACM0::INSTR')
caen.query('$CMD:SET,PAR:BDCLR')
caen.write('*RST')
caen.query(f'$CMD:SET,CH:{caen_channel},PAR:VSET,VAL:{caen_vmax}', caen_DELAY)
caen.query(f'$CMD:SET,CH:{caen_channel},PAR:ISET,VAL:{caen_imax}', caen_DELAY)
caen.query(f'$CMD:SET,CH:{caen_channel},PAR:IMRANGE,VAL:{caen_imrange}', caen_DELAY)
caen.query(f'$CMD:SET,CH:{caen_channel},PAR:RUP,VAL:{caen_rup}', caen_DELAY)
caen.query(f'$CMD:SET,CH:{caen_channel},PAR:RDWN,VAL:{caen_rdwn}', caen_DELAY)
caen.query(f'$CMD:SET,CH:{caen_channel},PAR:TRIP,VAL:{caen_trip}', caen_DELAY)

# Keysight N6705C activation
keysight.write('OUTP ON,(@1,3,4)')
print('\nKeysight N6705C activated on channels 1, 3, 4')

time.sleep(delay)

# CAEN HiVolta activation
caen.query(f'$CMD:SET,CH:{caen_channel},PAR:ON',caen_DELAY)
print(f'CAEN HiVolta activated on channel {caen_channel}\n')