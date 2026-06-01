import json
import pathlib

FILE_ADRESS = f"{pathlib.Path().resolve()}\data\saved_data.json"



def save_data(to_do, ind = 4) :
    with open(FILE_ADRESS, "w") as file :
        json.dump(
            to_do.to_dict(),
            file,
            indent= ind
        )

def load_data() :
    with open(FILE_ADRESS, "r") as file :
        data = json.load(file)
    return data
    
