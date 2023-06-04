import urllib.request
import re

url = "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml"
output_file = "./node/id.yml"

def export_us_content():
    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
    filtered_content = re.findall(r'^.*🇮🇩ID.*', content, flags=re.MULTILINE)
    with open(output_file, "w") as f:
        f.write("proxies:\n")  # Add proxies: at the beginning of the file
        for line in filtered_content:
            f.write(line + "\n")
    print("🇮🇩ID exported.")

export_us_content()
