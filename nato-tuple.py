# nato-tuple.py
#no defined functions just code
nato = (["A", "ALPHA"], ["B", "BRAVO"], ["C", "CHARLIE"],
        ["D", "DELTA"], ["E", "ECHO"], ["F", "FOXTROT"],
        ["G", "GOLF"], ["H", "HOTEL"], ["I", "INDIA"],
        ["J", "JULIET"], ["K", "KILO"], ["L", "LIMA"],
        ["M", "MIKE"], ["N", "NOVEMBER"], ["O", "OSCAR"],
        ["P", "PAPA"], ["Q", "QUEBEC"], ["R", "ROMEO"],
        ["S", "SIERRA"], ["T", "TANGO"], ["U", "UNIFORM"],
        ["V", "VICTOR"], ["W", "WHISKEY"],["X", "XRAY"],
        ["Y", "YANKEE"], ["Z", "ZULU"])
# print the raw tuple
print(nato)
#print a human understandable list
print(nato[0][1])
for n in range(0,26):
    print (n+1,nato[n][0],nato[n][1])
    # notice each print entity n+1  , nato[n][0] and nato[n][1])
    # this is a 2D tuple
