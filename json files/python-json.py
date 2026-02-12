#Converting the python into json files
import json

x = {
  "name": "sai",
  "age": 22,
  "married": False,
  "lang known": ("python","java"),
  "pets": None,
  "dlproject": [
    {"model": "mobileNet", "acc": 95},
    {"model": "EfficientNet", "acc": 86.9}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = "))) #if we use sort_keys = True - Then the keys are arranged in the alphabetic order

"""{
    "name" = "sai". 
    "age" = 22. 
    "married" = false. 
    "lang known" = [
        "python". 
        "java"
    ]. 
    "pets" = null. 
    "dlproject" = [
        {
            "model" = "mobileNet". 
            "acc" = 95
        }. 
        {
            "model" = "EfficientNet". 
            "acc" = 86.9
        }
    ]
}"""