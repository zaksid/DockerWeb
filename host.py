import pickle
import socket

from utility import *

class Host(object):
    def __init__(self, hostname, port):
        self.host = hostname
        self.port = int(port)

    def __str__(self):
        return (self.host + ':' + str(self.port))

    def equals(self, hostname, port):
        return self.host == hostname and self.port == port

    def create_container(self, image, hostname, bind, user, memory_size):
        container = (
          'create',
          image,
          hostname,
          bind,
          user,
          memory_size,
        )
        sock = socket.socket()
        sock.connect((self.host, self.port))
        sock.send(pickle.dumps(container))
        data = pickle.loads(sock.recv(1024))
        if(data[0] == 'bibas'):
            alert(data[1])
            resp = input()
            sock.send(pickle.dumps((resp)))
            resp = pickle.loads(sock.recv(1024))
            print(resp)
            if(resp[0] != 'success'):
                raise Exception('Somethin went wrong')
            return resp[1]
        return data[1]

    def stop_container(self, name):
        sock = socket.socket()
        sock.connect((self.host, self.port))
        sock.send(pickle.dumps(('stop', name)))
        data = pickle.loads(sock.recv(1024))
        if(data[0] != 'success'):
            return False
        return True

    def get_containers(self):
        sock = socket.socket()
        sock.connect((self.host, self.port))
        sock.send(pickle.dumps(('containers')))
        data = pickle.loads(sock.recv(4096))
        return data[1]