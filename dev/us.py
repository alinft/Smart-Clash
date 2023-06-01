import urllib.request
import re
import time

url = "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml"
output_file = "usfiltered.yml"
six_hours = 6 * 60 * 60  # 6 hours in seconds

while True:
  current_time = time.time()
  next_time = current_time + six_hours - (current_time % six_hours)
  time.sleep(next_time - current_time)

  with urllib.request.urlopen(url) as f:
    content = f.read().decode('utf-8')

  filtered_content = re.sub(r'\n- 🇺🇸US', '', content)

  with open(output_file, "w") as f:
    f.write("proxies:\n" + filtered_content)
