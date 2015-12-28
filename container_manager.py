import docker
import utility
from psutil import virtual_memory

class ContainerManager:

    def __init__(self):
        self.client = docker.Client()

    def create_container(self, image, binds, memory='256m'):
        volumes = [x.split(':')[0] for x in binds]
        container = self.client.create_container(
            image=image,
            stdin_open=True,
            tty=False,
            # mem_limit=memory,
            volumes=volumes,
            host_config=self.client.create_host_config(binds=binds)
        )
        return container

    def start_container(self, container):
        self.client.start(container)
        return self.client.inspect_container(container)['Name']

    def stop_container(self, name):
        container = self.find_container(name)
        if (container is False):
            return False
        self.client.stop(container)
        return True

    def get_container_ip(self, name):
        container = self.find_container(name)
        if (container is False):
            return False
        info = self.client.inspect_container(container)
        return info['NetworkSettings']['IPAddress']

    def get_full_information(self, name):
        container = self.find_container(name)
        if (container is False):
            raise MyException('error')
            return False
        return self.client.inspect_container(container)

    def list_containers(self):
        return [self.client.inspect_container(container)['Name'] for container in self.client.containers()]

    def get_system_memory(arg):
        mem = virtual_memory()
        return int(mem.total)  # total physical memory available

    def get_memory_usage_for_all(self):
        containers_id = []
        for container in self.client.containers():
            containers_id.append(self.client.inspect_container(container)['Id'])

        mem = []
        overall_memory_usage = 0
        for container in containers_id:
            filename = "/sys/fs/cgroup/memory/docker/"+container+"/memory.usage_in_bytes"
            f = open(filename);
            mem.append(int(f.read().strip()))
            f.close()

        for i in mem:
            overall_memory_usage += i

        return overall_memory_usage

    def find_container(self, name):
        container = utility.contains(self.client.containers(), lambda x: self.client.inspect_container(x)['Name'] == name)
        return container
