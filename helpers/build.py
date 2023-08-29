print("Building sound_collection.gd and sound_collection_3d from sound_collection_2d.gd")
with open("addons/randaudioplayer/sound_collection_2d.gd", "r", encoding="utf-8") as file:
    original = file.read()
    print("Read", end=" - ")
    with open("addons/randaudioplayer/sound_collection_3d.gd", "w", encoding="utf-8") as output:
        output.write(original.replace("2D", "3D"))
    print("Wrote sound_collection_3d.gd", end=" - ")
    with open("addons/randaudioplayer/sound_collection.gd", "w", encoding="utf-8") as output:
        output.write(original.replace("2D", ""))
    print("Wrote sound_collection.gd")
print("Done")