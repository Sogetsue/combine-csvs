import os
import glob
import pandas as pd

def log_combine():
    input_path=input("Please input the path of the files you would like to combine : ").replace("\\","\\\\").replace('"',"")
    search_criteria=input("Please input the prefix of the files (i.e. 'Accounting*.csv' or if all files of a type '*.csv') : ")
    output_path=input("Please input where you would like the output file to be saved : ").replace("\\","\\\\").replace('"',"")
    output_name=input("What would you like to call your output file? (include file suffix .csv) : ")
    print("Logs are being combined, please wait...")

    slash = "\\"
    output_file = f'{output_path}{slash}{output_name}'

    files = glob.glob(os.path.join(input_path, search_criteria))

    data = []

    for file in files:
        try:
            dataframe = pd.read_csv(file)
            data.append(dataframe)
        except:
            print("",
            "There was an issues with the following log file: ",
            "",
            file,
            )
            pass
    try:
        readSuccess = pd.concat(data, ignore_index=True)
        readSuccess.to_csv(output_file, index=False)
        print("Successfully combined files, see result at", output_file)
    except ValueError as vError:
        print(vError)
    except pd.EmptyDataError as noDataError:
        print(noDataError)
    

if __name__ == '__main__':
    log_combine()