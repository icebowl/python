# solarized_math_.py
"""
base03      0  43  54
base02      7  54  66
base01      88 110 117
base00     101 123 131
base0      131 148 150
base1      147 161 161
base2      238 232 213
base3       253 246 227
yellow      181 137   0
orange     203  75  22
red        220  50  47
magenta    211  54 130
violet     108 113 196
blue        38 139 210
cyan       42 161 152
green       65 133 153
"""
def main():
    sn = ["base03","base02" , "base01",  "base00", "base0", "base1" , "base2", "base3", "yellow", "orange",  "red", "magenta" , "violet",  "blue",  "cyan", "green"]
    sl =[[0,43,54],[7 , 54,  66],[88 ,110 ,117], [101 ,123, 131], [131,148,150],
        [147,161,161],[238, 232, 213],[253,246,227], [181,137,0] ,[203,75, 22],
        [220,50,47],[211,54,130],[108,113,196],[38,139,210],[42,161,152],
        [65 ,133 ,153]]
    print(sn)
    print(sl)
    print(sl[0][1])
    print(sl[0][2])
    print ("***************************")
    for r in range (0,16):
        print(sl[r][0],sl[r][1],sl[r][2])
    for n in range (0,16):
        print(sn[n],"   " , sl[n][0]/255,",",sl[n][1]/255,",",sl[n][2]/255)



main()
