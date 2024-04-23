import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define keywords/patterns to search for in log entries
keywords = ['ERROR', 'HTTP status']

# Path to the log file to monitor
log_file_path = r"C:\Users\Yuvaraj\Desktop\realtime_log.txt"

def monitor_log(log_file_path):
    try:
        with open(log_file_path, "r") as log_file:
            # Read and print the current content of the log file
            logging.info("Current log file content:")
            for line in log_file:
                logging.info(line.strip())

            # Continuously monitor the log file for new entries
            while True:
                line = log_file.readline()
                if line:
                    # Print the new log entry
                    logging.info(line.strip())
                    # Perform basic analysis (count occurrences of keywords)
                    for keyword in keywords:
                        if keyword in line:
                            logging.info(f"Found keyword: {keyword}")
                else:
                    # Sleep for a short interval before checking for new lines again
                    time.sleep(0.1)
    except KeyboardInterrupt:
        logging.info("Monitoring interrupted. Exiting...")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    logging.info(f"Monitoring log file: {log_file_path}")
    monitor_log(log_file_path)

if __name__ == "__main__":
    main()
