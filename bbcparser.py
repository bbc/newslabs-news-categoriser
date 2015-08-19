import re

class BbcParser:
   @staticmethod
   def parse(url):
     return re.findall(r'([a-z]*)\-', url)
