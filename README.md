## Flask Application for CRUD operations on MongoDB

Developed a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The app is containerized using Docker and designed for scalability and clarity.

#### Features:
- REST API via Flask
- MongoDB integration via mongoengine
- Password hashing using bcrypt
- Dockerized for deployment
- Clean and scalable system design

#### Setup
  ```bash
git clone https://github.com/your-username/flask-crud-api.git
cd flask-crud-api
docker-compose up --build
```
API will be live at: http://localhost:5000/

To test all the endpoints, use POSTMAN.

#### API Endpoints:
- GET /users - Returns a list of all users.
- GET /users/<id> - Returns the user with the specified ID.
- POST /users - Creates a new user with the specified data.
- PUT /users/<id> - Updates the user with the specified ID with the new data.
- DELETE /users/<id> - Deletes the user with the specified ID.

**Note** : User id is MongoDB generated _id.

#### Tech Stack:
- Flask
- MongoEngine
- bcrypt

  #### Testing:
  - Postman
