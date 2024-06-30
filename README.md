# passwordGenerator v1.0

<p align="center">
  <img src="https://github.com/D1se0/passwordGenerator/assets/164921056/65de4e4f-4db1-40e7-9095-a406db50b6e3" alt="Directorybrute" width="400">
</p>

## Description

`passwordGenerator` is a command line tool for generating strong passwords with encryption options and estimated time to crack them. This tool is designed to be easy to use and highly configurable to meet various security needs.

## Characteristics

- Generation of secure passwords with configurable length.
- Optional inclusion of special characters.
- Password encryption in multiple formats: `SHA1`, `SHA256`, `SHA512`, `MD5`, `UNIX` (shadow) and `MySQL`.
- Calculation of the estimated time to crack the password.
- Export of results to a text file.

## Requirements

- `Python 3`
- Python packages: `argparse`, `passlib`, `colorama`

## Facility

Run the following script `requirements.sh` to install all requirements and copy the script to `/usr/bin`:

```bash
chmod +x requirements.sh
```

```bash
./requirements.sh
```

## Use

### `-h` or `--help` to view the tool information:

```bash
python3 passwordGenerator.py -h
```

Info:

`-h`, `--help` = show this help message and exit

`-l` [LENGTH], `--length` [LENGTH] = Password length (default: 8)

`-s`, `--special` = Include special characters

`-f` FILE, `--file` FILE = Export password to a text file

`-e` {sha1,sha256,sha512,md5,unix_passwd,mysql,shadow}, `--encode` {sha1,sha256,sha512,md5,unix_passwd,mysql,shadow} = Encoding/hash type for password

`-c`, `--time-crack` = Show estimated time to crack password

After installation, you can run the script from anywhere with the passwordGenerator command.

### Command Examples

Generate a 32-character password:

```bash
python3 passwordGenerator.py -l 32
```

Generate a 16-character password including special characters:

```bash
python3 passwordGenerator.py -l 16 -s
```

Generate a 12-character password and display the estimated time to crack it:

```bash
python3 passwordGenerator.py -l 12 -c
```

Generate a 20 character password and encode it in SHA256:

```bash
python3 passwordGenerator.py -l 20 -e sha256
```

### Generate a 24-character password, encode it in UNIX (shadow) and display the estimated time to crack it:

```bash
python3 passwordGenerator.py -l 24 -e unix_passwd -c
```

### Generate a 20-character password and export the results to a text file:

```bash
python3 passwordGenerator.py -l 20 -f resultados.txt
```

## Contribution

### If you wish to contribute to this project, please follow the following steps:

Fork the repository.

Create a new branch (`git checkout -b feature/new-feature`).

Make your changes and commit (`git commit -am 'Add new functionality'`).

Push to the branch (`git push origin feature/new-feature`).

Create a new `Pull Request`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

`passwordGenerator` v1.0 was developed by Diseo (@d1se0).
