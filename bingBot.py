import webbrowser, sys, random, string, time

# Number of links to open:
to_open = 20
if(len(sys.argv) > 1):
    to_open = int(sys.argv[1])

# Length of random string:
length = 5

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def randomword(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# open x many searches
if(to_open > 0):
    link = randomword(length)
    webbrowser.get('edge').open_new(f'https://www.bing.com/search?q={link}') # open new browser for first link
    for i in range(to_open-1):
        link = randomword(5)
        webbrowser.get('edge').open_new_tab(f'https://www.bing.com/search?q={link}') # open new tab for rest of links
        time.sleep(2) # sleep a bit
    time.sleep(5)
    webbrowser.delete('edge') # delete all tabs when done
