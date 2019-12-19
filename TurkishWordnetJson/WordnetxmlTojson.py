import json
from lxml import etree
import xmltodict

# You can find Turkish Wordnet from https://github.com/olcaytaner/TurkishWordNet
# Thank you Olcay Taner for this work.

tree = etree.parse("turkish_wordnet.xml")
root = tree.getroot()


stringXml = etree.tostring(root, encoding='utf8', method='xml')


with open('turkishWordNetJson.json', 'w', encoding='utf-8') as f:
    json.dump(xmltodict.parse(stringXml), f, ensure_ascii=False, indent=4)
