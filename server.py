from host import Host
from container_manager import ContainerManager
from hosts_manager import HostsManager
from utility import *

manager = HostsManager('hosts')
manager.check_available_host()

def find_host():
    list_hosts()

    slave_host = input('slave host: ')
    slave_port = int(input('slave port: '))

    try:
        host = manager.get_host(slave_host, slave_port)
    except Exception as e:
        alert(str(e))
        return None
    return host

def create():
    host = find_host()

    if(host is None):
        return

    # image = input('image name: ')
    # hostname = input('host name: ')
    # memory_size = input('memory_size: ')
    # from_d = input('directory from: ')
    # to_d = input('directory to: ')
    # user = input('user name: ')
    # binds = ['%s:/usr/share/nginx/html:ro' % from_d]

    image = 'nginx'
    hostname = 'wow.com.ua'
    memory_size = 256
    from_d = '/www/aaa/'
    to_d = '/ww/aaa/'
    user = 'vlad'
    binds = ['%s:/usr/share/nginx/html:ro' % "/home/vlad/DockerNginxSimpleStaticSite/html"]

    try:
        name_container = host.create_container(image, hostname, binds, user, memory_size)
        print('Container {0} on slave-machine {1} was started'.format(name_container, host))
    except Exception as e:
        alert(str(e))

def stop():
    host = find_host()

    if(host is None):
        return

    name = input('write the name of the container: ')

    if(host.stop_container(name)):
        print ('Container {0} on slave machine {1} was stopped.'.format(name, host))
    else:
        print ('Something wrong')

def get_containers():
    host = find_host()

    if(host is None):
        return

    print('List of started containers on {0} slave machine:'.format(host))
    for cont in host.get_containers():
        print(cont)

def list_hosts():
    print(manager)

def check():
    manager.check_available_host()
    list_hosts()

while(True):
    arguments = input('> ')
    command = arguments.split(' ')[0]
    if (command == 'exit'):
        print('good bye')
        break
    elif (command == 'create'):
        create()
    elif (command == 'check'):
        check()
    elif (command == 'hosts'):
        list_hosts()
    elif (command == 'stop'):
        stop()
    elif (command == 'containers'):
        get_containers()
    else:
        pass
