import urllib.request
import re

url = "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml"
output_file = "usfiltered.yml"

with urllib.request.urlopen(url) as f:
  content = f.read().decode('utf-8')

filtered_content = re.sub(r'\n- 🇺🇸US', '', content)

with open(output_file, "w") as f:
  f.write(filtered_content)
