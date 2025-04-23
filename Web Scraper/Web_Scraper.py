from time import sleep
import urllib.request
import bs4 as beautifulsoup
import os
from colorama import Fore, Style, init

init(autoreset=True)

GREEN = Fore.GREEN
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

Target_Website = input(f"{GREEN}Enter Target Website Url:\n\n{RESET}{GREEN}")
def get_source(url):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = f"https://{url}"  
        return urllib.request.urlopen(url).read()
    except Exception as e:
        print(f"{GREEN}Error fetching the webpage: {RESET}{e}")
        sleep(2)
        quit()

source = get_source(Target_Website)
soup = beautifulsoup.BeautifulSoup(source, 'lxml')

UserName = os.getlogin()
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')  
file = "Output From Web Scraper.txt"
Title = soup.title
Attributes = soup.title.name
Values = soup.title.string
Navi = soup.title.parent.string
SpecValue = soup.p
ParaTag = soup.find_all('p')
Text = soup.get_text()
FullPage = soup.prettify

def IterThruParaTags():
    for paragraph in soup.find_all('p'):
        print(f"{WHITE}{paragraph.text}{RESET}")

def GrabURLS():
    for url in soup.find_all('a'):
        print(f"{WHITE}{url.get('href')}{RESET}")

print(f"{GREEN}1. Page Title\n2. Page Attributes\n3. Page Values\n4. Page Navigation\n5. Specific Values\n6. Paragraph Tags\n7. Iterate Through Paragraph Tags\n8. Grab Links\n9. Grab Text\n10. Full Page\n\n{RESET}")
User_Input = int(input(f"{GREEN}Enter Your Choice:\n\n{RESET}{GREEN}"))

if User_Input == 1:
    print(f"{WHITE}{Title}{RESET}")
elif User_Input == 2:
    print(f"{WHITE}{Attributes}{RESET}")
elif User_Input == 3:
    print(f"{WHITE}{Values}{RESET}")
elif User_Input == 4:
    print(f"{WHITE}{Navi}{RESET}")
elif User_Input == 5:
    print(f"{WHITE}{SpecValue}{RESET}")
elif User_Input == 6:
    print(f"{WHITE}{ParaTag}{RESET}")
elif User_Input == 7:
    IterThruParaTags()
elif User_Input == 8:
    GrabURLS()
elif User_Input == 9:
    print(f"{WHITE}{Text}{RESET}")
elif User_Input == 10:
    print(f"{WHITE}{FullPage}{RESET}")
else:
    print(f"{GREEN}Invalid Input.{RESET}")
    sleep(2)
    quit()

Input_File = input(f"{GREEN}Would you like this in a text file, on your desktop? (WARNING: IF YOU ALREADY HAVE ONE THE DATA WILL BE ERASED) Y/N\n\n{RESET}{GREEN}")
if Input_File.upper() == "Y" or "y":
    os.makedirs(desktop_path, exist_ok=True)
    file_path = os.path.join(desktop_path, file)
    with open(file_path, 'w', encoding='utf-8') as fp:
        fp.write("Web Scraper Output:\n\n")
        if User_Input == 1:
            fp.write(f"{Title}")
        elif User_Input == 2:
            fp.write(f"{Attributes}")
        elif User_Input == 3:
            fp.write(f"{Values}")
        elif User_Input == 4:
            fp.write(f"{Navi}")
        elif User_Input == 5:
            fp.write(f"{SpecValue}")
        elif User_Input == 6:
            fp.write(f"{ParaTag}")
        elif User_Input == 7:
            fp.write("Iterating Through Paragraph Tags:\n\n")
            for paragraph in soup.find_all('p'):
                fp.write(f"{paragraph.text}")
        elif User_Input == 8:
            fp.write("Links Found on the Page:\n\n")
            for url in soup.find_all('a'):
                fp.write(f"{url.get('href')}")
        elif User_Input == 9:
            fp.write(Text)
        elif User_Input == 10:
            fp.write(f"{soup.prettify}")
        else:
            fp.write("Invalid Input.\n\n")
            sleep(2)
            quit()
    
    print(f"{GREEN}File saved to: {file_path}{RESET}")
else:
    print(f"{GREEN}File Not Created{RESET}")