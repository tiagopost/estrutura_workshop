import pandas as pd
import os

def load_excel(data_frame: pd.DataFrame, output_path:str, filename: str) -> str:

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(f"{output_path}/{filename}.xlsx", index=False)
    return "arquivo salvo com sucesso"