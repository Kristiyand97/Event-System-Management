![image](https://github.com/user-attachments/assets/d79aa391-d230-4451-8742-ca36101cb676)





# Event Management System

## Overview

The Event Management System is a web application built with Django that allows users to create, manage, and participate in events. This project demonstrates proficiency in Django's features, including user authentication, payment processing, media handling, and third-party integrations. The application is designed to provide a seamless experience for both event organizers and participants.

## Features

### User Authentication & Authorization
- **Registration & Email Confirmation**: Users must register and confirm their email address before accessing their profile.
- **Profile Management**: Logged-in users can edit their profile, view their created events, and see the status (Pending, Approved, or Rejected) of each event.
- **Password Reset**: Users can reset their password. This feature is available for both logged-in and non-logged-in users.

### Event Management
- **Event Creation**: Users can create events, which are submitted for admin approval. Events can have one of three statuses: Pending, Approved, or Rejected.
- **Event Approval System**: Admins can approve or reject events. Approved events are visible to everyone, while rejected events are only visible to the event creator in their profile.
- **Homepage Countdown**: The homepage displays the 3 most upcoming approved events, each with a countdown timer.

### Ticket Management
- **Ticket Purchase**: Logged-in users can purchase tickets for events using Stripe for payment processing. After purchasing, a QR code is generated for each ticket.
- **QR Code Generation**: Each purchased ticket generates a QR code, which can be viewed in the user’s profile under the "Purchased Tickets" section.

### Admin Features
- **Event Approval/ Rejection**: Admins have the ability to approve or reject events created by users, ensuring that only suitable events are listed on the platform.
  
## Technologies Used

### Core Frameworks and Libraries
- **Django**: The web framework used for developing the application.
- **Django-Allauth**: Used for handling user authentication, including registration and email verification.
- **Django Rest Framework**: Used for building API endpoints.

### Payment Processing
- **Stripe**: Integrated for secure payment processing during ticket purchases.

### Media and QR Code Handling
- **Pillow**: Used for image processing.
- **QRCode**: Used to generate QR codes for tickets.

### Other Libraries
- **asgiref**
- **certifi**
- **charset-normalizer**
- **colorama**
- **django-email-users**
- **idna**
- **pypng**
- **requests**
- **sqlparse**
- **typing_extensions**
- **tzdata**
- **urllib3**

## Getting Started

### Prerequisites
- Python 3.10+
- Django 5.0.6

### Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/event-management-system.git
    cd event-management-system
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`

## Usage

### User Actions
- **Register**: Sign up and confirm your email to access your profile.
- **Create Events**: Organize events and submit them for approval.
- **View Events**: Browse approved events on the homepage and purchase tickets.
- **Manage Profile**: Update personal information and view event statuses in the profile.

### Admin Actions
- **Approve/Reject Events**: Review user-submitted events and determine their visibility on the platform.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the project.
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
