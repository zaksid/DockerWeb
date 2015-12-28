import socket
import pickle

from container_manager import ContainerManager
from utility import *

manager = ContainerManager()

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print ('connected: {0}{1}'.format(addr, '!!'))
    data = pickle.loads(conn.recv(1024))
    print('data: {0}'.format(repr(data)))
    if(data[0] == 'check'):
        conn.close()
    elif(data[0] == 'create'):
        sys_mem = manager.get_system_memory()
        doc_mem = manager.get_memory_usage_for_all()

        if (doc_mem < sys_mem * 0.8):
            conn.send(pickle.dumps(('bibas', 'You\'ve used more then 80\% of memory !!!\n\tDo you really want to continue(yes)?')))
            resp = pickle.loads(conn.recv(1024))
            if (resp == 'no'):
                conn.send(pickle.dumps(('failed')))
                conn.close()
                continue

        container = manager.create_container(data[1], data[3], data[5])

        name = manager.start_container(container)

        add_site_to_hosts(data[2], manager.get_container_ip(name))

        print('container %s was started' % name)

        conn.send(pickle.dumps(('success', name)))
        conn.close()
    elif(data[0] == 'stop'):
        if(manager.stop_container(data[1])):
            conn.send(pickle.dumps(('success', data[1])))
            conn.close()
        else:
            conn.send(pickle.dumps(('failed', data[1])))
            conn.close()
    elif(data == 'containers'):
        conn.send(pickle.dumps(('success', manager.list_containers())))
        conn.close()
    else:
        conn.send(str(data).encode('UTF-8'))

conn.close()