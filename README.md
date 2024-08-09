# System Management System

## Overview

The System Management System is a Django-based web application designed to streamline the process of managing various events and personal information. This project currently includes features for user registration, event creation, event viewing, password management, and personal information management. As the project evolves, more features and functionalities will be added.

## Features

- **User Registration**: New users can easily sign up and create an account within the system.
- **Event Creation**: Registered users can create and manage events, with options to add details such as event name, date, and description.
- **View Events**: Users can view a list of all available events, along with detailed information about each event.
- **Password Reset**: Users who have forgotten their passwords can reset them through a secure process.
- **Personal Information Management**: Users can view and update their personal information, ensuring that their profile is always up to date.

## Getting Started

To get started with the System Management System, follow the steps below:

### Prerequisites

- Python 3.x
- Django 4.x
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/system-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd system-management-system
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

5. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser account to access the Django admin:
   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

9. Open your browser and navigate to:
   ```bash
   http://localhost:8000
   ```

### Environment Variables

Make sure to configure the necessary environment variables in your `.env` file or within your environment for settings like the database, secret key, etc. You can use a package like `django-environ` to manage this.

## Usage

### Registering a New User

- Go to the registration page at `/register/`.
- Fill in the required fields (username, email, password).
- Submit the form to create a new account.

### Creating an Event

- Log in to your account.
- Navigate to the "Create Event" page at `/events/create/`.
- Fill in the event details (name, date, description).
- Submit the form to create the event.

### Viewing Events

- Go to the "View Events" page at `/events/`.
- Browse through the list of available events.
- Click on any event to see more details.

### Resetting Password

- Go to the "Forgot Password" page at `/password-reset/`.
- Enter your registered email address.
- Follow the instructions sent to your email to reset your password.

### Managing Personal Information

- Log in to your account.
- Navigate to the "Profile" page at `/profile/`.
- Update your personal information as needed.
- Save changes.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request for review.
