import os
frequency = 131 # Hertz
duration  = 500 # milliseconds
os.system('play -n synth %s sin %s' % (duration/1000, frequency))
