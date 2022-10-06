import re
from level_packs import create_pack as c

t = "print('sldkfjaldskjfad')"

x = re.findall("^p.*t$", t)

print(x)
