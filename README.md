# Password Manager CLI

A simple, self-hosted password manager CLI application built in Python. It stores encrypted passwords locally and provides a console-based interface for secure password management.

## Features

- Store and retrieve passwords securely
- Encrypt sensitive data with a local key file
- Simple command-line workflow for adding, viewing, and deleting entries
- Designed for personal use and quick local access

## How it works

1. The app stores credentials in `passwords.txt`.
2. A local key file `key.key` is used to encrypt/decrypt the stored data.
3. When running the app, passwords are encrypted/decrypted on demand.
4. The repository includes a minimal CLI interface in `main.py`.

## Files

- `main.py` – Main application script for interacting with passwords
- `README.md` – Project documentation
- `key.key` – Local encryption key file
- `passwords.txt` – Stored password entries

## Getting started

### Requirements

- Python 3.8 or newer

### Run the app

```bash
cd /home/gopo/git/passwordManagerCli
python3 main.py
```

### Basic usage

- Add a password entry when prompted
- View saved passwords from the CLI
- Delete or update entries using the app menu

## Notes

- Keep `key.key` secure; it is required to decrypt stored passwords.
- This project is intended for local, personal use only.
- Do not store production secrets in plain text without additional security controls.

