"""
Write a function that when given a URL as a string,
parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    assert type(url) == str

    # 1. what is domain?:
    #     if http/https doma
    #     if www. doma
    #     if _/ name ! = domain

    domain = ''
    newurl = url

    for i, letter in enumerate(url):
        # print(i, letter, url[i:i+4])

        if letter == '/' and url[i+1] == '/':
            newurl = url[i+2:]
            print('MI ZDES')

        elif url[i:i+4] == 'www.':
            newurl = url[i+4:]
            # print('MI TYT')
            break
        # else:
        #     newurl = url

    for letter in newurl:
        if letter != '.':
            domain += letter
        else:
            break
    # print(domain)
    return domain

print(domain_name("github.com/carbonfive/raygun"))