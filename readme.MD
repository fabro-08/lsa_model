# Configuración del Entorno

Este proyecto contiene un script de configuración de entorno ubicado en la carpeta `env/`. El script `install_env.sh` se encarga de leer el archivo `config.yaml`, eliminar y reinstalar el entorno de Python utilizando `requirements.txt`, y registrar las versiones de los paquetes en la carpeta `freeze_req/`.

## Estructura del Proyecto

```
├── 01_lsa_model.ipynb     # Contiene los traductores
├── env
│   ├── config.yaml        # Contiene el nombre del ambiente y la versión de Python.
│   ├── freeze_req/        # Carpeta donde se guarda el listado de paquetes instalados.
│   │   └── req.txt        # Archivo con la lista de paquetes congelados.
│   ├── install_env.sh     # Script que configura el entorno de Python.
│   └── requirements.txt   # Lista de dependencias necesarias para el entorno.
└── readme.MD              # Este archivo con instrucciones.
```

## Requisitos Previos

Antes de ejecutar el script, asegúrese de tener instalado:
- **Python** (La versión especificada en `config.yaml`)
- **Bash** (para macOS y Linux)
- **Git Bash o WSL** (para Windows si no se usa PowerShell)

## Instalación del Entorno

### En macOS y Linux
1. Abrir una terminal.
2. Navegar a la carpeta del proyecto:
   ```sh
   cd path/to/project/env/
   ```
3. Asignar permisos de ejecución (si es necesario):
   ```sh
   chmod +x install_env.sh
   ```
4. Ejecutar el script:
   ```sh
   ./install_env.sh
   ```

### En Windows
#### Opción 1: Usando Git Bash
1. Abrir **Git Bash**.
2. Navegar a la carpeta del proyecto:
   ```sh
   cd path/to/project/env/
   ```
3. Ejecutar el script:
   ```sh
   bash install_env.sh
   ```

#### Opción 2: Usando WSL
1. Abrir **Windows Subsystem for Linux (WSL)**.
2. Navegar a la carpeta del proyecto:
   ```sh
   cd /mnt/c/path/to/project/env/
   ```
3. Ejecutar el script:
   ```sh
   ./install_env.sh
   ```

#### Opción 3: Usando PowerShell
1. Instalar **Windows Subsystem for Linux (WSL)** si no está instalado.
2. Ejecutar el script dentro de WSL desde PowerShell:
   ```powershell
   wsl bash install_env.sh
   ```

## Verificación de Dependencias
Para comprobar que las dependencias instaladas coinciden con las versiones esperadas, se genera un archivo en la carpeta `freeze_req/`. Puede verificarlo ejecutando:
```sh
cat freeze_req/req.txt
```

Si hay diferencias, puede compararlas con:
```sh
diff requirements.txt freeze_req/req.txt
```

## Descarga del Modelo LSA
El archivo `01_lsa_model.ipynb` contiene los traductores necesarios para el procesamiento. Asegúrese de descargar y ejecutar este notebook para acceder a su funcionalidad completa.

### Dependencias de Modelos en `01_lsa_model.ipynb`
El notebook `01_lsa_model.ipynb` hace uso de **Ollama**, por lo que es necesario tenerlo instalado para poder ejecutar los siguientes modelos:
- **llama3.2**
- **deepseek-r1:32b**
- **phi4**

Para instalar Ollama, siga las instrucciones en [https://ollama.ai](https://ollama.ai) y asegúrese de que los modelos mencionados están disponibles en su entorno.

---
Este `README.md` proporciona instrucciones claras sobre cómo ejecutar `install_env.sh` en diferentes sistemas operativos y cómo utilizar el modelo LSA. Si tiene preguntas, consulte la documentación de su sistema o abra un issue en el repositorio.

