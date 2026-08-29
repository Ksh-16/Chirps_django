# Chirps - Social Media Platform

A lightweight Twitter/X-inspired social media application built with Django. Share short text posts and photos with a clean, intuitive interface.

## 🌐 Live Demo

Visit the live application: [https://ksh16.pythonanywhere.com](https://ksh16.pythonanywhere.com)

## ✨ Features

- **User Authentication**: Secure registration and login system
- **Tweet Management**: Create, read, update, and delete tweets with ease
- **Photo Uploads**: Attach images to your tweets for richer content
- **User Profiles**: Display user information and posted content
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Clean UI**: Modern, intuitive interface with Bootstrap styling

## 🛠️ Tech Stack

- **Backend**: Django 6.0.7
- **Frontend**: Bootstrap 5.3.8, HTML5, CSS3
- **Database**: SQLite3
- **Hosting**: PythonAnywhere
- **Version Control**: Git & GitHub

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Git

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Ksh16/Chirps_django.git
cd Chirps_django
```

### 2. Create a Virtual Environment
```bash
python -m venv myworld
source myworld/bin/activate  # On Windows: myworld\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Apply Migrations
```bash
cd Chirps
python manage.py migrate
```

### 6. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```

### 8. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000/tweet/` in your browser to see the app.

## 📁 Project Structure

```
Chirps_django/
├── Chirps/                          # Project configuration folder
│   ├── settings.py                  # Django settings
│   ├── urls.py                      # URL routing
│   ├── wsgi.py                      # WSGI configuration
│   └── asgi.py                      # ASGI configuration
├── tweet/                           # Main app
│   ├── migrations/                  # Database migrations
│   ├── templates/                   # App-specific templates
│   ├── models.py                    # Database models (Tweet)
│   ├── views.py                     # View logic
│   ├── urls.py                      # App URL routing
│   ├── forms.py                     # Django forms
│   └── admin.py                     # Admin configuration
├── templates/                       # Global templates
│   ├── layout.html                  # Base template
│   ├── registration/                # Auth templates
│   └── tweet_list.html              # Tweet listing
├── static/                          # Static files (CSS, JS, images)
│   └── css/
│       └── theme.css                # Custom styling
├── media/                           # User-uploaded files
├── manage.py                        # Django CLI
├── requirements.txt                 # Project dependencies
└── db.sqlite3                       # SQLite database
```

## 💻 Usage

### Creating an Account
1. Click on "Register" link on the login page
2. Fill in username, email, and password
3. Submit to create your account

### Creating a Tweet
1. Log in to your account
2. Click "Create a tweet" button
3. Enter your text (max 240 characters) and optionally upload a photo
4. Click "Submit"

### Managing Your Tweets
- **Edit**: Click the "Edit" button on any of your tweets
- **Delete**: Click the "Delete" button to remove a tweet

## 🔐 Security Features

- Secure password hashing with Django's built-in authentication
- CSRF protection on all forms
- SQL injection prevention through Django ORM
- Secure session management
- Environment variable-based configuration for sensitive data

## 📱 Responsive Design

The application is fully responsive and optimized for:
- Desktop browsers
- Tablets
- Mobile devices

## 🚢 Deployment

### Deploying to PythonAnywhere

1. Create a PythonAnywhere account
2. Upload your project files
3. Set up a virtual environment on PythonAnywhere
4. Configure environment variables in `.env`
5. Set up the WSGI file to point to your Django app
6. Reload the web app

For detailed instructions, refer to [PythonAnywhere Documentation](https://help.pythonanywhere.com/pages/DeployingYourDjangoapplication)

## 📦 Dependencies

See `requirements.txt` for the complete list:
- Django==6.0.7
- asgiref==3.12.1
- sqlparse==0.5.5
- tzdata==2026.3

## 🐛 Known Issues & Future Enhancements

### Current Known Issues
- Dark mode text visibility (in progress)

### Planned Features
- User follow/follower system
- Like and comment functionality
- Direct messaging between users
- Tweet search functionality
- User profiles with bio and profile picture
- Trending hashtags
- Notifications system

## 👨‍💻 Author

**Kanishka Sharma**
- GitHub: [@Ksh16](https://github.com/Ksh-16)
- Project Repository: [Chirps_django](https://github.com/Ksh16/Chirps_django)



## 🙏 Acknowledgments

- Django documentation and community
- Bootstrap framework
- YouTube tutorials and learning resources
- Everyone who provided feedback and suggestions

---

**Last Updated**: August 2026  
**Current Version**: 1.0.0
