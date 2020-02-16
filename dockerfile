FROM openjdk:11
COPY target/eureka-discovery-0.0.1-SNAPSHOT.jar eureka-discovery.jar
ENTRYPOINT ["java","-jar","eureka-discovery.jar"]