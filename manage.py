#!/usr/bin/env python3

import os
import sys
import subprocess


def create_virtualenv():
    """Cria um ambiente virtual chamado .venv"""
    if os.path.exists(".venv"):
        print("🟡 Ambiente virtual .venv já existe.")
    else:
        print("🔧 Criando ambiente virtual .venv...")
        subprocess.run([sys.executable, "-m", "venv", ".venv"])
        print("✅ Ambiente virtual criado com sucesso.")

    # Cria script para ativação
    if os.name == 'nt':
        with open("active.bat", "w") as f:
            f.write(".venv\\Scripts\\activate\n")
    else:
        with open("active.sh", "w") as f:
            f.write("source .venv/bin/activate\n")


def activate_virtualenv():
    """Mostra o comando para ativar o ambiente virtual dependendo do sistema operacional"""
    print("\n💡 Para ativar o ambiente virtual, use:")
    if os.name == 'nt':
        print("   .venv\\Scripts\\activate")
    else:
        print("   source .venv/bin/activate")


def freeze_requirements():
    """Salva os pacotes instalados no requirements.txt"""
    if not os.path.exists(".venv"):
        print("❌ O ambiente virtual não foi encontrado. Rode 'init' primeiro.")
        return
    print("📦 Gerando requirements.txt com pacotes instalados...")
    subprocess.run([".venv/bin/pip" if os.name != 'nt' else ".venv\\Scripts\\pip.exe", "freeze", ">", "requirements.txt"], shell=True)
    print("✅ Arquivo requirements.txt atualizado.")


def install_requirements():
    """Instala os pacotes do requirements.txt"""
    if not os.path.exists("requirements.txt"):
        print("❌ Arquivo requirements.txt não encontrado.")
        return
    if not os.path.exists(".venv"):
        print("❌ Ambiente virtual não encontrado. Rode 'init' primeiro.")
        return
    print("📦 Instalando pacotes do requirements.txt...")
    subprocess.run([".venv/bin/pip" if os.name != 'nt' else ".venv\\Scripts\\pip.exe", "install", "-r", "requirements.txt"])
    print("✅ Pacotes instalados com sucesso.")


def show_help():
    print("""
📘 Comandos disponíveis:

  init           Cria o ambiente virtual .venv
  active         Mostra o comando para ativar o ambiente virtual
  freeze         Salva os pacotes instalados em requirements.txt
  install        Instala pacotes do requirements.txt
  help           Mostra esta ajuda

Exemplo de uso:
  python manage.py init
  python manage.py freeze
  python manage.py install
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "init":
        create_virtualenv()
        activate_virtualenv()
    elif command == "active":
        activate_virtualenv()
    elif command == "freeze":
        freeze_requirements()
    elif command == "install":
        install_requirements()
    elif command == "help":
        show_help()
    else:
        print(f"❌ Comando desconhecido: {command}")
        show_help()


if __name__ == "__main__":
    main()
