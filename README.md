
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
git clone https://github.com/ZetaGo-Aurum/Aleocrhopic.git
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


### Troubleshooting

Jika mengalami masalah saat instalasi, coba:
# Di Termux
pkg install build-essential
pkg install python-dev
pkg install openssl-dev
pkg install libffi-dev

# Di Linux (Ubuntu/Debian)
sudo apt install build-essential
sudo apt install python3-dev
sudo apt install libssl-dev
sudo apt install libffi-dev


### Perintah Git Tambahan yang Berguna

```bash
# Update repository ke versi terbaru
git pull origin main

# Lihat status perubahan
git status

# Lihat versi/commit history
git log

# Kembali ke versi tertentu
git checkout [commit-hash]
```



### Catatan Penting

1. Pastikan Anda memiliki koneksi internet yang stabil

2. Jika repository belum tersedia di GitHub, Anda perlu:

   - Membuat repository di GitHub terlebih dahulu
   
   - Push kode ke repository tersebut
   
   - Baru kemudian bisa melakukan clone

3. Untuk menghapus instalasi:
```bash
# Nonaktifkan virtual environment jika digunakan
deactivate

# Hapus folder project
cd ..
rm -rf Javascript-encryptor-decryptor
```

4. Untuk update script ke versi terbaru:
   
git pull origin main
pip install -r requirements.txt


Setelah instalasi selesai, Anda dapat menggunakan semua fitur yang tersedia dalam JavaScript Tools sesuai dengan menu yang ditampilkan.
