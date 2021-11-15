import websocket
from network.MessageHandler import MessageHandler
from typing import List
import threading

class Socket:
    def __init__(self, server: str, handlers: List[MessageHandler]):
        self.__handlers = handlers
        self.__ws = websocket.WebSocketApp(server,
                                           on_open=self.__on_open,
                                           on_message=self.__on_message,
                                           on_error=self.__on_error,
                                           on_close=self.__on_close)
        
    def run(self):
        self.__ws.run_forever()

    def __on_message(self, ws, message):
        print(message)
        threading.Thread(target=self.__async_on_message, args=(ws,message,)).start()

    def __async_on_message(self, ws, message):
        for handler in self.__handlers:
            handler.handle(message)

    def __on_error(self, ws, error):
        print(error)

    def __on_close(self, ws, close_status_code, close_msg):
        print("### closed ###")

    def __on_open(self, ws):
        print("### open ###")

    def send(self, data):
        self.__ws.send(data)
