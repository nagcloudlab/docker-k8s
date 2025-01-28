# Stage 1: Build the application
FROM maven:3-amazoncorretto-17 AS stage1
ARG WD=/app
# Set the working directory inside the container
WORKDIR ${WD}
# Copy the pom.xml and download dependencies
COPY pom.xml .
# This will download the dependencies and cache them
RUN mvn dependency:go-offline -B

# Copy the source code
COPY src/ ./src/ 

# Package the application ( .jar )
RUN mvn clean package -DskipTests


# Stage 2: Create the runtime image
FROM openjdk:17-jdk-alpine
# Set the working directory
WORKDIR /app
# Copy the JAR from the builder stage
COPY --from=stage1 /app/target/transfer-service-0.0.1-SNAPSHOT.jar app.jar
# Expose port 8080
EXPOSE 8080
# RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup
# USER appuser
# HEALTHCHECK --interval=1m --timeout=10s --start-period=30s --retries=3 \
#   CMD curl -f http://localhost:8080/actuator/health || exit 1
ENV SPRING_PROFILES_ACTIVE=dev
# Run the application
# CMD ["java", "-jar", "app.jar"]
ENTRYPOINT ["java", "-jar", "app.jar"]

