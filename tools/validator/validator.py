import json
import glob
import sys
import os.path
from PIL import Image

# TODO: If @petriw adds $schema to the JSON, use it to validate

main_key_fields = [
    'checklistText',
    'Group',
    'Images',
    'Name',
    'ProjectName',
    'Side',
    'SortPriority',
    'Spacecraft',
    'Steps',
    'AutoGenerate'
]

main_key_fields_ignorable = [
    'AutoGenerate'
]

main_key_types = {
    'checklistText': str,
    'Group': str,
    'Images': list,
    'Name': str,
    'ProjectName': str,
    'Side': int,
    'SortPriority': int,
    'Spacecraft': int,
    'Steps': list,
    'AutoGenerate': bool
}

step_key_fields = ['Program', 'Type', 'SetID', 'ToPosID', 'Text', 'Description']

step_key_fields_ignorable = ['Description']

# TODO: step_key_types

image_key_fields = ['Name', 'Position', 'Size']

image_key_types = {'Name': str, 'Position': dict, 'Size': dict}

if not all([field in main_key_types for field in main_key_fields]):
    print('Self test failed, main field-type unknown')

all_valid = True
for checklist in glob.glob('*/*/checklist.json'):
    if ' ' in checklist:
        print(checklist, 'FILENAME', 'HAS SPACE (OPTIONAL)')
        # file_ok = False
        # all_valid = False
    j = json.load(open(checklist))
    file_ok = True
    for main_key in main_key_fields:
        if main_key not in j.keys():
            if main_key in main_key_fields_ignorable:
                print(checklist, 'MAIN', main_key, 'MISSING (OPTIONAL)')
            else:
                print(checklist, 'MAIN', main_key, 'MISSING')
                file_ok = False
                all_valid = False
    for main_key in j.keys():
        if main_key not in main_key_fields:
            print(checklist, 'MAIN', main_key, 'Invalid (unknown) key')
            file_ok = False
            all_valid = False
        if type(j[main_key]) != main_key_types[main_key]:
            print(checklist, 'MAIN', main_key, 'Key has wrong type')
            file_ok = False
            all_valid = False
    for step in j['Steps']:
        if step is None:
            # TODO: Ask @petriw if this is valid
            continue
        for step_key in step_key_fields:
            if step_key not in step.keys():
                if step_key in step_key_fields_ignorable:
                    print(checklist, 'STEP', step_key, 'MISSING (OPTIONAL)')
                else:
                    print(checklist, 'STEP', step_key, 'MISSING')
                    file_ok = False
                    all_valid = False
            if step_key not in step_key_fields:
                print(checklist, 'STEP', step_key, 'Invalid (unknown) key')
                file_ok = False
                all_valid = False
        for step_key in step.keys():
            # TODO: Add type-validation for step-keys. One issue is that NULL appears to be a valid value for Text
            # if type(step_key) not in step_key_types[step_key]:
            #     print(checklist, 'STEP', step_key, 'Key has wrong type')
            #     file_ok = False
            #     all_valid = False
            pass
    for image in j['Images']:
        for image_key in image_key_fields:
            if image_key not in image.keys():
                print(checklist, 'IMAGE', image_key, 'MISSING')
                file_ok = False
                all_valid = False
            if image_key not in image_key_fields:
                print(checklist, 'IMAGE', image_key, 'Invalid (unknown) key')
                file_ok = False
                all_valid = False
            if type(image[image_key]) != image_key_types[image_key]:
                print(checklist, 'IMAGE', image_key, 'Key has wrong type')
                file_ok = False
                all_valid = False
        image_path = os.path.normpath(
            os.path.join(
                checklist,
                '..',
                image['Name']))
        if not os.path.isfile(image_path):
            print(checklist, 'IMAGE', image_path, 'File not found')
            file_ok = False
            all_valid = False
        try:
            with Image.open(image_path) as im:
                pass  # ATM, just "this is a valid image" is enough
        except:
            file_ok = False
            all_valid = False

sys.exit(0 if all_valid else -1)
