from django.urls import path
from hello import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

# Key-based dictionary defining all application endpoints
ENDPOINTS = {
    "home": {
        "name": "home",
        "path": "",
        "description": "Home landing view",
        "view": views.home,
    },
    "getAllLogs": {
        "name": "getAllLogs",
        "path": "getAllLogs",
        "description": "Retrieve all system log entries",
        "view": views.getAllLogs,
    },
    "getAllPersons": {
        "name": "getAllPersons",
        "path": "getAllPersons",
        "description": "Retrieve all person records",
        "view": views.getAllPersons,
    },
    "getAllContactForms": {
        "name": "getAllContactForms",
        "path": "getAllContactForms",
        "description": "Retrieve submitted contact form records",
        "view": views.getAllContactForms,
    },
    "train_tictactoe_model": {
        "name": "train_tictactoe_model",
        "path": "train_tictactoe_model",
        "description": "Trigger training for the Tic-Tac-Toe ML model",
        "view": views.train_tictactoe_model,
    },
    "download_tictactoe_model": {
        "name": "download_tictactoe_model",
        "path": "download_tictactoe_model",
        "description": "Download trained Tic-Tac-Toe model artifacts",
        "view": views.download_tictactoe_model,
    },
    "predict": {
        "name": "predict_apollo_time",
        "path": "predict/",
        "description": "Predict Apollo execution time",
        "view": views.predict_apollo_time,
    },
    "health": {
        "name": "health/",
        "path": "health/",
        "description": "System health status and endpoint discovery",
        "view": views.health,
    },
    "getAppVersion": {
        "name": "getAppVersion",
        "path": "getAppVersion",
        "description": "Get current application version",
        "view": views.getAppVersion,
    },
    "getPythonVersion": {
        "name": "getPythonWebServerVersion",
        "path": "getPythonVersion",
        "description": "Get installed Python version",
        "view": views.getPythonVersion,
    },
    "getPythonWebServerVersion": {
        "name": "getPythonVersion",
        "path": "getPythonWebServerVersion",
        "description": "Get web server Python runtime version",
        "view": views.getPythonWebServerVersion,
    },
    "ping": {
        "name": "ping",
        "path": "ping",
        "description": "Simple ping response check",
        "view": views.ping,
    },
    "schema": {
        "name": "schema",
        "path": "api/schema/",
        "description": "OpenAPI schema generator endpoint",
        "view": SpectacularAPIView.as_view(),
    },
    "swagger-ui": {
        "name": "swagger-ui",
        "path": "api/docs/",
        "description": "Swagger UI API documentation interface",
        "view": SpectacularSwaggerView.as_view(url_name="schema"),
    },
    "redoc": {
        "name": "redoc",
        "path": "api/redoc/",
        "description": "ReDoc API documentation interface",
        "view": SpectacularRedocView.as_view(url_name="schema"),
    },
}

# Dynamically construct Django URL patterns from the ENDPOINTS dictionary
urlpatterns = [
    path(data["path"], data["view"], name=data["name"])
    for data in ENDPOINTS.values()
]