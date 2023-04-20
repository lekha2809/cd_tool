import docker
#import os

class DockerInterface:
    def __init__(self):
        self.cli = docker.DockerClient(base_url='tcp://10.10.24.97:2377')

    def get_docker_info(self):
        result = self.cli.info()
        return result

    # def get_node_number(self):
    #     result = self.cli.info()

    #     system_status = result['SystemStatus']
    #     for row in system_status:
    #         if row[0] == 