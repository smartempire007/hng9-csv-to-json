import csv
import json
import hashlib

csvData = 'HNGi9-CSV-FILE.csv'

new_csv_file = 'HNGi9-CSV-FILE.output.csv'

f = open(new_csv_file, 'w')

writer = csv.writer(f)

writer.writerow(
    ['TEAM_NAMES', 'SerialNumber', 'Filename', 'Name', 'Description', 'Gender', 'Attributes', 'UUID', 'SHA256']
)

with open(csvData, 'r') as f:
    read_csv = csv.reader(f, delimiter=',')
    next(read_csv)
    
    data = []
    for a in read_csv:
        data.append(a)

    for row in data:
        team_names = row[0]
        series_number = row[1]
        filename = row[2]
        name= row[3]
        description= row[4]
        gender = row[5]
        attributes = row[6]
        uuid = row[7]

        chip0007_format = {
            "format": "CHIP-0007",
            "name": name,
            "description": description,
            "minting_tool": team_names,
            "sensitive_content": False,
            "series_number": series_number,
            "series_total": 420,
            "attributes": [
                {
                    "trait_type": "gender",
                    "value": gender
                }
            ],
            "collection": {
                "name": "Zuri NFT tickets for free lunch",
                "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
                "attributes": [
                    {
                        "type": "description",
                        "value": "Rewards for accomplishments during HNGi9"
                    }
                ]
            },
        }
        
        attrib = [x.split(':') for x in attributes.split(';')]
                
        for index in attrib:
            chip0007_format['attributes'].append([{'trait_type': index[0].strip(), 'value':index[0].strip()}])

        # generating a json file for each row in the csv file.
        chip0007_json = json.dumps(chip0007_format, indent=4) # Converting the json file to a string.
        with open(f'json_output/{filename}.json', 'w') as f:
            f.write(chip0007_json)
        f.close()

        # generating a hash of the json file and appending it to the csv file.
        hash_256 = hashlib.sha256(chip0007_json.encode()).hexdigest()
        row.append(hash_256)
        writer.writerow(row)

# close the file
f.close()