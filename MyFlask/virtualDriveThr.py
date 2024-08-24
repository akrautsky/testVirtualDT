import os
#from dotenv import load_dotenv
from vapi_python import Vapi
import requests

# Load environment variables from .env file
#load_dotenv()

# Get VAPI key from environment variables
#vapi_key = os.getenv("1f9872bd-686a-4af1-99d0-1d305f2c5b33")

# Initialize the Vapi object    
vapi = Vapi(api_key='38cbc199-f6b3-4aa1-a83f-ce521273e75b')



# Define menu items
menu_items = [
    {'id': 1,  'category': 'Appetizers', 'item_name': 'Spring Rolls', 'price': 5.00},
    {'id': 2, 'category': 'Appetizers', 'item_name': 'Garlic Bread', 'price': 4.00},
    {'id': 3, 'category': 'Smoothies', 'item_name': 'Green Detox', 'price': 7.00},
    {'id': 4, 'category': 'Smoothies', 'item_name': 'Banana Honey', 'price': 6.00},
    {'id': 5, 'category': 'Pizzas', 'item_name': 'Margherita', 'price': 12.00},
    {'id': 6, 'category': 'Pizzas', 'item_name': 'Pepperoni', 'price': 14.00}
]

items_names = ['Spring Rolls', 'Garlic Bread', 'Green Detox', 'Banana Honey', 'Margherita', 'Pepperoni']

# Define JSON payload
# json_payload = [
#     {'item': 1, 'quantity': 2},
#     {'item': 7, 'quantity': 1},
#     {'item': 10, 'quantity': 1}
# ]

# Define URL and payload for the VAPI request
url = "https://api.vapi.ai/assistant"


# to-do : when someone ask for the menu we are switchin the model to 3.5 turbo to have it in the prompt.


bot_prompt = f'''
                You are a calm and welcoming phone answering bot, well-versed with menu items and prices. Greet users casually unless interrupted. If silence exceeds 4 seconds after the greeting, offer to read the menu. Only read the menu if asked or during extended silence. After the user finishes ordering, ask for confirmation and read the order in a human-like manner without numbering. Mention quantity only if more than one.

                Instructions:

                Order Processing and Confirmation:
                1. Listen carefully to the user's order and identify the items by matching them to the {items_names} list.
                2. For each item mentioned by the user, retrieve the correct `item_name`, `item_id` from {menu_items}.
                3. If there is a spelling mistake or different accent, look up the key values in {items_names} and match it with the correct entry in {menu_items}.
                4. After identifying all items in the user's order, combine them into a single JSON array in the format:
                    Order=[{{"item": "item_name", "item_id": id, "quantity": quantity}}, ...]
                5. Always ensure that the JSON response is an array of objects, even if there is only one item.
                6. Call the processOrder function with the final combined JSON input after the user confirms their order. Make sure to include all ordered items in a single call.

                Tip and Total Adjustment:
                After providing the order total, ask if the customer would like to leave a tip or round off the total to the nearest dollar. Based on their response, create a JSON response like `{{"Tip": 5, "roundOffTotal": true, "orderTotal": 31}}`. If they decline, set `"Tip"` to 0 and `"roundOffTotal"` to false. Only call the `addTip` function if a tip is given or the total is rounded off.

                Example Interaction:
                User: Hi, I'd like to place an order.
                System: Hello! What would you like to order today?
                User: I'll have two Margherita pizzas and two Spring Rolls.
                System: Got it. Two Margherita pizzas and two Spring Rolls. Is that correct?
                User: Yes.
                System: Great! Let me confirm your order.

                JSON Output Format after Confirmation:
                Order=[{{"item": "Margherita pizza", "item_id":9, "quantity": 2}}, {{"item": "Spring Rolls", "item_id":1, "quantity": 2}}]

                Example Tip Interaction:
                System: Your order total is $31. Would you like to leave a tip or round off the total to the nearest dollar?
                User: Yes, add $5 tip.
                JSON Output Format: `{{"Tip": 5, "roundOffTotal": false, "orderTotal": 31}}`

                User: No, just round off the total.
                JSON Output Format: `{{"Tip": 0, "roundOffTotal": true, "orderTotal": 31}}`

                User: No, thank you.
                JSON Output Format: `{{"Tip": 0, "roundOffTotal": false, "orderTotal": 31}}`

                Important: Ensure that the JSON response always follows the specified format strictly. The format must be an array of objects, each with "item", "item_id", "cat_id", and "quantity" keys. If there is any ambiguity, always look up the correct values in {menu_items}.
            '''



payload = {
    "transcriber": {
        "provider": "deepgram",
        "model": "nova-2",
        "language": "en",
        "smartFormat": True
    },
    "model": {
        "messages": [
            {
                "content": (f"{bot_prompt}"
                ),
                "role": "assistant"
            }
        ],
        "provider": "openai",
        "model": "gpt-4",
        "tools": [
            {
                "async": False,
                "messages": [
                    {
                        "type": "request-start",
                        "content": "Adding tip to the order"
                    }
                ],
                "type": "function",
                "function": {
                    "name": "addTip",
                    "description": "This function will take a json object as input with tip amount and roundoff total and returnt he final total",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "tip": {
                                "type": "object",
                                "properties": {
                                    "tip": {"type": "integer"},
                                    "roundofftotal": {"type": "boolean"},
                                    "ordertotal": {"type": "integer"}
                                }
                            }
                        },
                        "required": ["order"]
                    }
                },
                "server": {
                    "url": "https://1def-2603-9000-f801-977f-5d1-8a36-7a44-bf22.ngrok-free.app/api/processMyTip/processMyTip",
                    "timeoutSeconds": 20
                }
            },
            {
                "async": False,
                "messages": [
                    {
                        "type": "request-start",
                        "content": "Confirming your order, thank you for your patience"
                    }
                ],
                "type": "function",
                "function": {
                    "name": "processorder",
                    "description": "This function will take a json object as input and process the result and return the result",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "order": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "integer"},
                                    "item": {"type": "string"},
                                    "quantity": {"type": "integer"}
                                }
                            }
                        },
                        "required": ["order"]
                    }
                },
                "server": {
                    "url": "https://1def-2603-9000-f801-977f-5d1-8a36-7a44-bf22.ngrok-free.app/api/processMyOrder/processMyOrder",
                    "timeoutSeconds": 20
                }
            }
        ],
        "temperature": 1,
        "knowledgeBase": {
            "provider": "canonical",
            "fileIds": ["openai"]
        }
    },
    "voice": {
        "inputPreprocessingEnabled": True,
        "inputReformattingEnabled": True,
        "provider": "deepgram",
        "voiceId": "luna"
    },
    "firstMessageMode": "assistant-speaks-first",
    "recordingEnabled": False,
    "silenceTimeoutSeconds": 15,
    "responseDelaySeconds": 1,
    "voicemailDetection": {"provider": "twilio"},
    "analysisPlan": {"structuredDataSchema": {"type": "string"}}
}

# Define request headers
headers = {
    "Authorization": "Bearer 81839410-9f19-41aa-96ae-2822469ecbbe",
    "Content-Type": "application/json"
}

# Send POST request to VAPI
#response = requests.post(url, json=payload, headers=headers)

# Get and print the assistant ID from the response
#assistant_id = response.json().get('id')
#print(assistant_id)

# Start the assistant with the obtained ID
vapi.start(assistant= payload)
