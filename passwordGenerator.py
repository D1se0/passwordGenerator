#!/usr/bin/python3

import argparse
import random
import string
import hashlib
from passlib.hash import sha512_crypt, mysql41, sha256_crypt
from colorama import init, Fore, Style

# Inicializar colorama
init()

# Logo en ASCII con colores
LOGO = f"""
{Fore.MAGENTA}  ____                        _  ____                                      
{Fore.GREEN} |  _ \\  __ _ ___  ___       | |/ ___|  __ _ _ __ ___   __ _ _ __ _   _ ___ 
{Fore.YELLOW} | | | |/ _` / __|/ _ \\  _   | | |  _  / _` | '_ ` _ \\ / _` | '__| | | / __|
{Fore.CYAN} | |_| | (_| \\__ \\  __/ | |__| | |_| | (_| | | | | | | (_| | |  | |_| \\__ \\
{Fore.RESET} |____/ \\__,_|___/\\___|  \\____/ \\____|\\__,_|_| |_| |_|\\__,_|_|   \\__,_|___/
{Fore.CYAN}passwordGenerator v1.0{Fore.RESET}
{Fore.CYAN}by Diseo (@d1se0){Fore.RESET}
"""

def generate_password(length, use_special_chars):
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def hash_password(password, hash_type):
    if hash_type == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif hash_type == 'sha512':
        return hashlib.sha512(password.encode()).hexdigest()
    elif hash_type == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == 'unix_passwd':
        return sha512_crypt.hash(password)
    elif hash_type == 'mysql':
        return mysql41.hash(password)
    elif hash_type == 'shadow':
        return sha256_crypt.hash(password)
    else:
        raise ValueError('Opción de hash no válida')

def calculate_crack_time(password):
    # Supongamos que un hacker puede probar 10 mil millones de combinaciones por segundo
    attempts_per_second = 10_000_000_000

    # Calcular la cantidad de combinaciones posibles
    password_length = len(password)
    possible_combinations = 94 ** password_length  # 94 caracteres ASCII imprimibles

    # Calcular el tiempo estimado en segundos
    seconds = possible_combinations / attempts_per_second

    # Convertir segundos a días, horas, minutos y segundos
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return f'{int(days)} días, {int(hours)} horas, {int(minutes)} minutos, {int(seconds)} segundos'

def save_to_file(file_path, password, hash_type, crack_time):
    hashed_password = hash_password(password, hash_type)

    with open(file_path, 'w') as file:
        file.write(LOGO.strip() + '\n\n')
        file.write(f'Contraseña Generada:\n{password}\n')
        file.write(f'Contraseña codificada ({hash_type.upper()}):\n{hashed_password}\n')
        if crack_time:
            file.write(f'\nTiempo estimado para crackear la contraseña:\n{crack_time}\n')

def main():
    parser = argparse.ArgumentParser(description='Generador de Contraseñas Seguras')
    parser.add_argument('-l', '--length', type=int, default=8, nargs='?', const=8, help='Longitud de la contraseña (default: 8)')
    parser.add_argument('-s', '--special', action='store_true', help='Incluir caracteres especiales')
    parser.add_argument('-f', '--file', metavar='FILE', help='Exportar la contraseña a un archivo de texto')
    parser.add_argument('-e', '--encode', choices=['sha1', 'sha256', 'sha512', 'md5', 'unix_passwd', 'mysql', 'shadow'], help='Tipo de codificación/hash para la contraseña')
    parser.add_argument('-c', '--time-crack', action='store_true', help='Mostrar tiempo estimado para crackear la contraseña')

    # Parsear los argumentos de la línea de comandos
    args = parser.parse_args()

    # Si no se proporciona ningún argumento, mostrar la ayuda y salir
    if not any(vars(args).values()):
        parser.print_help()
        return

    # Mostrar logo
    print(LOGO.strip(), '\n')

    # Generar contraseña
    password = generate_password(args.length, args.special)
    print(f'{Fore.GREEN}Contraseña Generada: {Style.RESET_ALL}{Fore.YELLOW}{password}{Style.RESET_ALL}\n')

    # Mostrar contraseña codificada si se especifica el parámetro -e
    if args.encode:
        hashed_password = hash_password(password, args.encode)
        print(f'{Fore.GREEN}Contraseña codificada ({args.encode.upper()}): {Style.RESET_ALL}{Fore.YELLOW}{hashed_password}{Style.RESET_ALL}\n')

    # Mostrar tiempo estimado para crackear si se especifica el parámetro -c
    if args.time_crack:
        crack_time = calculate_crack_time(password)
        print(f'{Fore.GREEN}Tiempo estimado para crackear la contraseña: {Style.RESET_ALL}{Fore.CYAN}{crack_time}{Style.RESET_ALL}\n')

    # Guardar en archivo si se especifica
    if args.file:
        save_to_file(args.file, password, args.encode or 'sha256', crack_time if args.time_crack else None)
        print(f'{Fore.GREEN}Contraseña guardada en el archivo: {Style.RESET_ALL}{Fore.CYAN}{args.file}{Style.RESET_ALL}\n')

if __name__ == '__main__':
    main()
