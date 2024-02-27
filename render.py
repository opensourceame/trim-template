# from pprint import pprint
# from bs4 import BeautifulSoup
# from collections import deque

from skimpy.skimpy import Skimpy

path = "file.slim"

# class Line:
#     def __init__(self, type, text):
#         self.type = type
#         self.text = text





skimpy = Skimpy("file.slim")
output = skimpy.render()
print(output)

# pprint(skimpy.__dict__)

# skimpy.debug()
