from qdrant_client import QdrantClient
from app.core.config import settings
import redis


qdrant_client = QdrantClient(
    url=settings.QDRANT_DB_URL,
    api_key=settings.QDRANT_API_KEY
)

r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,
    username=settings.REDIS_USERNAME,
    password=settings.REDIS_PASSWORD
)




