# Task Manager
A simple task manager, powered by Django + HTMX + Alpine.js.

## Prerequisites
- Unix-like OS (Linux, MacOS, *BSD)
- Python 3.13
- MySQL driver libraries
- Podman or Docker

## Local Development Setup
1. Create and activate virtual environment:
    ```console
    python3 -m venv .venv
    source ./.venv/bin/activate
    ```
2. Install Python dependencies:
    ```console
    python3 -m pip install -r requirements.txt
    ```
3. Configure environment variables:
    ```env
    DJANGO_DEBUG=1
    DJANGO_SECRET="<secret>"
    MYSQL_DATABASE="task_manager"
    MYSQL_HOST="127.0.0.1"
    MYSQL_ROOT_PASSWORD="<password>"
    ```
4. Start MySQL in a container:
    ```console
    podman-compose up mysql
    ```
5. Run database migrations:
    ```console
    ./manage.py migrate
    ```
6. Create a (super)user account:
    ```console
    ./manage.py createsuperuser
    ```
7. Start development server:
    ```console
    ./manage.py runserver
    ```

## Running the App in Containers
1. Configure environment variables:
    ```env
    DJANGO_DEBUG=0
    DJANGO_SECRET="<secret>"
    MYSQL_DATABASE="task_manager"
    MYSQL_HOST="mysql"
    MYSQL_ROOT_PASSWORD="<password>"
    ```
2. Launch all services:
    ```console
    podman-compose up
    ```
