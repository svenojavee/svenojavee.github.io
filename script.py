# pretty_html_table_generator.py

data = [
    {"Name": "Alice", "Age": 30, "City": "Zurich"},
    {"Name": "Bob", "Age": 25, "City": "Geneva"},
    {"Name": "Charlie", "Age": 35, "City": "Basel"}
]

# Create HTML table with styles
html = """<html>
<head>
    <title>Styled HTML Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }
        h2 {
            color: #333;
        }
        table {
            border-collapse: collapse;
            width: 60%;
            background-color: #fff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        th, td {
            text-align: left;
            padding: 12px 15px;
        }
        th {
            background-color: #007ACC;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #e8f0fe;
        }
    </style>
</head>
<body>
    <h2>User Data Table</h2>
    <table>
        <tr>
            <th>Name</th><th>Age</th><th>City</th>
        </tr>"""

for row in data:
    html += f"<tr><td>{row['Name']}</td><td>{row['Age']}</td><td>{row['City']}</td></tr>"

html += """
    </table>
</body>
</html>"""

# Save to file
with open("styled_output.html", "w") as f:
    f.write(html)

