# Manual for RPGLite Temporal Property Analysis

## [generate_format.py](generate_format.py)
### Gets the data set in the required format to run the Expectation Maximisation Algorithm
 1. Download the RPGLite data set here: [RPGLite](https://researchdata.gla.ac.uk/1070/)
 2. Extract the **rpglite-player-data.json** file and add to src/ directory
 3. Run the *generate_format.py* with `python generate-format.py in_file out_file`
    - Where `in_file` is the RPGLite JSON name
    - Where `out_file` is the output JSON name
 4. The generated `out_file` can be used with the EM Algorithm 

## [prsim_json_to_txt.py](prism_json_to_txt.py)

### Parses the PRISM outputs into a readable structured format
 1. Put all PRISM output files into the `src/in_files` folder
 2. Run *prism_json_to_txt.py* with `python prism_json_to_txt.py`
 3. The output will be added to the `out_files` directory in a structured order with each time interval having a directory and each value of `k` having a sub-directory
 4. The results are in the format:

    state 0 | k1 | k2 | ... | kn

    state 1 | k1 | k2 | ... | kn
 5. These can then be analysed with the aid of Excel and split data to columns

## [user_data.py](user_data.py)

### Used to get descriptive statistics on the data set
 1. Ensure you have ran the [generate_format.py](generate_format.py) file
 2. Uncomment whichever stat you wish to use
 3. Look at the accompanied command to run in terminal e.g. `python user_data.py out.json > user_times.txt`
    1. Where `out.json` is the parsed data
 4. Study the output text file