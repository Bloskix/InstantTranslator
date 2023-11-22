# InstantTranslator

InstantTranslator es un programa que permite a dos usuarios de diferentes idiomas comunicarse de manera sencilla a través de un servidor. El programa traduce automáticamente los mensajes entre los idiomas de los usuarios, permitiendo una comunicación fluida y sin barreras de idioma.

## Estructura del Proyecto

El proyecto se divide en varios archivos:

- `client.py`: Este archivo contiene la lógica para el cliente, que se conecta al servidor y envía y recibe mensajes.
- `server.py`: Este archivo contiene la lógica para el servidor, que acepta conexiones de los clientes y retransmite los mensajes entre ellos.
- `translator.py`: Este archivo contiene la lógica para traducir los mensajes entre diferentes idiomas.
- `constants.py`: Este archivo define varias constantes y funciones de utilidad que se utilizan en todo el proyecto.
- `main.py`: Este es el punto de entrada del programa. Aquí se recogen los detalles del usuario y se inicia el cliente o el servidor según sea necesario.

## Cómo usar

Para usar InstantTranslator, sigue estos pasos:

1. Ejecuta `main.py`.
2. Se te pedirá que introduzcas tu idioma (es/en/fr/de).
3. A continuación, se te pedirá que introduzcas tu nombre de usuario.
4. A continuación, se te presentará un menú con varias opciones. Puedes elegir crear una sala de chat, unirte a una sala de chat existente, cambiar tu idioma o salir del programa.