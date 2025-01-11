import json
import functools
import os
from mistralai import Mistral
from dotenv import load_dotenv

from tools import tools
from tools import (
    get_weather, 
    set_temperature, 
    get_temperature,
    control_lights,
    make_coffee,
    control_music)

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

model = "mistral-large-latest"

names_to_functions = {
    'get_weather': functools.partial(get_weather),
    'set_temperature': functools.partial(set_temperature),
    'get_temperature': functools.partial(get_temperature),
    'control_lights': functools.partial(control_lights),
    'make_coffee': functools.partial(make_coffee),
    'control_music': functools.partial(control_music)
}

def system_prompt(question):
    system = """
        You are named Max, a smart home assistant. You are designed to help users with their daily tasks.
       
        You help the user answer questions and perform tasks related to the smart home system.

        The user questions is:
        {question}
    """
    return system.format(question=question)


def generate_response(question):
    messages = [{"role": "user", "content": system_prompt(question)}]
    
    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    
    if response.choices[0].message.tool_calls:
        # Handle tool call
        messages.append({
            "role": "assistant",
            "content": None,
            "tool_calls": response.choices[0].message.tool_calls
        })
        
        tool_call = response.choices[0].message.tool_calls[0]
        function_name = tool_call.function.name
        function_params = json.loads(tool_call.function.arguments)
        print("function_name: ", function_name, "\nfunction_params: ", function_params)
        
        function_result = names_to_functions[function_name](**function_params)
        # Add tool response to messages
        messages.append({
            "role": "tool",
            "name": function_name,
            "content": function_result,
            "tool_call_id": tool_call.id
        })

        response = client.chat.complete(
            model=model, 
            messages=messages
        )
        return response.choices[0].message.content
    else: 
        messages.append({
            "role": "assistant",
            "content": response.choices[0].message.content,
            "tool_calls": None
        })
        return response.choices[0].message.content
    

if __name__ == "__main__":
    # Process different user inputs
    inputs = [
        # get_weather
        "What's the weather like in Berlin?",
        "Can you tell me the current weather in New York?",

        # set_temperature
        "Set the living room temperature to 22°C.",
        "Can you adjust the bedroom temperature to 25°C?",

        # get_temperature
        "What's the current temperature in the kitchen?",
        "Can you check the temperature in the bedroom?",

        # control_lights
        "Turn on the lights in the kitchen.",
        "Can you switch off the bedroom lights?",

        # make_coffee
        "Can you make me an espresso?",
        "Prepare a latte for me.",

        # control_music
        "Play 'Bohemian Rhapsody'.",
        "Can you stop the music?",

        # Others
        "What's your name?",
        "How are you doing?",
    ]



    for user_input in inputs:
        print("\nUser:", user_input)
        response = generate_response(question=user_input)
        print("Response:", response)
        print("#" * 50)
