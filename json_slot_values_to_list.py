import json

ALEXA_INTERACTION_JSON_PATH = 'input/alexa_interaction.json'
ALEXA_SLOTS_PATH = '../custom/alexa/slot_types.py'


def generate_slot_list_from_alexa_json():
    python_out_file = open(ALEXA_SLOTS_PATH, 'w+')

    with open(ALEXA_INTERACTION_JSON_PATH) as json_in_file:
        data = json.load(json_in_file)

        for types in data['interactionModel']['languageModel']['types']:
            python_out_file.write((types['name']) + ' = [')

            slot_values_string = ''

            for value in types['values']:
                slot_values_string += '"' + value['name']['value'].lower() + '",'

            python_out_file.write(slot_values_string[:-1])
            python_out_file.write(']\n')
