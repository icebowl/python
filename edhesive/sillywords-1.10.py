'''Let's play Silly Sentences!

Enter a name: Grace
Enter an adjective: stinky
Enter an adjective: blue
Enter an adverb: quietly
Enter a food: soup
Enter another food: bananas
Enter a noun: button
Enter a place: Paris
Enter a verb: jump

Grace was planning a dream vacation to Paris.
Grace was especially looking forward to trying the local
cuisine, including stinky soup and bananas.

Grace will have to practice the language quietly to
make it easier to jump with people.

Grace has a long list of sights to see, including the
button museum and the blue park.

Your output should be based on this template:

[name] was planning a dream vacation to [place].
[name] was especially looking forward to trying the local
cuisine, including [adjective 1] [food 1] and [food 2].
 
[name] will have to practice the language [adverb] to
make it easier to [verb] with people.
 
[name] has a long list of sights to see, including the
[noun] museum and the [adjective 2] park.

Enter a name: Grace
Enter an adjective: stinky
Enter an adjective: blue
Enter an adverb: quietly
Enter a food: soup
Enter another food: bananas
Enter a noun: button
Enter a place: Paris
Enter a verb: jump

Dolly Madison
rough
smooth
annoyingly
oatmeal
mustard
sheep
Argentina
tickle

'''
name = input( "Enter a name: Grace : ")
adj1 = input ("Enter an adjective: stinky : ")
adj2 = input("Enter an adjective: blue : ")
adv = input("Enter an adverb: quietly : ")
food1 = input("Enter a food: soup : ")
food2 = input("Enter another food: bananas : ")
noun = input("Enter a noun: button : ")
place = input ("Enter a place: Paris : ")
verb = input ("Enter a verb: jump : ")

print (name+" was planning a dream vacation to "+place)
print (name+" was especially looking forward to trying the local")
print ("cuisine, including "+adj1+" "+food1+" and "+food2+".")
print (name+ "will have to practice the language "+ adv+" to")
print ("make it easier to "+verb+" with people.")
print (name+ " has a long list of sights to see, including the")
print (noun + " museum and the "+ adj2+" park.")
