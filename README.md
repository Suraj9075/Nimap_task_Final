🧩 Client & Project Management API
A Django REST Framework project to manage Clients and their Projects, with support for assigning existing Users to Projects.

This API allows you to:
Register and manage Clients
Create and assign Projects under Clients
Assign multiple existing Users to a Project
Retrieve all Projects assigned to a specific user (simulated)
Automatically track who created what and when
Work without actual authentication (uses default users like 'Rohit', 'Ganesh' internally)

🚀 Features
✅ CRUD operations on Clients
✅ Create Projects under a Client with user assignments
✅ List Projects assigned to a specific user
✅ Simulated user tracking (created_by) without login/authentication
✅ Fully JSON-based API for frontend integration or Postman testing

🛠️ Tech Stack
Backend: Django, Django REST Framework
Database: SQLite (easily switchable to PostgreSQL/MySQL)
Language: Python 3.11+

📁 Endpoints Overview
📦 Client APIs
Method	Endpoint	Description
GET	/api/clients/	List all clients
POST	/api/clients/	Create a new client
GET	/api/clients/<id>/	Retrieve single client info with its projects
PUT/PATCH	/api/clients/<id>/	Update client
DELETE	/api/clients/<id>/	Delete client
POST	/api/clients/<id>/projects/	Create a project under a client with users

📂 Project APIs
Method	Endpoint	Description
GET	/api/projects/	List all projects assigned to a simulated user (e.g., Ganesh)

🔍 Sample API Requests & Responses
✅ Create Client
POST /api/clients/

Request:

json
Copy
Edit
{
  "client_name": "Birla"
}
Response:

json
Copy
Edit
{
  "id": 7,
  "client_name": "Birla",
  "created_at": "2025-07-15T09:23:24.235490Z",
  "created_by": "Rohit"
}
📄 List All Clients
GET /api/clients/

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "client_name": "Nimap",
    "created_at": "...",
    "created_by": "Rohit"
  }
]
🔎 Get Client with Projects
GET /api/clients/2/

Response:

json
Copy
Edit
{
  "id": 2,
  "client_name": "microsoft",
  "created_at": "...",
  "created_by": "Rohit",
  "updated_at": "...",
  "projects": [
    {
      "id": 7,
      "name": "Project A"
    }
  ]
}
✏️ Update Client
PUT /api/clients/3/

Request:

json
Copy
Edit
{
  "client_name": "changed"
}
➕ Add Project Under a Client
POST /api/clients/5/projects/

Request:

json
Copy
Edit
{
  "project_name": "Project 6",
  "users_input": [
    {
      "id": 1,
      "name": "Rohit"
    }
  ]
}
Response:

json
Copy
Edit
{
  "id": 10,
  "project_name": "Project 6",
  "client": "google",
  "users": [
    {
      "id": 1,
      "name": "Rohit"
    }
  ],
  "created_at": "...",
  "created_by": "Ganesh"
}
📋 List Projects for a User
GET /api/projects/

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "project_name": "Project A",
    "client": "Nimap",
    "users": [],
    "created_at": "...",
    "created_by": "Ganesh"
  }
]
❌ Delete Client
DELETE /api/clients/7/
Response: HTTP 204 No Content

🧪 How to Run
bash
Copy
Edit
# Clone the repository
git clone <your-repo-url>
cd project-folder

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superusers (Simulated Users: Rohit and Ganesh)
python manage.py createsuperuser  # Use Rohit
python manage.py createsuperuser  # Use Ganesh

# Start development server
python manage.py runserver
