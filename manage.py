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

    # Criação opcional de um script auxiliar para facilitar
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


def show_help():
    print("""
📘 Comandos disponíveis:

  init           Cria o ambiente virtual .venv
  help           Mostra esta ajuda

Exemplo de uso:
  python manage.py init
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
    elif command == "help":
        show_help()
    else:
        print(f"❌ Comando desconhecido: {command}")
        show_help()


if __name__ == "__main__":
    main()
