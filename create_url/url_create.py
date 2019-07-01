# url_create.py
'''
https://johnmburnside.github.io/
erick-lakkham.githu
'''
name_git = [[1,"JohnB","johnmburnside"],
            [2,"DocC","randomrocket80"],
            [3,"CraigC","liluda"],
            [4,"TrentC","1tspsalt"],
            [5,"OmarC","strixglitch117"],
            [6,"KienanE","comet955"],
            [7,"LeviE","deepspace15"],
            [8,"CalebG","pixel-game-100"],
            [9,"Billy(Won)","obiwonbinobi77"],
            [10,"StevenK","ping-1000"],
            [11,"ConnerK","strightarrow"],
            [12,"ErickL","erick-lakkham"],
            [13,"AnishaM","armadillo111"],
            [14,"Jony5M","jony-5"],
            [15,"WilliamM","queenmercury"],
            [16,"CalebM","jefferson464"],
            [17,"CorbinN","generalcorbin2"],
            [18,"Matteo0","matteo126"],
            [19, "AlexisR","eranzal"],
            [20,"PeterV","MLGChickenYT"],
            [21,"MalachiW","sharpeye125"]
            ]

print(name_git) 
print("\n\n * * * * * * * * * * \n")
urlstring = "<a href = \"https://"+str(name_git[0][2])+".github.io\" target = \"_blank\">"+str(name_git[0][1])+"</a>"
for n in range ( 0,21):
 urlstring = "<a href = \"https://"+str(name_git[n][2])+".github.io\" target = \"_blank\">"+str(name_git[n
 ][1])+"</a>"
 print (urlstring)

print()
 
for n in range ( 0,21):
 urlstring = "<a href = \"https://github.com/"+str(name_git[n][2])+"?tab=repositories target = \"_blank\">"+str(name_git[n
 ][1])+" REPOS </a>"
 print (urlstring)
