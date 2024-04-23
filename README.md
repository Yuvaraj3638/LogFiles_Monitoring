# Log Monitoring and Analysis Script

This Python script allows you to monitor a specified log file for new entries in real-time and perform basic analysis on the log entries.

## Requirements

- Python 3.x
- logfile path

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Yuvaraj3638/LogFiles_Monitoring.git
    ```

2. Navigate to the project directory:

    ```bash
    cd log-monitor
    ```

3. Run the script:

    ```bash
    python log_monitor.py <log_file_path>
    ```

    Replace `<log_file_path>` with the path to the log file you want to monitor.

4. The script will start monitoring the specified log file and print any new log entries in real-time. Press `Ctrl+C` to stop the monitoring.

## Example

```bash
python log_monitor.py /path/to/your/log/file.log
