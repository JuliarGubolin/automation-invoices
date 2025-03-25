import os
from pathlib import Path
import shutil

directory_origin = "/home/julia-rodrigues-gubolin/Área de trabalho/EMPRESAS/DRIVE"
directory_destiny = "/home/julia-rodrigues-gubolin/Área de trabalho/EMPRESAS//01 - CLIENTES/2025"
directory_destiny2 = "/home/julia-rodrigues-gubolin/Área de trabalho/EMPRESAS/02 - CLIENTES/2025"
os.chdir(directory_origin)

if (not Path(directory_origin).is_dir() or not Path(directory_destiny).is_dir() or not Path(directory_destiny2).is_dir()):
  print("Algum dos caminhos foi digitado incorretamente. Verificar.")
else: 
  for folders in os.listdir():
    os.chdir(f"{directory_origin}/{folders}")
    for cnpj in os.listdir():
      if Path(f"{directory_origin}/{folders}/{cnpj}/NFSE PRESTADOS").is_dir():
        os.chdir(f"{directory_origin}/{folders}/{cnpj}/NFSE PRESTADOS")
        files_prestados = os.listdir()
        if len(files_prestados) != 0:
          for file in range(0, len(files_prestados)):
            folders_aux = folders.split('-')
            if Path(f"{directory_destiny}/{folders_aux[1]}/ESCRITA FISCAL/NOTAS FISCAIS/PRESTADOS/03 - MARÇO").is_dir():
              shutil.copy(files_prestados[file], f"{directory_destiny}/{folders_aux[1]}/ESCRITA FISCAL/NOTAS FISCAIS/PRESTADOS/03 - MARÇO")
            elif Path(f"{directory_destiny2}/{folders_aux[1]}/ESCRITA FISCAL/NOTAS FISCAIS/PRESTADOS/03 - MARÇO").is_dir():
              shutil.copy(files_prestados[file], f"{directory_destiny2}/{folders_aux[1]}/ESCRITA FISCAL/NOTAS FISCAIS/PRESTADOS/03 - MARÇO")
          print(folders_aux[1] + " PRESTADOS SALVOS")
        else:
          print(folders_aux[1] + " PRESTADOS VAZIO")
      if Path(f"{directory_origin}/{folders}/{cnpj}/NFSE COMPRADOS").is_dir():
        os.chdir(f"{directory_origin}/{folders}/{cnpj}/NFSE COMPRADOS")
        files_tomados = os.listdir()
        if len(files_tomados) != 0:
          for file in range(0, len(files_tomados)):
            folders_aux = folders.split('-')
            if Path(f"{directory_destiny}/{folders_aux[1]}/ESCRITA FISCAL/NOTAS FISCAIS/TOMADOS/03 - MARÇO").is_dir():
              shutil.copy(files_tomados[file], f"{directory_destiny}/{folders_aux}/ESCRITA FISCAL/NOTAS FISCAIS/TOMADOS/03 - MARÇO")
            elif Path(f"{directory_destiny2}/{folders_aux[1]}/ESCRITA FISCAL/NOTAS FISCAIS/TOMADOS/03 - MARÇO").is_dir():
              shutil.copy(files_prestados[file], f"{directory_destiny2}/{folders_aux[1]}/ESCRITA FISCAL/NOTAS FISCAIS/TOMADOS/03 - MARÇO")
          print(folders_aux[1] + " TOMADOS SALVOS")
        else:
          print(folders_aux[1] + " TOMADOS VAZIO")
      else:
        print("Algo deu errado! Verifique os caminhos digitados")