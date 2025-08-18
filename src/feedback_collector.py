import json
import os
import datetime
import sys

# Define the output file for storing feedback
FEEDBACK_FILE = "feedback.json"

def get_feedback_record():
    """Prompts the user for feedback details and returns a dictionary."""
    print("--- Chatbot Feedback Collector ---")
    user_id = input("Enter user ID (e.g., '12345'): ").strip()
    feedback_type = input("Feedback type (e.g., 'bug_report', 'feature_request'): ").strip()
    description = input("Please describe the issue or suggestion: ").strip()

    if not all([user_id, feedback_type, description]):
        print("Error: All fields are required. Please try again.")
        return None

    feedback_record = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "user_id": user_id,
        "feedback_type": feedback_type,
        "description": description
    }
    return feedback_record

def save_feedback(record):
    """Saves a single feedback record to a JSON file."""
    if not record:
        return

    # Check if the file exists and has content
    data = []
    if os.path.exists(FEEDBACK_FILE) and os.path.getsize(FEEDBACK_FILE) > 0:
        try:
            with open(FEEDBACK_FILE, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: {FEEDBACK_FILE} is corrupted. Starting a new file.")

    data.append(record)

    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Feedback successfully saved to {FEEDBACK_FILE}")

if __name__ == "__main__":
    new_feedback = get_feedback_record()
    save_feedback(new_feedback)