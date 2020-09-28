songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0] + ", " + songs[2])
print(songs[1:3])
songs[2] = "Love Is Only a Feeling"
songs.append("Can You Blame Me")
songs.extend(["Roll Some Mo", "Lucky Night"])
songs.insert(2, "SKELETONS")
songs.remove("Do It")

animals = ["Dogs", "Squirrels", "Monkeys"]
animals.append("Cats")
print(animals[2])
del animals[0]
for i in range(len(animals)):
    print(animals[i])