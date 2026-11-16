import os
import json

# Paths
method_dir = "docs/methods"
output_dir = "cap"
output_file = os.path.join(output_dir, "methods_index.json")

# Use a dictionary for methods
methods = {}


def question_key(data):
    """Canonical use case question key of a method, e.g. "reg_q_1a".

    Method JSON files created from the issue form store the selected question
    as "use_case_question_content" (e.g. "1a"); the platform filters on the
    same "reg_q_<key>" names that the tool index uses.
    """
    if data.get("regulatory_question"):
        return data["regulatory_question"]
    key = (data.get("use_case_question_content") or "").strip()
    if not key or key == "_No response_":
        return ""
    return key if key.startswith("reg_q_") else f"reg_q_{key}"


# Process each method JSON
for filename in os.listdir(method_dir):
    if filename.endswith(".json") and filename != "template.json":
        filepath = os.path.join(method_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)

                # Extract required fields
                method_id = data.get("id", "")
                methods[method_id] = {
                    "id": data.get("id", ""),
                    "method": data.get("method", ""),
                    "issue_number": data.get("issue_number", ""),
                    "sop": data.get("available_sop_or_protocol_url", ""),
                    "method_name_content": data.get("method_name_content", ""),
                    "data_producer_content": data.get("data_producer_content", ""),
                    "method_description_content": data.get(
                        "method_description_content", ""
                    ),
                    "type_content": data.get("ontology_term_url", ""),
                    "vendor_content": data.get("vendor_content", ""),
                    "catalog_number_content": data.get("catalog_number_content", ""),
                    "catalog_webpage_url": data.get("catalog_webpage_url", ""),
                    "citation_content": data.get("citation_content", "")
                    or data.get("citation_url", ""),
                    "workflow_stage_content": data.get("workflow_stage_content", ""),
                    "workflow_substage_content": data.get(
                        "workflow_substage_content", ""
                    ),
                    "regulatory_question": question_key(data),
                    "case_study": data.get("case_study", "")
                    or data.get("use_case_content", ""),
                    "timestamp": data.get("timestamp", ""),
                }

            except json.JSONDecodeError:
                print(f"Skipping invalid JSON file: {filename}")

# Sort alphabetically by method ID
methods = dict(sorted(methods.items(), key=lambda item: item[1]["id"].lower()))

# Write output
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(methods, f, indent=2)
