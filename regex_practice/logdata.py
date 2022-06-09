import re
# simple function to find patterns in txt files
def log():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
        pattern = """(?P<host>\d+[.]\d+[.]\d+[.]\d+)
                         (\s\-\s)
                         (?P<username>\w+|-)
                         (\s\[)
                         (?P<time>[\w/:]+[\s-]+[\d-]+)
                         (\]\s\")
                         (?P<request>[\w]+.+)
                         (\")"""
        log = []
        for i in re.finditer(pattern,logdata,re.VERBOSE):
            log.append(i.groupdict())
    return log
        

log()