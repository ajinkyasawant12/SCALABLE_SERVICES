# Gaming Platform Microservices Architecture

This document outlines the design of a scalable microservices architecture for a gaming platform. The platform includes core functionalities such as user management, game catalog, matchmaking, and leaderboard management.

## 1. System Operations

### Commands
- RegisterUser
- UpdateUserProfile
- DeleteUser
- AddGame
- UpdateGame
- DeleteGame
- CreateMatch
- UpdateMatch
- EndMatch
- SubmitScore

### Queries
- GetUser
- GetAllUsers
- GetGame
- GetAllGames
- GetMatch
- GetAllMatches
- GetLeaderboard

## 2. Business Capabilities and Services

### Business Capabilities
- User Management
- Game Management
- Matchmaking
- Leaderboard Management

### Mapped Services
- **User Service**: Manages user-related operations.
- **Game Service**: Manages game-related operations.
- **Matchmaking Service**: Manages match creation and updates.
- **Leaderboard Service**: Manages score submissions and leaderboard queries.

## 3. Assign System Operations to Services and Collaboration

### User Service
- **Commands**: RegisterUser, UpdateUserProfile, DeleteUser
- **Queries**: GetUser, GetAllUsers

### Game Service
- **Commands**: AddGame, UpdateGame, DeleteGame
- **Queries**: GetGame, GetAllGames

### Matchmaking Service
- **Commands**: CreateMatch, UpdateMatch, EndMatch
- **Queries**: GetMatch, GetAllMatches

### Leaderboard Service
- **Commands**: SubmitScore
- **Queries**: GetLeaderboard

### Collaboration Between Services
- **Matchmaking Service** collaborates with **User Service** to validate user information when creating a match.
- **Matchmaking Service** collaborates with **Game Service** to validate game information.
- **Leaderboard Service** collaborates with **Matchmaking Service** to update scores and retrieve match results.

## 4. Architecture Diagram

```plaintext
+----------------+       +----------------+       +----------------+       +----------------+
|  User Service  |<----->|  Game Service  |<----->| Matchmaking Svc|<----->| Leaderboard Svc|
+----------------+       +----------------+       +----------------+       +----------------+
       |                        |                        |                        |
       |                        |                        |                        |
       v                        v                        v                        v
+----------------+       +----------------+       +----------------+       +----------------+
|  User Database |       |  Game Database |       | Match Database |       | Leaderboard DB |
+----------------+       +----------------+       +----------------+       +----------------+


## 5. Example of Service Collaboration

### CreateMatch Flow
1. **Matchmaking Service** receives a `CreateMatch` command.
2. **Matchmaking Service** queries **User Service** to validate the users involved in the match.
3. **Matchmaking Service** queries **Game Service** to validate the game information.
4. **Matchmaking Service** creates the match and stores it in the match database.

### SubmitScore Flow
1. **Leaderboard Service** receives a `SubmitScore` command.
2. **Leaderboard Service** queries **Matchmaking Service** to validate the match and retrieve match details.
3. **Leaderboard Service** updates the leaderboard based on the submitted score.

This design ensures that each service is responsible for a specific business capability, promoting scalability and maintainability. Each service can be independently developed, deployed, and scaled based on demand.

## 6. Commands 
Build Docker Images: 
       docker build -t user-service. 
       docker build -t matchmaking-service. 

Run Docker Containers: 

       docker run -d -p 5000:5000 --name user-service user-service 
       docker run -d -p 5001:5001 --name matchmaking-service matchmaking-service 

Start Minikube: 

       minikube start 
       eval $(minikube docker-env) 

Build Docker Images for Minikube: 

       docker build -t user-service. 
       docker build -t matchmaking-service. 

Create Kubernetes Deployment and Service YAML Files: 

       user-service-deployment.yaml 
       matchmaking-service-deployment.yaml 

Deploy to Kubernetes: 

       kubectl apply -f user-service-deployment.yaml 
       kubectl apply -f matchmaking-service-deployment.yaml 

Access Kubernetes Dashboard: 

       minikube dashboard 

Verify the Deployments: 

       Access the services using the Minikube IP and NodePort 
       http://<minikube_ip>:<node_port>/users. 
       http://<minikube_ip>:<node_port>/matches 

## 7. Additional Resources

For more group details, refer to the [Group Assignment Document](https://wilpbitspilaniacin0.sharepoint.com/:x:/r/sites/ScalableServicesS1-24_CCZG583/_layouts/15/Doc.aspx?sourcedoc=%7BB60589BB-4D2B-463F-B963-21106FF06D8F%7D&file=Group_Assignment_S1-24_CCZG583.xlsx&action=default&mobileredirect=true&DefaultItemOpen=1&ct=1728233533710&wdOrigin=OFFICECOM-WEB.START.REC&cid=8f4c3a21-0839-4193-85dd-fa44bdec06fa&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=eea4f79e-4c8d-487b-97d8-65a64a4a870d).
