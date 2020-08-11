FROM amazoncorretto:11-al2-full
COPY target/eureka-discovery-0.0.1-SNAPSHOT.jar eureka-discovery.jar
ENTRYPOINT ["java","-jar","eureka-discovery.jar"]