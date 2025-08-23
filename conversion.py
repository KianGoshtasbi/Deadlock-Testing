import json
import csv
import pandas as pd


def convert_json_to_csv_simple(json_file_path, csv_file_path):
    print("convertins Json to CSV")
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    # Extract only numeric values
    rows = []
    labels = ["cost","tier","wins","losses","matches","players"]
    for item_id, attributes in data.items():
       
        item_name = attributes[0]
        numeric_values = attributes[1:]
        row = {'item_name': item_name}
        
        for i, value in enumerate(numeric_values):
            row[labels[i]] = value 
        rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(csv_file_path, index=False)
    print("Done!")
    return

        





def main():
    print("Running new file")
    convert_json_to_csv_simple("item_attributes.json","itemAttributes.csv")


    



if __name__ == "__main__":
    main()