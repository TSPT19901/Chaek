from Signup_Login import login_signup #import signup login file
from colorama import init, Fore, Style
init(autoreset=True)

chaek_text = f"""
                                                        {Fore.RED} ██████╗ {Fore.YELLOW}██╗  ██╗ {Fore.GREEN}█████╗ {Fore.CYAN}███████╗{Fore.MAGENTA}██╗  ██╗
                                                        {Fore.RED}██╔════╝ {Fore.YELLOW}██║  ██║{Fore.GREEN}██╔══██╗{Fore.CYAN}██╔════╝{Fore.MAGENTA}██║ ██╔╝
                                                        {Fore.RED}██║      {Fore.YELLOW}███████║{Fore.GREEN}███████║{Fore.CYAN}█████╗  {Fore.MAGENTA}█████╔╝ 
                                                        {Fore.RED}██║      {Fore.YELLOW}██╔══██║{Fore.GREEN}██╔══██║{Fore.CYAN}██╔══╝  {Fore.MAGENTA}██╔═██╗ 
                                                        {Fore.RED}╚██████  {Fore.YELLOW}██║  ██║{Fore.GREEN}██║  ██║{Fore.CYAN}███████╗{Fore.MAGENTA}██║  ██╗
                                                        {Fore.RED} ╚═════╝ {Fore.YELLOW}╚═╝  ╚═╝{Fore.GREEN}╚═╝  ╚═╝{Fore.CYAN}╚══════╝{Fore.MAGENTA}╚═╝  ╚═╝
        """


#display welcome 
print("                                         -------------------WELCOME TO PERSONAL SECURITY TOOLKIT-------------------")

for i in range(3):
    print("")
print(Style.BRIGHT + chaek_text)
input("                                                          Press Enter to continue to the Chaek: ")
for i in range(5):
    print("")
print("                                         --------------------------------------------------------------------------")
print("\n\n\n")
#Call function signup/login from login_signup file.py
login_signup.sign_up_login()
