##Crud Exercise: FastAPI

This repository contains a simple implementation of the FastAPI interface and CRUD methods for two independent entities: Computer and Table. The project is containerized using Docker for easy database setup and management, allowing seamless interaction with both entities.

##Computer Management
- Add, Edit, Delete and View computer records.
- Attributes include manufacturer, model, processor, memory_size, storage_capacity, operating_system and graphics_card

##Table Management 
- Add, Edit, Delete and View table records
- Attributes include brand, model, price, suppor and color

##Independence:
Computer and Table are two separate, unrelated classes.

##Technologies Used:
- FastAPI: For building RESTful APIs.
- Docker: To manage the database container.
- [Database]: Managed through Docker, used for persistent data storage.

##How to Run:

- Clone the repository.
- Build and start the Docker containers by running: `docker-compose buid` and `docker-compose up -d`

Access the API at `http://localhost:8000/docs` to interact with the CRUD operations.
The ApiKey is: 4d631589-409c-4c7f-8729-c21064c4f242

Access the Adminer at `http://localhost:8080` to interact with the data base.


