API_URL = "http://localhost:8000/logs/"

LEVELS = ["DEBUG", "INFO", "WARN", "ERROR"]
SERVICES = ["auth-service", "order-service", "payment-service"]
MESSAGES = [
    "User logged in",
    "Invalid token provided",
    "Payment processed successfully",
    "Database timeout error",
    "User not found",
    "External API failed"
]
_POD_COUNT = 3
