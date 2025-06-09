import random
import uuid
from datetime import datetime, timezone
from const import LEVELS, SERVICES, MESSAGES, _POD_COUNT

def generate_log() -> dict:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": random.choice(LEVELS),
        "service_name": random.choice(SERVICES),
        "message": random.choice(MESSAGES),
        "trace_id": str(uuid.uuid4()),
        "source": f"pod-{random.randint(1, _POD_COUNT)}"
    }
