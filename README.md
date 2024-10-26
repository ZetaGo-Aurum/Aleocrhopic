
### 1. Instalasi Git dan Python

```bash
# Di Termux
pkg update && pkg upgrade
pkg install git
pkg install python

# Di Linux (Ubuntu/Debian)
sudo apt update && sudo apt upgrade
sudo apt install git
sudo apt install python3 python3-pip
```

### 2. Clone Repository

```bash
# Buat folder untuk project (opsional)
mkdir projects
cd projects

# Clone repository
git clone https://github.com/RayhanDz/Javascript-encryptor-decryptor.git

# Masuk ke direktori hasil clone
cd Javascript-encryptor-decryptor
```

### 3. Setup Environment dan Instalasi Dependencies

```bash
# Buat virtual environment (opsional tapi direkomendasikan)
python -m venv venv

# Aktifkan virtual environment
# Di Linux/Termux:
source venv/bin/activate
# Di Windows:
# venv\Scripts\activate

# Install semua dependencies yang diperlukan
pip install -r requirements.txt
```


### 4. Jalankan Script

```bash
python Javascript-encryptor-decryptor.py
```

