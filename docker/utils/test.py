import docker
import re
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

filters = {
    #'id': '15e13cc9252b',
    'name': 'hihi-rundeck'

}

# auth_config = {
#             'username': 'lekha2809',
#             'password': 'emdixaqua1'
#        }
containers = client.containers.list(filters = filters)
for container in containers:
    dict = ((container.attrs['NetworkSettings']))
    private_port = list(dict['Ports'].keys())[0]
    print(private_port.split("/")[0])
client.close()