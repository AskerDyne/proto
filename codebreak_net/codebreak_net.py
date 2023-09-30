# Imports
import sys
import os
from colorama import Fore

# Configuration
sys.tracebacklimit = 0

print_successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]")
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]")
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]")
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]")

try:
    # Applies a given wordlist to the .hccapx using hashcat for brute-forcing 
    capture = input(f"\n(Netgear must be WPA-PBKDF2-PMKID+EAPOL)\n{print_question} .hccapx full-file path: ")
    wl = input(f"{print_question} Wordlist full-file path: ")
    os.system(f'hashcat -d1 -m22000 -w3 --status -a6 ./etc/captures/{capture} ./var/pipes/wldb/{wl} "?d?d?d"')
    print(f"\n{print_exited} {print_notice} {print_successfully}")

# Error handling
except KeyboardInterrupt:
    print(f"\n{print_exited} {print_notice} {print_successfully}")
    print(f'\n{print_notice} You interrupted the program.'); exit()
except ValueError:
    print(f"\n{print_exited} {print_notice} {print_successfully}")
    print(f'\n{print_notice} You entered invalid data into a field.'); exit()