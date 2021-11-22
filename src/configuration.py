"""Load configuration from env."""
import os

import dotenv

dotenv.load_dotenv()

GENERATED_USER = os.getenv("GENERATED_USER")
GENERATED_PASS = os.getenv("GENERATED_PASS")
DOMAIN = os.getenv("DOMAIN")

SERVICE = os.getenv("SERVICE")
USER_AGENT = os.getenv("USER_AGENT")

NO_NET_INTERVAL = int(os.getenv("NO_NET_INTERVAL"))
NO_CHANGE_INTERVAL = int(os.getenv("NO_CHANGE_INTERVAL"))