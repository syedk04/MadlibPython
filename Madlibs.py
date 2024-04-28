#how to put strings together
#several ways to do it for example using a variable youtuber

# youtuber = "mommy" #some string variable which would be a youtubers name

#ways to do it

# print("sub to: " + youtuber)
# print("sub to: {}".format(youtuber))
# print(f"sub to: {youtuber}") #most forward way (using this for project)

adj = input("Adjective:") #taking user inputs 
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Celeb: ")

madlib = f"Computer programming is so {adj}! Makes me so excited because I \
love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
