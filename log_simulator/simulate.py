import asyncio
import httpx
import logging
from generator import generate_log
from const import API_URL

logging.basicConfig(level=logging.INFO)

async def send_log():
    async with httpx.AsyncClient() as client:
        log_data = generate_log()
        try:
            response = await client.post(API_URL, json=log_data)
            logging.info(f"[{log_data['level']}] {log_data['service_name']}: {log_data['message'][:50]}... → {response.status_code}")
        except httpx.RequestError as e:
            logging.error(f"Failed to send log: {e}")

async def simulate_logs(count: int = 10, delay: float = 0.5):
    """
    Simulates sending `count` log entries with a delay between them.
    """
    for _ in range(count):
        await send_log()
        await asyncio.sleep(delay)

if __name__ == "__main__":
    asyncio.run(simulate_logs(count=10, delay=0.5))
