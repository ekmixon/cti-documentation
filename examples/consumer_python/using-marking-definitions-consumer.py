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
        print(f"Contact Information: {obj.contact_information}")
        print(f"Sectors: {str(obj.sectors)}")

    elif obj == indicator:
        print("------------------")
        print("== INDICATOR ==")
        print("------------------")
        print(f"ID: {obj.id}")
        print(f"Created: {str(obj.created)}")
        print(f"Modified: {str(obj.modified)}")
        print(f"Created by Ref: {obj.created_by_ref}")
        print(f"Name: {obj.name}")
        print(f"Indicator Types: {obj.indicator_types[0]}")
        print(f"Pattern: {obj.pattern}")
        print(f"Valid From: {str(obj.valid_from)}")
        print(f"Object Marking Refs: {str(obj.object_marking_refs)}")

    elif obj in [marking_def_amber, marking_def_statement]:
        print("------------------")
        print("== MARKING DEFINITION ==")
        print("------------------")
        print(f"ID: {obj.id}")
        print(f"Created: {str(obj.created)}")
        print(f"Definition Type: {obj.definition_type}")
        print(f"Definition: {str(obj.definition)}")
