import os
import requests

GITHUB_API_URL = "https://api.github.com/repos/wso2/api-manager/labels"
ISSUE_BODY_ENV = "ISSUE_BODY"


def get_existing_labels():
    """Return a list of label names in the repository. Fail soft if API is unavailable."""
    labels = []
    try:
        response = requests.get(
            GITHUB_API_URL,
            headers={"Accept": "application/vnd.github.v3+json"},
            timeout=10,
        )
        if response.status_code == 200:
            for label in response.json():
                name = label.get("name")
                if name:
                    labels.append(name)
        else:
            # If label list cannot be fetched, fall back to default label
            print("Missing/Component")
            exit(0)
    except Exception:
        # Network or API error – do not break the workflow
        print("Missing/Component")
        exit(0)
    return labels


def extract_first_non_empty_line(text):
    """Get the first non-empty line from a block of text."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def main():
    all_labels = get_existing_labels()

    issue_body = os.environ.get(ISSUE_BODY_ENV, "")
    if not issue_body:
        print("Missing/Component")
        return

    component_marker = "### Affected Component"
    version_marker = "### Version"

    i = issue_body.find(component_marker)
    j = issue_body.find(version_marker)

    # If markers are missing or in the wrong order, use fallback label
    if i == -1 or j == -1 or j <= i:
        print("Missing/Component")
        return

    # Text between "Affected Component" and "Version" headings
    component_section = issue_body[i + len(component_marker):j].strip()
    component = extract_first_non_empty_line(component_section)
    labels = []

    if component:
        component_label = f"Component/{component}"
        if component_label in all_labels:
            labels.append(component_label)

    # Text after "Version" heading
    version_section = issue_body[j + len(version_marker):].strip()
    version = extract_first_non_empty_line(version_section)

    if component and version:
        affected_label = f"Affected/{component}-{version}"
        if affected_label in all_labels:
            labels.append(affected_label)

    if labels:
        print(",".join(labels))
    else:
        print("Missing/Component")


if __name__ == "__main__":
    main()
