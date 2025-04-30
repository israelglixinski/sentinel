#!/usr/bin/env python3

import os
import sys
import subprocess
import platform
import shutil
import zipfile
import urllib.request


def run_command(command, shell=False):
    result = subprocess.run(command, shell=shell)
    if result.returncode != 0:
        print(f"❌ Erro ao executar: {' '.join(command)}")
        sys.exit(1)


def upgrade_build_tools():
    print("📦 Atualizando pip, setuptools e wheel...")
    run_command([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])


def install_ffmpeg():
    system = platform.system()

    if system == "Windows":
        print("🔧 Instalando FFmpeg no Windows...")

        ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        zip_path = "ffmpeg.zip"
        extract_dir = "ffmpeg"

        if not os.path.exists("ffmpeg"):
            print("⬇️ Baixando FFmpeg...")
            urllib.request.urlretrieve(ffmpeg_url, zip_path)

            print("📦 Extraindo FFmpeg...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            # Encontra a pasta 'bin' dentro do diretório extraído
            bin_dir = None
            for root, dirs, files in os.walk(extract_dir):
                if 'ffmpeg.exe' in files:
                    bin_dir = root
                    break

            if bin_dir:
                # Adiciona ao PATH temporariamente
                os.environ["PATH"] = f"{bin_dir};" + os.environ["PATH"]
                print(f"✅ FFmpeg pronto para uso (temporariamente via PATH): {bin_dir}")
            else:
                print("❌ Não foi possível localizar o ffmpeg.exe")
                sys.exit(1)

            # Limpa o zip
            os.remove(zip_path)
        else:
            print("🟡 FFmpeg já extraído.")

    elif system == "Linux":
        print("🔧 Instalando FFmpeg no Linux...")
        run_command(["sudo", "apt", "update"])
        run_command(["sudo", "apt", "install", "-y", "ffmpeg"])

    elif system == "Darwin":  # macOS
        print("🔧 Instalando FFmpeg no macOS...")
        run_command(["brew", "install", "ffmpeg"])
    else:
        print("❌ Sistema operacional não suportado para instalação automática do FFmpeg.")
        sys.exit(1)


def install_whisper():
    print("🧠 Instalando openai-whisper do GitHub...")
    run_command([sys.executable, "-m", "pip", "install", "git+https://github.com/openai/whisper.git"])


def main():
    print("🚀 Iniciando processo de instalação completa...\n")
    upgrade_build_tools()
    install_ffmpeg()
    install_whisper()
    print("\n✅ Instalação concluída com sucesso!")


if __name__ == "__main__":
    main()
