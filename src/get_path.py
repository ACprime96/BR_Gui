import json
def get_file_path(f1):
    rf = open("/Users/adityachandra/Environments/myocr/Gui/config.json")
    config = json.load(rf)
    rf.close()
    wf = open("/Users/adityachandra/Environments/myocr/Gui/config.json","w")
    config["folder_path"] = f1
    config["images"] = f1 + "/images"
    config["english"] = f1 + "/eng.txt"
    config["braille"] = f1 + "/br.txt"
    config["br_img"] = f1 + "/braille_images"
    json.dump(config,wf)
    wf.close()

def get_images():
    rf = open("/Users/adityachandra/Environments/myocr/Gui/config.json")
    config = json.load(rf)
    rf.close()
    return config["images"]

def get_english():
    rf = open("/Users/adityachandra/Environments/myocr/Gui/config.json")
    config = json.load(rf)
    rf.close()
    return config["english"]

def get_braille():
    rf = open("/Users/adityachandra/Environments/myocr/Gui/config.json")
    config = json.load(rf)
    rf.close()
    return config["braille"]

def get_braille_images():
    rf = open("/Users/adityachandra/Environments/myocr/Gui/config.json")
    config = json.load(rf)
    rf.close()
    return config["br_img"]
