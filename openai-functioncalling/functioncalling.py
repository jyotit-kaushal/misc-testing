import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)


import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)


student_1_description = "David Nguyen is a sophomore majoring in computer science at Stanford University. He is Asian American and has a 3.8 GPA. David is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after graduating."

# A simple prompt to extract information from "student_description" in a JSON format.
prompt1 = f'''
Please extract the following information from the given text and return it as a JSON object:

name
major
school
grades
club

This is the body of text to extract the information from:
{student_1_description}
'''


# Generating response back from gpt-3.5-turbo
openai_response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': prompt_1}]
)

openai_response.choices[0].message.content

'{\n  "name": "David Nguyen",\n  "major": "computer science",\n  "school": "Stanford University",\n  "grades": "3.8 GPA",\n  "club": "Robotics Club"\n}'


import json

# Loading the response as a JSON object
json_response = json.loads(openai_response.choices[0].message.content)
json_response


# {'name': 'David Nguyen',
#  'major': 'computer science',
#  'school': 'Stanford University',
#  'grades': '3.8 GPA',
#  'club': 'Robotics Club'}

student_custom_functions = [
    {
        'name': 'extract_student_info',
        'description': 'Get the student information from the body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person'
                },
                'major': {
                    'type': 'string',
                    'description': 'Major subject.'
                },
                'school': {
                    'type': 'string',
                    'description': 'The university name.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                },
                'club': {
                    'type': 'string',
                    'description': 'School club for extracurricular activities. '
                }
                
            }
        }
    }
]



student_description = [student_1_description,student_2_description]
for i in student_description:
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role': 'user', 'content': i}],
        functions = student_custom_functions,
        function_call = 'auto'
    )

    # Loading the response as a JSON object
    json_response = json.loads(response.choices[0].message.function_call.arguments)
    print(json_response)

custom_functions = [
    {
        'name': 'extract_student_info',
        'description': 'Get the student information from the body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person'
                },
                'major': {
                    'type': 'string',
                    'description': 'Major subject.'
                },
                'school': {
                    'type': 'string',
                    'description': 'The university name.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                },
                'club': {
                    'type': 'string',
                    'description': 'School club for extracurricular activities. '
                }
                
            }
        }
    },
    {
        'name': 'extract_school_info',
        'description': 'Get the school information from the body of the input text',
        'parameters': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the school.'
                },
                'ranking': {
                    'type': 'integer',
                    'description': 'QS world ranking of the school.'
                },
                'country': {
                    'type': 'string',
                    'description': 'Country of the school.'
                },
                'no_of_students': {
                    'type': 'integer',
                    'description': 'Number of students enrolled in the school.'
                }
            }
        }
    }
]








