# Stage 1: Build the application using Maven
FROM maven:3-amazoncorretto-17 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the pom.xml and download dependencies
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy the source code
COPY src ./src

# Package the application (skip tests for faster builds; remove -DskipTests to include tests)
RUN mvn clean package -DskipTests



# Stage 2: Create the runtime image
FROM openjdk:17-jdk-alpine

# Set the working directory
WORKDIR /application

# Copy the jar file from the builder stage
COPY --from=builder /app/target/transfer-service-0.0.1-SNAPSHOT.jar app.jar

# Expose the port your application runs on (default is 8080 for Spring Boot)
EXPOSE 8080

# Define the entry point to run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
