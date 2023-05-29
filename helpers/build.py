with open("addons/randaudioplayer/sound_collection_2d.gd", "r", encoding="utf-8") as file:
    original = file.read()
    with open("addons/randaudioplayer/sound_collection_3d.gd", "w", encoding="utf-8") as output:
        output.write(original.replace("2D", "3D"))
    with open("addons/randaudioplayer/sound_collection.gd", "w", encoding="utf-8") as output:
        output.write(original.replace("2D", ""))