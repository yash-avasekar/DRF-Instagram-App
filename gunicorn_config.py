import multiprocessing

# Gunicorn configuration
bind = "0.0.0.0:8000"  # Bind to localhost on port 8000
workers = 4  # Adjust the number of workers as needed
timeout = 30  # Adjust the timeout value as needed

command = "/home/yash/Desktop/InstagramApp/.venv/bin/gunicorn"
# Django specific settings
pythonpath = "/home/yash/Desktop/InstagramApp/Instagram"  # Replace with the path to your Django project directory
# You can specify the Django WSGI application using the format: module_name:application_variable_name
# For example, if your WSGI application is defined in 'wsgi.py' as 'application', use: Instagram.wsgi:application
# Replace 'Instagram' with your actual Django project name
# Replace 'application' with the variable name that holds the WSGI application
# By default, it's 'application' in 'wsgi.py'
# Example:
# app = "Instagram.wsgi:application"
# or
# app = "Instagram.asgi:application"  # For ASGI applications
app = (
    "Instagram.wsgi:application"  # Replace with your Django project's WSGI application
)
