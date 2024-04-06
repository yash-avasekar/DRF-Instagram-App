# Instagram Lite (Social Media) App

Instagram Lite is a lightweight social media application that provides essential features for users to interact with profiles and posts. It includes functionalities such as profile following, followers, posting, liking, commenting, profile updates and deletions, with restricted permissions, pagination, throttling, and search filtering.

## Features

- User authentication and authorization using Django REST Framework's Token Authentication
- User profiles with following and followers functionality
- Posting, liking, and commenting on posts
- Profile updates and deletions
- Restricted permissions for certain actions
- Pagination for large datasets
- Throttling to limit the number of requests
- Profile search filtering
- Endpoints to view all profiles posts and interact with posts

## Technologies Used

- Python
- Django
- Django REST Framework
- Gunicorn
- Nginx

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/instagram-lite.git

1. Navigate into the project directory:
cd Instagram

1. Create a virtual environment:
python3 -m venv env

1. Activate the virtual environment:
source env/bin/activate

1. Install dependencies:
pip install -r requirements.txt

1. Run database migration
python manage.py migrate

1.Create a superuser:
python manage.py createsuperuser

python manage.py runserver
