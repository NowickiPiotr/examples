import random
import string


from UserLog import save_random_user_to_log,read_first_line_from_file


def randomFullName(self,accountLength):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(accountLength))

def randomEmail(self,accountLength):
    emailName=  ''.join(random.choice(string.ascii_uppercase) for _ in range(accountLength))
    email = '@'
    domain= emailName+'.com'

    random_login_name = emailName+email+domain

    save_random_user_to_log(random_login_name,random_login_name)

    return random_login_name

print(randomEmail(3,3))