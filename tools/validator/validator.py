import json, glob, sys

# TODO: If @petriw adds $schema to the JSON, use it to validate

main_key_fields = ['Spacecraft', 'ProjectName', 'Group', 'Name', 'Side', 'SortPriority', 'checklistText', 'Steps', 'Images']

main_key_types = {
    'Spacecraft': int,
    'ProjectName': str,
    'Group': str,
    'Name': str,
    'Side': int,
    'SortPriority': int,
    'checklistText': str,
    'Steps': list,
    'Images': list
}

step_key_fields = ['Program', 'Type', 'SetID', 'ToPosID', 'Text']

image_key_fields = ['Name', 'Position', 'Size']

image_key_types = {'Name': str, 'Position': dict, 'Size': dict}

if not all([field in main_key_types for field in main_key_fields]):
    print('Self test failed, main field-type unknown')

all_valid = True
for checklist in glob.glob('*/*/checklist.json'):
    if ' ' in checklist:
        print(checklist, 'FILENAME', 'HAS SPACE')
        file_ok = False
        all_valid = False
    j = json.load(open(checklist))
    file_ok = True
    for main_key in main_key_fields:
        if main_key not in j.keys():
            print(checklist, 'MAIN', main_key, 'MISSING')
            file_ok = False
            all_valid = False
    for main_key in j.keys():
        if main_key not in main_key_fields:
            print(checklist, 'MAIN', main_key, 'Invalid key')
            file_ok = False
            all_valid = False
        if type(j[main_key]) != main_key_types[main_key]:
            print(checklist, 'MAIN', main_key, 'Key has wrong type')
            file_ok = False
            all_valid = False
    if 'Steps' in j.keys():
        for step in j['Steps']:
            if step is None:
                # TODO: Ask @petriw if this is valid
                continue
            for step_key in step_key_fields:
                if step_key not in step.keys():
                    print(checklist, 'STEP', step_key, 'MISSING')
                    file_ok = False
                    all_valid = False
            for step_key in step.keys():
                if step_key not in step_key_fields:
                    print(checklist, 'STEP', step_key, 'Invalid key')
                    file_ok = False
                    all_valid = False
                # TODO: Add type-validation for step-keys. One issue is that NULL appears to be a valid value for Text
    if 'Images' in j.keys():
        for image in j['Images']:
            for image_key in image_key_fields:
                if image_key not in image.keys():
                    print(checklist, 'IMAGE', image_key, 'MISSING')
                    file_ok = False
                    all_valid = False
                if type(image[image_key]) != image_key_types[image_key]:
                    print(checklist, 'IMAGE', image_key, 'Invalid key')
                    file_ok = False
                    all_valid = False

                    
sys.exit(0 if all_valid else -1)
            