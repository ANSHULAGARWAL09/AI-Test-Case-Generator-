import pandas as pd


def save_excel(data):

    df = pd.DataFrame(data)

    output_file = (
        "output/generated_testcases.xlsx"
    )

    df.to_excel(
        output_file,
        index=False
    )

    return output_file