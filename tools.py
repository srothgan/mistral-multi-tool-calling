
# Dummy methods for tools
def get_weather(location):

    value = {
        "city": location,
        "weather": "sunny",
        "temperature": "22°C"
    }
    return str(value)

def set_temperature(room, temperature):
    value= {
        "status": "success",
        "room": room,
        "temperature": temperature
    }
    return str(value)

def get_temperature(room):
    value= {
        "status": "live",
        "room": room,
        "temperature": "22"
    }
    return str(value)

def control_lights(room, action):
    value = {
        "status": "success",
        "room": room,
        "action": action
    }
    return str(value)

def make_coffee(coffee_type):
    value= {
        "status": "success",
        "coffee_type": coffee_type,
        "coffee_machine": "Nespresso Vertuo"
    }
    return str(value)

def control_music(action, song=None):
    value = {
        "status": "success",
        "action": action,
        "song": song,
        "music_system": "Sonos"
    }
    return str(value)

# Tool list with descriptions for the AI model
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather of a location by calling the weather API. Returns a string with temperature and weather conditions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name to get the weather for.",
                    }
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "set_temperature",
            "description": "Call the smart home temperature endpoint to set the temperature in a room to a given temperature.",
            "parameters": {
                "type": "object",
                "properties": {
                    "room": {
                        "type": "string",
                        "description": "The room in the house where to set the temperature.",
                    },
                    "temperature": {
                        "type": "string",
                        "description": "The Celsius temperature.",
                    }
                },
                "required": ["room", "temperature"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_temperature",
            "description": "Retrieve the current temperature of a specified room from the smart home system.",
            "parameters": {
                "type": "object",
                "properties": {
                    "room": {
                        "type": "string",
                        "description": "The room in the house to get the current temperature for.",
                    }
                },
                "required": ["room"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "control_lights",
            "description": "Control the lights in a specific room, either turning them on or off.",
            "parameters": {
                "type": "object",
                "properties": {
                    "room": {
                        "type": "string",
                        "description": "The room in which to control the lights.",
                    },
                    "action": {
                        "type": "string",
                        "description": "The action to perform on the lights, either 'on' or 'off'.",
                        "enum": ["on", "off"],
                    }
                },
                "required": ["room", "action"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "make_coffee",
            "description": "Prepare a coffee of the specified type using the smart coffee machine.",
            "parameters": {
                "type": "object",
                "properties": {
                    "coffee_type": {
                        "type": "string",
                        "description": "The type of coffee to prepare, e.g., espresso, latte, or cappuccino.",
                    }
                },
                "required": ["coffee_type"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "control_music",
            "description": "Control the music system to play a specific song or stop the current music.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": "The action to perform, either 'play' or 'stop'.",
                        "enum": ["play", "stop"],
                    },
                    "song": {
                        "type": "string",
                        "description": "The name of the song to play (only required when action is 'play').",
                    }
                },
                "required": ["action"],
            },
        },
    }
]
