import cssutils
import urllib

css_path="styles.css"
base_url="https://www.test.com"
file_dest="C:/images/"

sheet = cssutils.parseFile(css_path)

for rule in sheet: 
    if hasattr(rule,'style') and rule.style.backgroundImage!='' and 'url' in rule.style.backgroundImage:
        file_name=rule.style.backgroundImage.split('/')[2].replace(')','').replace("'","")
        file_url=base_url+file_name
        out_loc=file_dest + file_name

        urllib.request.urlretrieve(file_url, out_loc)