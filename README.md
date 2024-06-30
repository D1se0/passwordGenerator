<h2 align="center">
  passwordGenerator v1.0
</h2>

<p align="center">
  <img src="https://github.com/D1se0/passwordGenerator/assets/164921056/65de4e4f-4db1-40e7-9095-a406db50b6e3" alt="Directorybrute" width="400">
</p>

## Descripción

`passwordGenerator` es una herramienta de línea de comandos para generar contraseñas seguras con opciones de codificación y cálculo de tiempo estimado para crackearlas. Esta herramienta está diseñada para ser fácil de usar y altamente configurable para satisfacer diversas necesidades de seguridad.

## Características

- Generación de contraseñas seguras con longitud configurable.
- Inclusión opcional de caracteres especiales.
- Codificación de contraseñas en múltiples formatos: `SHA1`, `SHA256`, `SHA512`, `MD5`, `UNIX` (shadow) y `MySQL`.
- Cálculo del tiempo estimado para crackear la contraseña.
- Exportación de resultados a un archivo de texto.

## Requisitos

- `Python 3`
- Paquetes de Python: `argparse`, `passlib`, `colorama`

## Instalación

Ejecuta el siguiente script `requirements.sh` para instalar todos los requisitos y copiar el script a `/usr/bin`:

```bash
chmod +x requirements.sh
```

```bash
./requirements.sh
```

## Uso

### `-h` o `--help` para ver la informacion de la herramienta:

```bash
python3 passwordGenerator.py -h
```

Info:

`-h`, `--help` = show this help message and exit

`-l` [LENGTH], `--length` [LENGTH] = Longitud de la contraseña (default: 8)

`-s`, `--special` = Incluir caracteres especiales

`-f` FILE, `--file` FILE = Exportar la contraseña a un archivo de texto

`-e` {sha1,sha256,sha512,md5,unix_passwd,mysql,shadow}, `--encode` {sha1,sha256,sha512,md5,unix_passwd,mysql,shadow} = Tipo de codificación/hash para la contraseña

`-c`, `--time-crack` = Mostrar tiempo estimado para crackear la contraseña

Después de la instalación, puedes ejecutar el script desde cualquier lugar con el comando passwordGenerator.

### Ejemplos de Comandos

Generar una contraseña de 32 caracteres:

```bash
python3 passwordGenerator.py -l 32
```

Generar una contraseña de 16 caracteres incluyendo caracteres especiales:

```bash
python3 passwordGenerator.py -l 16 -s
```

Generar una contraseña de 12 caracteres y mostrar el tiempo estimado para crackearla:

```bash
python3 passwordGenerator.py -l 12 -c
```

Generar una contraseña de 20 caracteres y codificarla en SHA256:

```bash
python3 passwordGenerator.py -l 20 -e sha256
```

### Generar una contraseña de 24 caracteres, codificarla en UNIX (shadow) y mostrar el tiempo estimado para crackearla:

```bash
python3 passwordGenerator.py -l 24 -e unix_passwd -c
```

### Generar una contraseña de 20 caracteres y exportar los resultados a un archivo de texto:

```bash
python3 passwordGenerator.py -l 20 -f resultados.txt
```

## Contribución

### Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

Haz un fork del repositorio.

Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).

Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).

Haz push a la rama (`git push origin feature/nueva-funcionalidad`).

Crea un nuevo `Pull Request`.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Autor

`passwordGenerator` v1.0 fue desarrollado por Diseo (@d1se0).
