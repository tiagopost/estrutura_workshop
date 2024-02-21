"""esse é o módulo de extração de dados."""

import glob  # biblioteca para listar arquivos
import os  # biblioteca para manipular arquivos e pastas
from typing import List

import pandas as pd

"""
funcao para ler arquivos de uma pasta
"""


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel(path = "data/input")
    print(data_frame_list)