import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os
import json
import re
import zlib
import random
import string
import codecs
from colorama import Fore, Back, Style, init
import jsbeautifier
import jsmin

# Inisialisasi colorama
init(autoreset=True)

class JSEncryptorDecryptor:
    def __init__(self):
        self.salt = os.urandom(16)
        
    def generate_key(self, password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    def encrypt(self, js_code, password):
        key = self.generate_key(password)
        f = Fernet(key)
        encrypted = f.encrypt(js_code.encode())
        return base64.b64encode(self.salt + encrypted).decode()
    
    def decrypt(self, encrypted_js, password=None):
        try:
            decoded = base64.b64decode(encrypted_js)
            self.salt = decoded[:16]
            encrypted = decoded[16:]
            
            if password:
                key = self.generate_key(password)
                f = Fernet(key)
                decrypted = f.decrypt(encrypted)
            else:
                decrypted = self.auto_decrypt(encrypted)
            
            return decrypted.decode()
        except Exception as e:
            return f"Gagal mendekripsi: {str(e)}"
    
    def auto_decrypt(self, encrypted):
        try:
            return base64.b64decode(encrypted)
        except:
            pass
        
        try:
            return codecs.decode(encrypted.decode(), 'rot13').encode()
        except:
            pass
        
        raise Exception("Tidak dapat mendeteksi metode enkripsi")

def print_cyber_style(text, color=Fore.GREEN):
    print(f"{color}[CYBER]{Style.RESET_ALL} {text}")

def print_fancy_border():
    print(f"{Fore.CYAN}╔{'═'*50}╗")
    print(f"║{' '*50}║")
    print(f"╚{'═'*50}╝{Style.RESET_ALL}")

def print_result(result):
    print_fancy_border()
    print(f"{Fore.GREEN}Hasil operasi:")
    print(f"{result}")
    print_fancy_border()

def show_menu():
    print_fancy_border()
    print(f"{Fore.YELLOW}╔{'═'*48}╗")
    print(f"║{' '*15}Javascript Tools{' '*15}║")
    print(f"╠{'═'*48}╣")
    print("║ 1.  Enkripsi JavaScript                        ║")
    print("║ 2.  Dekripsi JavaScript                        ║")
    print("║ 3.  Obfuskasi JavaScript                       ║")
    print("║ 4.  Deobfuskasi JavaScript                     ║")
    print("║ 5.  Minifikasi JavaScript                      ║")
    print("║ 6.  Mempercantik JavaScript                    ║")
    print("║ 7.  Kompresi JavaScript                        ║")
    print("║ 8.  Dekompresi JavaScript                      ║")
    print("║ 9.  Generate Nama Variabel Acak                ║")
    print("║ 10. Tambahkan Anti-Debugging                   ║")
    print("║ 11. Tambahkan Watermark                        ║")
    print("║ 12. Enkripsi String                            ║")
    print("║ 13. Tambahkan Kadaluarsa                       ║")
    print("║ 14. Pisahkan menjadi Chunk                     ║")
    print("║ 15. Gabungkan Chunk                            ║")
    print("║ 16. Analisis Kompleksitas                      ║")
    print("║ 17. Generate Dokumentasi                       ║")
    print("║ 18. Konversi ke Arrow Functions                ║")
    print("║ 19. Tambahkan Strict Mode                      ║")
    print("║ 20. Hapus Console.log                          ║")
    print("║ 21. Encode Unicode                             ║")
    print("║ 22. Decode Unicode                             ║")
    print("║ 23. Tambahkan Self-Destruction                 ║")
    print("║ 24. Keluar                                     ║")
    print(f"╚{'═'*48}╝{Style.RESET_ALL}")

def obfuscate_js(js_code):
    # Implementasi obfuskasi yang lebih sederhana
    obfuscated = js_code
    
    # Mengganti nama variabel dan fungsi
    variables = set(re.findall(r'\b(?:var|let|const)\s+(\w+)', obfuscated))
    functions = set(re.findall(r'\bfunction\s+(\w+)', obfuscated))
    
    for var in variables:
        new_var = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        obfuscated = re.sub(r'\b' + var + r'\b', new_var, obfuscated)
    
    for func in functions:
        new_func = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        obfuscated = re.sub(r'\b' + func + r'\b', new_func, obfuscated)
    
    # Menambahkan noise
    noise = ''.join(random.choice(string.ascii_letters) for _ in range(50))
    obfuscated = f"/* {noise} */\n" + obfuscated
    
    return obfuscated

def deobfuscate_js(obfuscated_code):
    # Implementasi deobfuskasi sederhana
    deobfuscated = obfuscated_code
    
    # Membersihkan kode
    deobfuscated = re.sub(r'/\*[\s\S]*?\*/', '', deobfuscated)  # Hapus comments
    deobfuscated = re.sub(r'^\s*\n', '', deobfuscated, flags=re.MULTILINE)  # Hapus empty lines
    
    # Mempercantik hasil akhir
    try:
        deobfuscated = jsbeautifier.beautify(deobfuscated)
    except:
        pass
            
    return deobfuscated

def minify_js(js_code):
    return jsmin.jsmin(js_code)

def beautify_js(js_code):
    return jsbeautifier.beautify(js_code)

def compress_js(js_code):
    compressed = zlib.compress(js_code.encode())
    return base64.b64encode(compressed).decode()

def decompress_js(compressed_code):
    decompressed = zlib.decompress(base64.b64decode(compressed_code))
    return decompressed.decode()

def generate_random_var_name(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def add_anti_debugging(js_code):
    anti_debug = """
    (function(){
        setInterval(function(){
            debugger;
        }, 100);
    })();
    """
    return anti_debug + "\n" + js_code

def add_watermark(js_code, watermark):
    return f"/* {watermark} */\n" + js_code

def encrypt_string(string):
    return ''.join([chr(ord(c) + 1) for c in string])

def add_expiration(js_code, expiration_date):
    expiration_code = f"""
    if (new Date() > new Date('{expiration_date}')) {{
        throw new Error('Kode ini telah kedaluwarsa');
    }}
    """
    return expiration_code + "\n" + js_code

def split_into_chunks(js_code, chunk_size=1000):
    return [js_code[i:i+chunk_size] for i in range(0, len(js_code), chunk_size)]

def join_chunks(chunks):
    return ''.join(chunks)

def analyze_complexity(js_code):
    lines = js_code.split('\n')
    functions = len(re.findall(r'\bfunction\b', js_code))
    loops = len(re.findall(r'\b(for|while)\b', js_code))
    return f"Jumlah baris: {len(lines)}\nJumlah fungsi: {functions}\nJumlah loop: {loops}"

def generate_documentation(js_code):
    functions = re.findall(r'function\s+(\w+)\s*\((.*?)\)', js_code)
    doc = "Dokumentasi:\n\n"
    for func, params in functions:
        doc += f"Fungsi: {func}\nParameter: {params}\n\n"
    return doc

def convert_to_arrow_functions(js_code):
    # Implementasi sederhana konversi ke arrow functions
    return js_code.replace("function", "=>")

def add_strict_mode(js_code):
    return '"use strict";\n' + js_code

def remove_console_log(js_code):
    return re.sub(r'console\.log\(.*?\);', '', js_code)

def encode_unicode(js_code):
    return ''.join(f'\\u{ord(c):04x}' for c in js_code)

def decode_unicode(encoded_js):
    return encoded_js.encode('utf-8').decode('unicode_escape')

def add_self_destruction(js_code):
    self_destruct = """
    (function(){
        setTimeout(function(){
            var script = document.currentScript;
            if(script) script.parentNode.removeChild(script);
        }, 10000);
    })();
    """
    return self_destruct + "\n" + js_code

def main():
    encryptor = JSEncryptorDecryptor()
    
    print_cyber_style("Selamat datang di Javascript Tools", Fore.CYAN)
    print_cyber_style("Dibuat oleh: Rayhan Dzaky Al Mubarok", Fore.MAGENTA)
    
    while True:
        show_menu()
        choice = input(f"{Fore.YELLOW}Masukkan pilihan (1-24): {Style.RESET_ALL}")
        
        if choice == '1':
            js_code = input("Masukkan kode JavaScript yang akan dienkripsi: ")
            password = input("Masukkan password untuk enkripsi: ")
            encrypted = encryptor.encrypt(js_code, password)
            print_result(f"Hasil enkripsi: {encrypted}")
        
        elif choice == '2':
            encrypted_js = input("Masukkan kode JavaScript terenkripsi: ")
            use_password = input("Apakah Anda ingin menggunakan password? (y/n): ").lower() == 'y'
            if use_password:
                password = input("Masukkan password untuk dekripsi: ")
                decrypted = encryptor.decrypt(encrypted_js, password)
            else:
                decrypted = encryptor.decrypt(encrypted_js)
            print_result(f"Hasil dekripsi: {decrypted}")
        
        elif choice == '3':
            js_code = input("Masukkan kode JavaScript yang akan diobfuskasi: ")
            obfuscated = obfuscate_js(js_code)
            print_result(f"Hasil obfuskasi: {obfuscated}")
        
        elif choice == '4':
            obfuscated_js = input("Masukkan kode JavaScript terobfuskasi: ")
            deobfuscated = deobfuscate_js(obfuscated_js)
            print_result(f"Hasil deobfuskasi: {deobfuscated}")
        
        elif choice == '5':
            js_code = input("Masukkan kode JavaScript yang akan diminifikasi: ")
            minified = minify_js(js_code)
            print_result(f"Hasil minifikasi: {minified}")
        
        elif choice == '6':
            js_code = input("Masukkan kode JavaScript yang akan dipercantik: ")
            beautified = beautify_js(js_code)
            print_result(f"Hasil mempercantik: {beautified}")
        
        elif choice == '7':
            js_code = input("Masukkan kode JavaScript yang akan dikompresi: ")
            compressed = compress_js(js_code)
            print_result(f"Hasil kompresi: {compressed}")
        
        elif choice == '8':
            compressed_js = input("Masukkan kode JavaScript terkompresi: ")
            decompressed = decompress_js(compressed_js)
            print_result(f"Hasil dekompresi: {decompressed}")
        
        elif choice == '9':
            var_name = generate_random_var_name()
            print_result(f"Nama variabel acak: {var_name}")
        
        elif choice == '10':
            js_code = input("Masukkan kode JavaScript: ")
            anti_debugged = add_anti_debugging(js_code)
            print_result(f"Kode dengan anti-debugging: {anti_debugged}")
        
        elif choice == '11':
            js_code = input("Masukkan kode JavaScript: ")
            watermark = input("Masukkan watermark: ")
            watermarked = add_watermark(js_code, watermark)
            print_result(f"Kode dengan watermark: {watermarked}")
        
        elif choice == '12':
            string = input("Masukkan string yang akan dienkripsi: ")
            encrypted_string = encrypt_string(string)
            print_result(f"String terenkripsi: {encrypted_string}")
        
        elif choice == '13':
            js_code = input("Masukkan kode JavaScript: ")
            expiration_date = input("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")
            expired = add_expiration(js_code, expiration_date)
            print_result(f"Kode dengan kadaluarsa: {expired}")
        
        elif choice == '14':
            js_code = input("Masukkan kode JavaScript: ")
            chunks = split_into_chunks(js_code)
            print_result(f"Kode telah dipisah menjadi {len(chunks)} chunk")
        
        elif choice == '15':
            chunks = []
            while True:
                chunk = input("Masukkan chunk (atau tekan Enter untuk selesai): ")
                if not chunk:
                    break
                chunks.append(chunk)
            joined = join_chunks(chunks)
            print_result(f"Kode yang digabung: {joined}")
        
        elif choice == '16':
            js_code = input("Masukkan kode JavaScript: ")
            complexity = analyze_complexity(js_code)
            print_result(f"Analisis kompleksitas:\n{complexity}")
        
        elif choice == '17':
            js_code = input("Masukkan kode JavaScript: ")
            documentation = generate_documentation(js_code)
            print_result(f"Dokumentasi:\n{documentation}")
        
        elif choice == '18':
            js_code = input("Masukkan kode JavaScript: ")
            arrow_functions = convert_to_arrow_functions(js_code)
            print_result(f"Kode dengan arrow functions: {arrow_functions}")
        
        elif choice == '19':
            js_code = input("Masukkan kode JavaScript: ")
            strict_mode = add_strict_mode(js_code)
            print_result(f"Kode dengan strict mode: {strict_mode}")
        
        elif choice == '20':
            js_code = input("Masukkan kode JavaScript: ")
            no_console_log = remove_console_log(js_code)
            print_result(f"Kode tanpa console.log: {no_console_log}")
        
        elif choice == '21':
            js_code = input("Masukkan kode JavaScript: ")
            unicode_encoded = encode_unicode(js_code)
            print_result(f"Kode dengan encoding Unicode: {unicode_encoded}")
        
        elif choice == '22':
            encoded_js = input("Masukkan kode JavaScript terenkode Unicode: ")
            unicode_decoded = decode_unicode(encoded_js)
            print_result(f"Kode yang didekode: {unicode_decoded}")
        
        elif choice == '23':
            js_code = input("Masukkan kode JavaScript: ")
            self_destructed = add_self_destruction(js_code)
            print_result(f"Kode dengan self-destruction: {self_destructed}")
        
        elif choice == '24':
            print_cyber_style("Terima kasih telah menggunakan Javascript Tools!", Fore.MAGENTA)
            break
        
        else:
            print_cyber_style("Pilihan tidak valid. Silakan coba lagi.", Fore.RED)
        
        print_fancy_border()
        next_action = input(f"{Fore.YELLOW}Tekan Enter untuk kembali ke menu utama atau ketik 'exit' untuk keluar: {Style.RESET_ALL}")
        if next_action.lower() == 'exit':
            print_cyber_style("Terima kasih telah menggunakan Javascript Tools!", Fore.MAGENTA)
            break

if __name__ == "__main__":
    main()
