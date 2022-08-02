from stix2.v21 import (Bundle)

for obj in bundle.objects:
    if obj == identity:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print(f"ID: {obj.id}")
        print(f"Created: {str(obj.created)}")
        print(f"Modified: {str(obj.modified)}")
        print(f"Name: {obj.name}")
        print(f"Identity Class: {obj.identity_class}")
        print(f"Sectors: {str(obj.sectors)}")
        print(f"Contact Information: {obj.contact_information}")

    elif obj == indicator:
        print("------------------")
        print("== INDICATOR ==")
        print("------------------")
        print(f"ID: {obj.id}")
        print(f"Created: {str(obj.created)}")
        print(f"Modified: {str(obj.modified)}")
        print(f"Name: {obj.name}")
        print(f"Type: {obj.type}")
        print(f"Indicator Types: {str(obj.indicator_types)}")
        print(f"Pattern: {obj.pattern}")
        print(f"Pattern Type: {obj.pattern_type}")
        print(f"Valid From: {str(obj.valid_from)}")

    elif obj in [marking_def_amber, marking_def_statement]:
        print("------------------")
        print("== MARKING DEFINITION ==")
        print("------------------")
        print(f"ID: {obj.id}")
        print(f"Type: {obj.type}")
        print(f"Created: {str(obj.created)}")
        print(f"Definition Type: {obj.definition_type}")
        print(f"Definition: {str(obj.definition)}")
