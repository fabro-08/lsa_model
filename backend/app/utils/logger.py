import logging
from app.config import config
import os

def config_logger(nombre_logger='default_logger'):
    """
    Configura el logger para FastAPI y guarda los logs en `app/logs/app.log`.

    Args:
    - nombre_logger (str): El nombre del logger a configurar. Por defecto es 'default_logger'.

    Returns:
    - logger (logging.Logger): El logger configurado.
    """
    # 📌 Definir el directorio de logs
    log_dir = config.LOG_DIR  # `app/logs/`
    log_file = os.path.join(log_dir, 'app.log')

    # 📌 Crear la carpeta de logs si no existe
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 📌 Configurar el logger
    logger = logging.getLogger(nombre_logger)

    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)  # Puedes cambiar a INFO o WARNING

        # 🔹 Handler para consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # 🔹 Handler para archivo de logs
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # 📌 Formato del log
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # 📌 Agregar handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.propagate = False  # Evitar propagación a loggers ancestros

    return logger