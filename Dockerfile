# Utiliza la imagen base de Python 3.11 en Debian Buster
FROM python:3.11-buster

# Instala dependencias de compilación
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev libmariadbclient-dev

# Configura la zona horaria a Argentina
ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Crea el directorio de la aplicación
WORKDIR /app

# Instala la aplicación y las dependencias de Python
COPY ./requirements.txt ./
RUN python3.11 -m pip install --upgrade pip \
    && pip3.11 install -r requirements.txt

# Agrega el código fuente
COPY . .

# Instalamos el modulo custom
RUN pip3.11 install -e .

# Abre el puerto 8888 para acceder a Jupyter Notebook
EXPOSE 8888

# Comando para iniciar Jupyter Notebook
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
