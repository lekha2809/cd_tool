from dockerservices import DockerInterface

docker_service = DockerInterface()
docker_info = docker_service.get_docker_info()

print(docker_info)