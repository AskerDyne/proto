# Imports
import os
import subprocess
import sys
from colorama import Fore

# Configuration
sys.tracebacklimit = 0

print_text = (f"{Fore.WHITE}")
print_dividers = (f"{Fore.LIGHTRED_EX}")
print_success = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]")
print_failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]")
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]")
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]")
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]")
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]")
print_command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ")

# Get drives and user
subprocess.run(["lsblk"])
user = os.getlogin()
luks_drive = input(f"\n{print_question} LUKS master drive: "); print(f"\n{print_prompt} Enter U for Unknown!")
luks_type = input(f"{print_question} LUKS type [1,2,U]: ")
print(f"\n{print_alert} This is a slow process - do not quit as it may cause corruption of the LUKS system.")

# Extracts drive header
subprocess.run(["sudo", "dd", "if=/dev/" + luks_drive, "bs=1", "count=16777216", "of=/home/" + user + "/Documents/luks_extracted"])
subprocess.run(["sudo", "cryptsetup", "luksDump", "/home/" + user + "/Documents/luks_extracted"])

# Attack method
attack_type = input(f"\n{print_question} What type of attack do you want? [Singular, Hashcat]: ")

if attack_type == "Singular":
    word_select = input(f"\n{print_question} Singular word: ")
    subprocess.run(['bash', '-c', f'echo "{word_select}" | sudo cryptsetup --test-passphrase open /home/{user}/Documents/luks_extracted 2>&1 | tee output.txt && (grep -q "No key available with this passphrase." output.txt && (echo && echo "{print_failed} | Invalid: {word_select}\n") || (echo && echo "{print_success} | Valid: {word_select}\n"))'])

elif attack_type == "Hashcat": # Hashcat must be installed
    luks_extracted = input(f"\n{print_question} LUKS header full-file path: ")
    dict_file = input(f"\n{print_question} Dictionary full-file path: ")
    subprocess.run(["hashcat", "-m", "14600", "-a", "0", "-w", "3", f"{luks_extracted}", f"{dict_file}", "-o", "luks_password.txt"])

else:
    print(f"{print_exited}")
    quit()