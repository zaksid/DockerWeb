import socket
import pickle
from host import Host

class HostsManager():

    def __init__(self, filename):
        self.hosts = []
        self.read_hosts_from(filename)

    def check_available_host(self):
        not_available = []

        sock = socket.socket()
        sock.settimeout(10)

        self.read_hosts_from(self.filename)
        for host in self.hosts:
            try:
                sock.connect((host.host, host.port))
                sock.send(pickle.dumps('check'))
                sock.close()
            except:
                not_available.append(host)

        self.hosts = [available for available in self.hosts if available not in not_available]

    def read_hosts_from(self, filename):
        self.hosts = []
        self.filename = filename

        hosts_file = open(filename, 'r')

        for line in hosts_file:
            hostname, port = line.strip().split(':')
            if (hostname is None) or (port is None):
                continue
            host = Host(hostname, port)
            self.hosts.append(host)
        hosts_file.close()

    def check_hosts(self):
        filename = input('please enter hosts-file: ')
        self.read_hosts_from(filename)
        self.check_available_host(self.socket, hosts)

    def __str__(self):
        result = 'list of available hosts:'
        for host in self.hosts:
            result += "\n\t" + str(host)
        return result

    def get_host(self, hostname, port):
        try:
            return [host for host in self.hosts if host.equals(hostname, port)][0]
        except:
            raise Exception('{0}:{1} does not found'.format(hostname, port))
