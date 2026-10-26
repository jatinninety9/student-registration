
from html.parser import HTMLParser

class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.current = []
            self.forms.append(self.current)

        elif self.current is not None:
            self.current.append((tag, attrs))

    def handle_endtag(self, tag):
        if tag == "form":
            self.current = None


with open("index.html", encoding="utf-8") as f:
    html = f.read()

parser = FormParser()
parser.feed(html)

assert parser.forms, "Form missing"
print("PASS: Registration form exists")

fields = parser.forms[0]

for field in ["name", "roll", "email", "course"]:
    assert any(
        attrs.get("id") == field
        for tag, attrs in fields
        if tag in ["input", "select"]
    ), f"{field} field missing"

    print(f"PASS: {field} field exists")

assert any(
    (tag == "button" and attrs.get("type") == "submit")
    or (tag == "input" and attrs.get("type") == "submit")
    for tag, attrs in fields
), "Submit button missing"

print("PASS: Submit button exists")
print("All tests passed!")
