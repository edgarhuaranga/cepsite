from django.http import HttpResponse
from rest_framework.views import APIView
import socket
import time
import threading
from datetime import datetime
import random

HOST = "localhost"
PORT = 9999
data_pattern = "{},{},{}\n"
sensorid = [1, 2]#, 3, 4] #4 sensores
is_listening = False
is_connected = False
close_connection = False
send_data = False

def create_communication_socket():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        is_listening = True
        print("iniciando server socket")
        conn, addr = s.accept()
        print("conectado")
        global send_data
        with conn:
            print(conn)
            is_connected = True
            print(f"Connected by {addr}")
            while True:
                if close_connection:
                    break
                if send_data:
                    try:
                        print("sending ..." + data)
                        conn.sendall(bytes(data, 'utf-8'))
                        send_data = False
                    except BrokenPipeError:
                        print("Se perdió la conexión")
                        break

            if close_connection:
                conn.close()


class SensorItem(APIView):
    def post(self, request):
        data_json = request.data
        global data
        data = data_pattern.format(data_json['sensorid'], data_json['timestamp'], data_json['value'])
        global send_data
        send_data = True
        return HttpResponse("received "+data)


class StartCEP(APIView):
    def post(self, request):
        print("Starting CEP engine...")
        threading.Thread(target=create_communication_socket).start()
        return HttpResponse("======= CEP started =======")


class StopCEP(APIView):
    def post(self, request):
        global close_connection
        close_connection = True
        print("============================")
        print("Stopping CEP engine...")
        print("============================")
        return HttpResponse("======= CEP stopped =======")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

