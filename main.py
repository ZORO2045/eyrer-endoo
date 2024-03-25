import random
import string

def generate_code(length=27):
    characters = string.ascii_letters + string.digits
    prefix = "AQAA"
    random_length = random.randint(1, 6)
    random_chars = ''.join(random.choice(characters) for _ in range(random_length))
    remaining_length = length - len(prefix) - len(random_chars)
    code = random_chars + ''.join(random.choice(characters) for _ in range(remaining_length))
    return code[:12] + prefix + code[12:]

def generate_links(count=10):
    links = [f"https://t.me/giftcode/{generate_code()}" for _ in range(count)]
    return links

def print_banner():
    banner = """
\033[1;31m███████╗██╗░░░██╗██████╗░███████╗██████╗░
██╔════╝╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗
█████╗░░░╚████╔╝░██████╔╝█████╗░░██████╔╝
██╔══╝░░░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗
███████╗░░░██║░░░██║░░██║███████╗██║░░██║
╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
███████╗███╗░░██╗██████╗░░█████╗░░█████╗░
██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗
█████╗░░██╔██╗██║██║░░██║██║░░██║██║░░██║
██╔══╝░░██║╚████║██║░░██║██║░░██║██║░░██║
███████╗██║░╚███║██████╔╝╚█████╔╝╚█████╔╝
╚══════╝╚═╝░░╚══╝╚═════╝░░╚════╝░░╚════╝░
"""
    developer = "\033[1;31mBy: ፚ Ꭷ Ꮢ Ꭷ ❥\033[0m"
    Telegram = "\033[1;31mTelegram: @ZORO2045\033[0m"
    print(banner)
    print(developer)
    print(Telegram)

def main():
    print_banner()
    print("Welcome!")
    while True:
        command = input("Enter a command (\033[1;32mcheck\033[0m/\033[1;32mhelp\033[0m/\033[1;32mexit\033[0m): ")
        if command == "check":
            links = generate_links()
            print("\nGenerated links:")
            for i, link in enumerate(links, start=1):
                color_code = random.choice(["\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m"])
                print(f"{color_code}{i}. {link}\033[0m")
            print()
        elif command == "help":
            print("\033[1;33mCommands:\033[0m")
            print("- \033[1;32mcheck\033[0m: Generate and display 10 links.")
            print("- \033[1;32mhelp\033[0m: Display this help message.")
            print("- \033[1;32mexit\033[0m: Exit the program.\n")
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
