
OVERVIEW

# backend
## Architecture
|Layer|Purpose|File Location|
|---|---|---|
|**Routes**|Define URL endpoints|`app/api/endpoints/*.py`|
|**CRUD Logic**|Query the database|`app/crud/*.py`|
|**Models**|Define DB tables (SQLAlchemy)|`app/models/*.py`|
|**Schemas**|Define request/response formats|`app/schemas/*.py`|
|**Main App**|App setup & route registration|`app/main.py`|

# Example Endpoints
placeholder

# Setup Scripts
used for Docker deployment on a server

# terraform
IaC to deploy Google Cloud infrastructure to host the project