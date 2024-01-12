import requests
from statistics import mean
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        links = [line.strip() for line in file.readlines()]
    return links


def write_results_to_file(results, file_path):
    with open(file_path, 'w') as file:
        for link, avg_time, response_times in results:
            file.write(f"{link} - Average Response Time: {avg_time} seconds\n")
            file.write("Individual Response Times:\n")
            for response_time in response_times:
                file.write(f"{link} - Response Time: {response_time} seconds\n")
            file.write("\n")


links_file_path = 'C:\\Users\\prasa\\OneDrive\\Desktop\\input_links.txt'
results_file_path = 'C:\\Users\\prasa\\OneDrive\\Desktop\\output_results.txt'

links = read_links_from_file(links_file_path)
num_tests = 3


def links1(links, num_tests):
    all_avg_response_times = []
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    for link in links:
        response_times = []

        for _ in range(num_tests):
            try:
                driver.get(link)
                time.sleep(2)

                status_code = requests.get(link).status_code
                response_time = driver.execute_script(
                    "return performance.timing.loadEventEnd - performance.timing.navigationStart") / 1000.0
                response_times.append(response_time)

                print(f"{link} - Status Code: {status_code}, Response Time: {response_time} seconds")

                driver.refresh()
                time.sleep(1)

            except (requests.exceptions.RequestException, Exception) as e:
                print(f"{link} - Error: {e}")

        avg_response_time = mean(response_times)
        all_avg_response_times.append((link, avg_response_time, response_times))

        print(f"\nAverage Response Time for {link}: {avg_response_time} seconds\n")

    driver.quit()
    return all_avg_response_times


average_response_times = links1(links, num_tests)

print("\nAll Average Response Times:")
for link, avg_time, _ in average_response_times:
    print(f"{link} - Average Response Time: {avg_time} seconds")

write_results_to_file(average_response_times, results_file_path)
