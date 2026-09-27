from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from google.adk import Agent

def get_current_time(city: str, timezone: str) -> str:
    """Returns the current local time in a city.

    Args:
        city: Name of the city, e.g. "Budapest".
        timezone: IANA timezone identifier of the city,
            e.g. "Europe/Budapest", "America/New_York", "Asia/Tokyo".
    """
    try:
        now = datetime.now(ZoneInfo(timezone))
        return f"The current local time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S')}."
    except (ZoneInfoNotFoundError, ValueError):
        return f"Error: Unknown timezone '{timezone}' for city '{city}'."

root_agent = Agent(
    model="ollama_chat/llama3.2-time",
    name="time_agent",
    description="An agent that provides the exact local time in any city.",
    instruction=(
        "You are a precise time assistant. When the user asks for the time in a city, "
        "you must invoke the get_current_time tool with the correct city and its IANA timezone."
    ),
    tools=[
        get_current_time,
    ],
)

import litellm

litellm.register_model(model_cost={
    "ollama_chat/llama3.2-time": {
        "supports_function_calling": True
    }
})