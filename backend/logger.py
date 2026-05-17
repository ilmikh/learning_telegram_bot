import logging


logger = logging.basicConfig(
    level=logging.INFO,
    format="%(acstime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)