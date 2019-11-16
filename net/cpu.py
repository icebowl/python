import platform
print(platform.processor())
import os
mem=str(os.popen('free -t -m').readlines())
print(mem)
mem=str(os.popen('free -m').readlines())
print("\n\n\n * * * * * * * *\n")
print(mem)
