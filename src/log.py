from datetime import datetime

def file_log(message, type="status"):
    with open("src/logHistory.txt", "a") as log_file:
        completed_logged_line = f"[{datetime.now()}] [{type}] {message}\n"
        log_file.write(completed_logged_line)

def clear_log():
    with open("src/logHistory.txt", "w") as log_file:
        log_file.write("")
    
if __name__ == "__main__":
    exit(0)