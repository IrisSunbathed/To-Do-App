from ToDo import ToDo
from DataPersistance import load_data


def main():
    data = load_data()
    todo = ToDo.from_dict(data)
    todo.main_menu()

if __name__ == "__main__":
    main()
    



        
    