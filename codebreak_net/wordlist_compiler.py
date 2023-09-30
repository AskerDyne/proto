# Imports
import sys
from colorama import Fore

# Configuration
sys.tracebacklimit = 0

print_successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]")
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]")
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]")
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]")
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]")

try:
    # Defines file paths
    file1 = "./db/adjectives.txt"
    file2 = "./db/nouns.txt"
    output = "./db/netgear_list.txt"
    file3 = "./db/adjectives_extreme.txt"
    file4 = "./db/nouns.txt"
    output_extreme = "./db/netgear_list_extreme.txt"

    # Reads the contents of files and outputs to their relative lists
    with open(file1, 'rt') as f:
        file1_content = f.read().strip('\n').split('\n')
    with open(file2, 'rt') as f:
        file2_content = f.read().strip('\n').split('\n')
    out = []
    for file1_line in file1_content:
        for file2_line in file2_content:
            out.append(file1_line.strip() + file2_line.strip())
    with open(output, 'wt') as f:
        f.write('\n'.join(out))
    with open(file3, 'rt') as f:
        file3_content = f.read().strip('\n').split('\n')
    with open(file4, 'rt') as f:
        file4_content = f.read().strip('\n').split('\n')
    out_extreme = []
    for file3_line in file3_content:
        for file4_line in file4_content:
            out.append(file3_line.strip() + file4_line.strip())
    with open(output_extreme, 'wt') as f:
        f.write('\n'.join(out))
    print(f"\n{print_exited} {print_notice} {print_successfully}")

# Error handling
except KeyboardInterrupt:
    print(f"\n{print_exited} {print_notice} {print_successfully}")
    print(f'\n{print_notice} You interrupted the program.'); exit()
except ValueError:
    print(f"\n{print_exited} {print_notice} {print_successfully}")
    print(f'\n{print_notice} You entered invalid data into a field.'); exit()