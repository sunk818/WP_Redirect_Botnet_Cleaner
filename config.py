# WP Database creds
DB_HOST = 'localhost'
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''

# Add Colors
class c:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Infection detection regex
regex = """(lobbydesires\.com)|(String\.fromCharCode\(104,116,116,112,115,58,47,47,108,111,98,98,121,100,101,115,105,114,101,115,46,99,111,109,47,108,111,99,97,116,105,111,110,46,106,115,63,115,61,49\))|(107,46,100,101,118,101,108,111)|(108,111,98,98,121,100,101,115,105,114,101,115)|(116,101,120,116,47,106,97,118,97,115,99,114,105,112,116)|(function makemee)|(chr\(104\)\.chr\(116\)\.chr\(116\)\.chr\(112\)\.chr\(115\)\.chr\(58\)\.chr\(47\)\.chr\(47\)\.chr\(108\)\.chr\(101\)\.chr\(116\)\.chr\(115\)\.chr\(109\)\.chr\(97\)\.chr\(107\)\.chr\(101\)\.chr\(112\)\.chr\(97\)\.chr\(114\)\.chr\(116\))|(letsmakeparty3.ga)|(104,116,116,112,115,58,47,47,108,101,116,115,109,97,107,101,112,97,114,116,121,51,46,103,97,47,108,46,106,115,63,100,61,49)|()|(stivenfernando.com)"""