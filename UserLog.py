import os

def save_random_user_to_log(self,random_login_name):
    with open("RandomUserLog.txt", "a") as text_file:
        print("email_log_name: {}".format(random_login_name), file=text_file)


def read_first_line_from_file(self,file_name):
    path_to_file = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))

    with open(path_to_file, "r") as f:
        for last in f:
            print(last)

        first = f.readline()
        print(first)