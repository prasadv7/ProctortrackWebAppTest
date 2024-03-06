import os
import requests
from statistics import mean
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ChromeController  # Install this library with: pip install chrome-controller


def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    base_url = lines[0]
    api_urls = [base_url + line if not line.startswith("http") else line for line in lines[1:]]

    return api_urls


def write_results_to_file(results, file_path):
    with open(file_path, 'w') as file:
        for link, avg_time, request_times, response_times in results:
            file.write(f"{link} - Average Response Time: {avg_time} seconds\n")
            file.write("Individual Request and Response Times:\n")
            for request_time, response_time in zip(request_times, response_times):
                file.write(f"{link} - Request Time: {request_time} seconds, Response Time: {response_time} seconds\n")
            file.write("\n")


def links1(links, num_tests):
    all_avg_times = []
    options = Options()
    options.headless = True

    for link in links:
        request_times = []
        response_times = []

        for _ in range(num_tests):
            try:
                # Start Chrome with remote debugging enabled
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--remote-debugging-port=9222')
                driver = webdriver.Chrome(options=chrome_options)

                # Navigate to the URL
                driver.get(link)

                # Wait for the page to load (you may need to adjust this based on your page)
                time.sleep(2)

                # Connect to Chrome DevTools
                with ChromeController() as chrome:
                    # Get the Performance domain
                    performance = chrome.get_performance()

                    # Retrieve the timing information
                    timing = performance.get_metrics()

                    # Extract the relevant timing values
                    request_start_time = timing['timestamps']['requestStart'] / 1000.0
                    response_start_time = timing['timestamps']['responseStart'] / 1000.0

                    # Calculate request and response times
                    request_time = response_start_time - request_start_time
                    response_time = time.time() - response_start_time

                    request_times.append(request_time)
                    response_times.append(response_time)

                    print(f"{link} - Request Time: {request_time} seconds, Response Time: {response_time} seconds")

            except Exception as e:
                print(f"{link} - Error: {e}")

            finally:
                # Close the browser
                driver.quit()

        avg_request_time = mean(request_times)
        avg_response_time = mean(response_times)
        all_avg_times.append((link, avg_response_time, request_times, response_times))

        print(f"\nAverage Request Time for {link}: {avg_request_time} seconds")
        print(f"Average Response Time for {link}: {avg_response_time} seconds\n")

    return all_avg_times


# Using os.path.join to construct file paths
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
links_file_path = os.path.join(desktop_path, 'input_links.txt')
results_file_path = os.path.join(desktop_path, 'output_results.txt')

links = read_links_from_file(links_file_path)
num_tests = 3

average_times = links1(links, num_tests)

print("\nAll Average Request and Response Times:")
for link, avg_response_time, _, _ in average_times:
    print(f"{link} - Average Response Time: {avg_response_time} seconds")

write_results_to_file(average_times, results_file_path)


# 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
# gpt-3.5-turbo-instruct