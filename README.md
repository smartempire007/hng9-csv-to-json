# HNG9-CSV-TO-JSON

This console script takes the CSV file and generates a CHIP-0007 compatible json, then calculates the sha256 of the json file and append each row  with the generated hash in the new output.csv.

## [](https://github.com/smartempire007/hng9-csv-to-json.git) Repository

https://github.com/smartempire007/hng9-csv-to-json.git

Cloning this repo:

```
git clone https://github.com/smartempire007/hng9-csv-to-json.git

```

```
cd into hng9-csv-to-json

```
### Running the script containing the program

open a CLI of your choice make sure your terminal is in the current working directory, then type:
```
python script.py
```
when the program finished running it will generate a json file for each row in the csv and also generate **filename.output.csv**  file containing a hashed function for each of the nft's.