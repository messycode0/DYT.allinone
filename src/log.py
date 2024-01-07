from datetime import datetime

def file_log(message, type="status"):
    with open("src/logHistory.txt", "a") as log_file:

        if type == "internal":
            inputed_message_split_A = message.split("[")
            inputed_message_split_B = message.split("]")
            final_inputed_message_split = f"{inputed_message_split_A[0]}[ xxx.xxx.xxxx-xxx ]{inputed_message_split_B[1]}"
            completed_logged_line = f"[{datetime.now()}] [{type}] {final_inputed_message_split}\n"
            log_file.write(completed_logged_line)

            # print(inputed_message_split_A)
            # print()
            # print(inputed_message_split_B)
            # print()
            # print(final_inputed_message_split)
            # print()
            return

        if type == "message_EMO":
            # .encode('ascii', 'ignore')
            message_split = message.split(" ")
            print(message_split)
            # foo = ""
            # for i in range(len(message_split)):
            #     foo = f"{foo} {message_split[i].encode('ascii', 'replace')}"
            completed_logged_line = f"[{datetime.now()}] [{type}] {message.encode('ascii', 'replace')}\n"
            log_file.write(completed_logged_line)
            return
        completed_logged_line = f"[{datetime.now()}] [{type}] {message}\n"
        log_file.write(completed_logged_line)
        return


def clear_log():
    with open("src/logHistory.txt", "w") as log_file:
        log_file.write("")
    return
    
if __name__ == "__main__":
    exit(0)