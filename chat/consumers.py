import json
from channels.generic.websocket import WebsocketConsumer

class ChattingConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        self.send(text_data=json.dumps({
            'message': '연결 성공'
        }))

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     print('Message: ', message)
    
    # def disconnect(self, close_code):
    #     pass
    
