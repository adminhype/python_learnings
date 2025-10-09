from dotenv import load_dotenv
import os
load_dotenv("./.env.user")

username = os.environ.get("USER_NAME")
print("Hello, {}".format(username))