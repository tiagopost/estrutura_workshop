import os
import pandas as pd

from app.pipeline.extract import extract_from_excel
from app.pipeline.transform import concat_data_frames
from app.pipeline.load import load_excel

# Define test data directory
TEST_DATA_DIR = "tests/test_data"

# Test extract_from_excel function
def test_extract_from_excel():
    # Create a temporary excel file for testing
    test_data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    test_file_path = os.path.join(TEST_DATA_DIR, "test_extract.xlsx")
    test_data.to_excel(test_file_path, index=False)

    # Test the function
    data_frame_list = extract_from_excel(TEST_DATA_DIR)
    
    # Assert the output
    assert isinstance(data_frame_list, list)
    assert len(data_frame_list) == 1
    assert isinstance(data_frame_list[0], pd.DataFrame)
    assert data_frame_list[0].equals(test_data)

    # Clean up the temporary file
    os.remove(test_file_path)

# Test concat_data_frames function
def test_concat_data_frames():
    # Create test data frames
    df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df2 = pd.DataFrame({"A": [7, 8, 9], "B": [10, 11, 12]})
    expected_result = pd.concat([df1, df2], ignore_index=True)

    # Test the function
    result = concat_data_frames([df1, df2])

    # Assert the output
    assert isinstance(result, pd.DataFrame)
    assert result.equals(expected_result)

# Test load_excel function
def test_load_excel():
    # Create a test data frame
    test_data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    output_path = os.path.join(TEST_DATA_DIR, "output")
    filename = "test_output"

    # Test the function
    result = load_excel(test_data, output_path, filename)

    # Assert the output
    assert result == "arquivo salvo com sucesso"
    assert os.path.exists(os.path.join(output_path, f"{filename}.xlsx"))

    # Clean up the generated file
    os.remove(os.path.join(output_path, f"{filename}.xlsx"))
    os.rmdir(output_path)
