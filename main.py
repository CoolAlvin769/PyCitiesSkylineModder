import zipfile, tkinter, ctypes, subprocess, os
from tkinter.filedialog import askopenfilenames

def popout(path):
    subprocess.Popen(f'explorer {os.path.realpath(path)}')
    print("Opened!")


def main():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        MODS = r"C:\Program Files\Epic Games\CitiesSkylines\Files\Mods"
        MODS_LOCAL = r"C:\Users\User\AppData\Local\Colossal Order\Cities_Skylines\Addons\Mods"

        MAPS = r"C:\Program Files\Epic Games\CitiesSkylines\Files\Maps"

        ASSETS = r"C:\Users\User\AppData\Local\Colossal Order\Cities_Skylines\Addons\Assets"

        STYLE = r"C:\Users\User\AppData\Local\Colossal Order\Cities_Skylines\Addons\Styles"

        SCENARIO = r"C:\Program Files\Epic Games\CitiesSkylines\Files"

        move_to = ""

        tkinter.Tk().withdraw()

        location = []

        while 1:
            match input("Select items/Open folder (1/2/l) "):
                case "1":
                    location = askopenfilenames()

                    print(f"Location: {', '.join(location)}" if location else "No file is selected!")
                    if not location: continue
                    inp = input("Confirm to continue? (y/n/l) ")
                    match inp:
                        case "l":
                            return 10
                        case "n":
                            print("Cancelled, please select again!")
                            continue
                        case "y":
                            break
                        case _:
                            print("Invaild use!")
                case "2":
                    match input("Open folder (1.Mods/2.Maps/3.Assets/4.District Style/m to go back to menu/l to leave the program) ").lower():
                        case "1":
                            match input("Local/Global (1/2) "):
                                case "1":
                                    popout(MODS_LOCAL)
                                case "2":
                                    popout(MODS)
                        case "2":
                            popout(MAPS)
                        case "3":
                            popout(ASSETS)
                        case "4":
                            popout(STYLE)
                        case "5":
                            popout(SCENARIO)
                        case "m":
                            continue
                        case "l":
                            return 30
                        case _:
                            print("Invaild use!")
                case "l":
                    return 70
        for i in location:
            print(f"Location: {i}")
            match input("File type (1.Mods, 2.Maps, 3.Assets, 4.District Style, Blank to leave): "):
                case "1":
                    name = input("Rename it as: ")
                    if not name:
                        print("Cancelled!")
                        continue
                    move_to = MODS + f"\{name}"
                    print(f"Moved to global mods folder. (Moved to {move_to})")
                case "2":
                    move_to = MAPS
                case "3":
                    move_to = ASSETS
                case "4":
                    move_to = STYLE
                case "5":
                    move_to = SCENARIO
                case _:
                    return 40

            with zipfile.ZipFile(i, 'r') as zip_ref:
                zip_ref.extractall(move_to)
        print("Finished.")
        return 20
    except Exception as e:
        print(f"Raised an exception: {e}")
        return e

if __name__ == "__main__":
    x = main()
    input("Closed.")