# How to Run Django Webserver

## Getting Started
### Prerequisites
**Python** - Ensure Python 3.x is installed. You can download it from python.org.

**Django** - Install Django (or specify other libraries or versions if necessary).

### Installation
#### Clone the repository:
```bash
git clone https://github.com/kangScripter/Vspark-Django
cd Vspark-Django
```

#### Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

##### 1. Apply migrations to set up the database:
```bash
python manage.py migrate

```

##### 2. Create a superuser for the Django admin panel:
```bash
python manage.py createsuperuser
```

#### #3.Start the development server:
```bash
python manage.py runserver
```
Open http://127.0.0.1:8000 in your browser to view the application.

