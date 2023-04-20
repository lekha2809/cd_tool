import logging
from docker import DockerClient
from docker.errors import APIError, NotFound

class DockerInterface:
    def __init__(self):
        self.cli = DockerClient(base_url='unix://var/run/docker.sock')

        self.auth_config = {
            'username': 'lekha2809',
            'password': 'emdixaqua1'
        }


    def get_docker_info(self):
        result = self.cli.info()
        return result

    def get_node_number(self):
        result = self.cli.info()

        system_status = result['Swarm']
        for row in system_status:
            if row == 'Nodes':
                number = int(system_status[row])
                return number
        return None
    
    def get_list_container(self, filters):
        return self.cli.containers.list(filters=filters)
    
    def pull_image(self, repository, tag):
        result = self.cli.images.pull(repository=repository, tag = tag, auth_config = self.auth_config)
        return result

    def delete_image(self, image, force= False):
        return self.cli.images.remove(image = image, force = True)
    
    def get_private_port_container_for_service(self, service_name):

        try:
            result = self.cli.containers.get(container_id = service_name)
        except (NotFound, APIError) as ex:
            logging.warning(ex)

            


    def close_connection(self):
        try:
            self.cli.close()
        except APIError as ex:
            logging.warning(ex)
