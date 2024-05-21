import random
import socket
import struct
import time


def neuropype_simulator(update_rate, val_range):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("NeuroPype Simulator: Waiting for a connection...")
    connection, client_address = server_socket.accept()
    print(f"NeuroPype Simulator: Connected to {client_address}")

    try:
        while True:
            min_value = val_range[0]
            max_value = val_range[1]
            data_array = [random.uniform(min_value, max_value) for _ in range(2)]
            data_bytes = struct.pack('2f', *data_array)
            connection.sendall(data_bytes)
            # print(f"sent {data_array}")
            time.sleep(update_rate)  # Simulate data sending every 5 seconds
    finally:
        connection.close()

