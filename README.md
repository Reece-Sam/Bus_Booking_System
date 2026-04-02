# Bus_Booking_System
  ## Description
- A Flask-based Bus Booking System that allows users to view available departure times, and cancel bookings within a specified time window.
  
  ## Features
- Users can book, can be created 
- Agencies can be created,updated,get a particular agency and departure time
- Cancel booking (within 3 hours rule)
- RESTful API design
  
  ## Tech Stack
- Python
- Flask
- PostgreSQL
- SQLAlchemy

 ## Installation
 1. Clone the repo:
git clone https://github.com/your-username/bus-booking-system.git
cd bus-booking-system
 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
 3. Install dependecies
pip install -r requirements.txt

 4. Set up database:
    - Create a PostgreSQL database
    - Update your connection string
 5. Run the app:
    - python3 app.py
 6.  API Endpoints (for your case ) 
## API Endpoints

### Create User
POST /users

### Get Users
GET /users

### Book a Trip
POST /bookings

### Cancel Booking
PATCH /bookings/<id>/cancel

 7.  Business Logic
   ## Business Rules
- Users can book and also cancel bookings only if it's at least 3 hours before departure.
  
 8. Project Structure
   ## Project Structure
.
├── app.py
├── models.py
├── routes/
├── extensions.py
└── requirements.txt

  
