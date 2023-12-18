# fetch-coding-challenge

**Requirements**

* Python 3
* Pip
* YAML module
* Requests module
  



Usage
1. Clone this repository:
git clone https://github.com/kishanthedeveloper/fetch-coding-challenge

2. Install the requirements:
pip install requests
&& pip3 install --upgrade pip
Below command will check if requirements are satisfied if not it will upgrade to latest one\
  python3 -m pip install --upgrade pip 

4. Run the code:
python3 main.py

5. Enter the file path:
Example- samle file name- inputFile.yaml

**Important make sure to use python3 else it would result into syntax error**


**How it works**

The code is divided into several functions:

read_yaml: This function reads a YAML file and returns the data as a Python object.

check_endpoints: This function takes the data from the YAML file and uses the requests module to check the availability of multiple endpoints. It returns a list of responses.

extractDomainName: This function takes a URL and returns the domain name.

logMetrics: This function takes a list of responses and calculates the availability percentage.

main: This function is the entry point of the program. It reads the YAML file, calls the check_endpoints function, and logs the availability percentage.
