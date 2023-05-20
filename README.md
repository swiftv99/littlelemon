# Simple project in Django REST Framework

## Available Endpoints

### InventoryAPI Endpoints
- /categories/<int:pk>/
- /products/<int:pk>/

### UserAPI Endpoints
- /users/<int:pk>/

### Authentication Endpoints
- /auth/register/
- /auth/change-password/
- /auth/login/
- /auth/login/refresh/
- /auth/login/verify/

<hr>

## Command to run all test and make report in html format
- coverage run manage.py test && coverage report && coverage html