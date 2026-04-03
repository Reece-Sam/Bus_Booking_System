# Bus_Booking_System

## Description

- A Flask-based Bus Booking System that allows users to view available departure times, and cancel bookings within a specified time window.

Deployed Site: https://bus-booking-system-fawn.vercel.app/  
API Docs: https://bus-booking-system-fawn.vercel.app/apidocs/

## Features
- You create a user, get all users that has been created, you can get user by the id, update and also delete a user by id 
- Agencies can be created,updated, delete ,get a particular agency by id  and departure time
- Cancel booking (within 3 hours rule)
- RESTful API design
- Also, if you want to delete a user or agency that has already been used to book it wont delete, you have to delete the booking first.

  ## Tech Stack
- Python
- Flask
- PostgreSQL
- SQLAlchemy

## Installation
1.  Clone the repo:
    git clone https://github.com/your-username/bus-booking-system.git
    cd bus-booking-system
2.  Create virtual environment
    python3 -m venv venv
    source venv/bin/activate
3.  Install dependecies
    pip install -r requirements.txt

4.  Set up database:
    - Create a PostgreSQL database
    - Update your connection string
5.  Run the app:
    - python3 app.py
6.  API Endpoints (for your case )

## API Endpoints

### Create User
POST /users

### Get Users
GET /users

### Get Users by id 
GET /users<int:id>

### Patch update user by id
PATCH /users<int:id>

### Delete user by id
DELETE /users<int:id>

========================================

### Create agencies
POST /agencies

### Get Agencies
GET /agencies

### Get Agencies by id 
GET /agencies<int:id>

### Patch update agencies by id
PATCH /agencies<int:id>

### Delete agencies by id
DELETE /agencies<int:id>

============================================

### Create booking
POST /bookings

### Get booking
GET /bookings

### Get booking by id 
GET /users<int:id>

### Cancel Booking
PATCH /bookings/<int:id>/cancel

### Patch update booking by id
PATCH /bookings<int:id>

### Delete booking by id
DELETE /bookings<int:id>



7.  Business Logic
## Business Rules
- Users can book and also cancel bookings only if it's at least 3 hours before departure.

8.  Project Structure
## Project Structure
## Project Structure
.
├── app.py
├── models.py
├── routes/
├── extensions.py
├── docs/
│   └── Bus_system.drawio
└── requirements.txt

9. I also tested the endpoints on hoppscotch and it works fine
