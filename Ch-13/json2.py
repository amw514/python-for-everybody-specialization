import json
input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
} ,
    { "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

data = json.loads(input)

print("User count: " , len(data))

for item in data:
    print("Name", item["name"])
    print("Id", item["id"])
    print("Attribute",item["x"])