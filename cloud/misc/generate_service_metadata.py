import os
import json

# Paths
service_dir = 'docs/service'
output_dir = 'cap'
output_file = os.path.join(output_dir, 'service_index.json')

# Use a dictionary for services
services = {}

# Process each service JSON
for filename in os.listdir(service_dir):
    if filename.endswith('.json') and filename != 'template.json':
        filepath = os.path.join(service_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)

                # Extract required fields
                service_id = data.get("id")   # unique key
                service_name = data.get("service")
                description = data.get("description")
                base_name = filename.replace('.json', '')

                # Main URL
                main_url = data.get("url") or "no_url"
                
                # Instance URL
                instance = data.get("instance", {})
                inst_url = instance.get("url") or "no_url"
                
                # Screenshot (file name in docs/service/, or empty when there is none)
                screenshot_url = data.get('screenshot') or ""

                # Stage
                service_stage = data.get('stage') or 'Unknown'

                # Store entry in dict, keyed by service_id
                services[service_id] = {
                    "id": service_id,
                    "service": service_name,
                    "description": description,
                    "html_name": f"{base_name}.html",
                    "md_file_name": f"{base_name}.md",
                    "png_file_name": screenshot_url,
                    "stage": service_stage,
                    "main_url": main_url,
                    "inst_url": inst_url,
                }

                # Use case questions: one "reg_q_<key>" field per question key
                # (e.g. "1a" = use case 1, question a), default "false". The
                # keys match the "id" of the questions in the use case
                # repository; entries starting with "_" are instructions.
                reg_q = data.get("regulatory-question", {})
                for key, value in reg_q.items():
                    if key.startswith("_"):
                        continue
                    services[service_id][f"reg_q_{key}"] = value or "false"

            except json.JSONDecodeError:
                print(f"Skipping invalid JSON file: {filename}")

# Sort alphabetically by "service" name (not by ID)
services = dict(sorted(services.items(), key=lambda item: item[1]['service'].lower()))

# Write output
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(services, f, indent=2)
