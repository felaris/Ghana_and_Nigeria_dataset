# Ghana and Nigeria json data hand trial
This is just a hand on trial on Nigeria and Ghana Json data

---

# JSON to CSV Data Conversion

This Python script is designed to convert JSON data into three CSV files: `country.csv`, `region.csv`, and `city.csv`. It processes hierarchical JSON data and extracts information about countries, regions, and cities, and then structures this data into the CSV format.

## Requirements

- Python 3.x (https://www.python.org/downloads/)

## Usage

1. **Input JSON Data**: Place your JSON data in a file (e.g., `Ghana.json`) in the same directory as the script.

2. **Run the Script**: Execute the Python script to process the JSON data and generate the CSV files.

   ```bash
   python script.py
   ```

3. **Output CSV Files**: Three CSV files will be created in the same directory where the script is located: `country.csv`, `region.csv`, and `city.csv`.

## JSON Data Structure

The script expects JSON data to follow a specific hierarchical structure. For example:

```json
Here's the hierarchy of the provided data:

- `version_number`
- `countries`
  - `Ghana`
    - `name`
    - `latitude`
    - `longitude`
    - `coordinates`
      - List with four values
    - `divisions`
      - `Ahafo`
        - `name`
        - `country`
        - `latitude`
        - `longitude`
        - `coordinates`
          - List with four values
        - `sub_divisions`
          - `Asunafo North`
            - `name`
            - `state`
            - `country`
            - `latitude`
            - `longitude`
            - `north_latitude`
            - `south_latitude`
            - `west_longitude`
            - `east_longitude`
            - `coordinates`
        

The hierarchy represents the nested structure of the data, with each level containing specific attributes and values.
```

Please ensure your JSON data adheres to this structure for the script to work correctly.

## Output CSV Files

The script generates three CSV files:

- `country.csv`: Contains information about countries.
- `region.csv`: Contains information about regions within each country.
- `city.csv`: Contains information about cities within each region.


## Author

- Felix Awortwe Kwamena

Feel free to modify this README to provide more specific information about your project.