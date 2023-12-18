import yaml
import requests
import time
from urllib.parse import urlparse

# YAML File Reader depending on the input path user sends in
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data

# records the responses after hitting all the endpoints from data
def check_endpoints(data):
    responses = []
    for d in data:
        method = d.get("method", "GET")
        url = d["url"]
        headers = d.get("headers", {})
        body = d.get("body", None)

        start_time = time.time()
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, timeout=0.5)
            else:
                response = requests.request(method, url, headers=headers, data=body, timeout=0.5)
            elapsed_time = time.time() - start_time

            if 200 <= response.status_code < 300 and elapsed_time < 0.5:
                responses.append({"url": url, "status": "UP"})
            else:
                responses.append({"url": url, "status": "DOWN"})
        except requests.RequestException:
            responses.append({"url": url, "status": "DOWN"})

    return responses

# extracts the domain name from the url
def extractDomainName(url):
    return urlparse(url).netloc
        
# returns the availability percentage from all endpoints
def logMetrics(status_list):
    up_counter = 0
    down_counter = 0
    for status in status_list:
        if status == "UP":
            up_counter += 1
        elif status == "DOWN":
            down_counter += 1
    
    total_counter = up_counter + down_counter
    if total_counter == 0:
        return 0
    else:
        return round((up_counter / total_counter) * 100)



def main():
    file_path = input("Enter the Sample File Path to the YAML File: ")
    data = read_yaml(file_path)

# continuously checks the endpoints
    while(True):
        responses = check_endpoints(data)
        domain_names_to_status = {} #fetch.com, UP_counter, DOWN_counter
        for response in responses:
            domain_name = extractDomainName(response.get("url", ""))
            if domain_name in domain_names_to_status:
                status_list = domain_names_to_status[domain_name]
                status_list.append(response.get("status", ""))
            else:
                status_list = []
                status_list.append(response.get("status", ""))
                domain_names_to_status[domain_name] = status_list

        for domain_name in domain_names_to_status:
            up_rate = logMetrics(domain_names_to_status[domain_name])
            formatted_string = f"{domain_name} has {up_rate}% availability percentage"

            print(formatted_string)

        time.sleep(15)

if __name__ == "__main__":
    main()