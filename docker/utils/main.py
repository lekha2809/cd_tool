from dockerservices import DockerInterface

docker_service = DockerInterface()
docker_info = docker_service.pull_image("lekha2809/telegram", tag='latest')

print(docker_info)

docker_service.close_connection()