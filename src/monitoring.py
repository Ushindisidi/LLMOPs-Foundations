import re
import time
import logging

# Configure logging for clear output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_pii(text):
    """Detects personally identifiable information (PII) like emails and phone numbers."""
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

    has_pii = bool(re.search(email_pattern, text) or re.search(phone_pattern, text))
    return has_pii

def process_log_file(file_path):
    """Reads and processes log entries from a file for monitoring purposes."""
    try:
        logging.info("Starting log file processing...")

        with open(file_path, 'r') as f:
            for line in f:
                # Simulate processing time for each log entry
                start_time = time.time()
                time.sleep(0.05)  # Simulate a 50ms delay

                # Check for errors and PII
                is_error = "ERROR" in line.upper()
                is_pii = detect_pii(line)

                latency_ms = (time.time() - start_time) * 1000

                if is_error:
                    logging.error(f"Error Detected! Log entry: {line.strip()}")

                if is_pii:
                    logging.warning(f"PII Detected! Log entry: {line.strip()}")

                logging.info(f"Processed line. Latency: {latency_ms:.2f}ms | PII: {is_pii} | Error: {is_error}")

        logging.info("Log file processing complete.")

    except FileNotFoundError:
        logging.error(f"Error: The file '{file_path}' was not found.")

if __name__ == "__main__":
    process_log_file('mock_chatbot_logs.txt')