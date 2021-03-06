if __name__ == '__main__':
    import os
    import socket

    image_name = "eureka-server"
    docker_tag = f"{socket.gethostbyname('alaitp-cloud')}:5555/{image_name}"
    os.system("mvn clean")
    os.system("mvn package")
    os.system(f"docker build --tag={image_name} --force-rm=true .")
    os.system(f"docker tag {image_name} {docker_tag}")
    os.system(f"docker push {docker_tag}")
