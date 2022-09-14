import json
import random
import glob

#Sets all files ending with .json from the folder on my desktop to a list called filenames
filenames = (glob.glob('/Users/felixpeng/PycharmProjects/MinecraftTextures/items/*.json'))
finalnames = []
#Adds the name of files to final names
for fullname in filenames:
    finalnames.append((fullname[57:len(fullname)-5]))

#Writes out the randomization script to be written on each json file
for name in finalnames:
    size = (random.randint(1, 50)/10)
    translation1 = random.randint(1, 50)
    translation2 = random.randint(1, 50)
    translation3 = random.randint(1, 50)
    angle1 = random.randint(-90, 90)
    angle2 = random.randint(-90, 90)
    angle3 = random.randint(-90, 90)
    randomization = {"display": {
            "thirdperson_righthand": {
                "rotation": [ angle1, angle2, angle3 ],
                "translation": [ translation1, translation2, translation3 ],
                "scale": [ size, size, size ]
            },
            "thirdperson_lefthand": {
                "rotation": [ angle1, angle2, angle3 ],
                "translation": [ translation1, translation2, translation3 ],
                "scale": [ size, size, size ]
            },
           "firstperson_righthand": {
               "rotation": [ angle1, angle2, angle3 ],
                "translation": [ translation1, translation2, translation3 ],
                "scale": [ size, size, size ]
            },
            "firstperson_lefthand": {
                "rotation": [ angle1, angle2, angle3 ],
                "translation": [ translation1, translation2, translation3 ],
                "scale": [ size, size, size ]
            }
        },}

    #Creates what needs to be added to each json file
    x = open(r'/Users/felixpeng/PycharmProjects/MinecraftTextures/items/'+name+'.json')
    data = json.load(x)
    print(data)
    randomString = json.dumps(randomization)

    #Since there are three different types of items(block, generated, and handheld), each one has the file written slightly differently and set to the variable final
    if (str(data)[22]) == "b":
        final = "{\"parent\": \"minecraft:block/" +name+"\","+(randomString[1:(len(randomString)-1)])+","+"\"textures\": {\"layer0\": \"minecraft:"+name+"\"}}"
    elif (str(data)[27]) == "g":
        final = "{\"parent\": \"minecraft:item/generated\","+(randomString[1:(len(randomString)-1)])+","+"\"textures\": {\"layer0\": \"minecraft:item/"+name+"\"}}"
    else:
        final = "{\"parent\": \"minecraft:item/handheld\","+(randomString[1:(len(randomString)-1)])+","+"\"textures\": {\"layer0\": \"minecraft:item/"+name+"\"}}"

    #Writes the file using the variable final
    with open(name+".json","w") as outfile:
        outfile.write(str(final))





