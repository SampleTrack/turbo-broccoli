import aiohttp
import random

# Fallback content if APIs fail
FALLBACK_QUOTES = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Don't watch the clock; do what it does. Keep going."
]

RIDDLES = [
    {"q": "What has to be broken before you can use it?", "a": "An egg"},
    {"q": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "a": "A candle"},
    {"q": "What month of the year has 28 days?", "a": "All of them"}
]

async def get_motivation_content():
    """Fetches a random quote and an image url."""
    quote = random.choice(FALLBACK_QUOTES)
    # Using a placeholder image service for reliability
    image_url = f"https://picsum.photos/seed/{random.randint(1,1000)}/800/600"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://zenquotes.io/api/random") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    quote = f"“{data[0]['q']}”\n\n— *{data[0]['a']}*"
    except:
        pass
        
    return quote, image_url

async def get_random_riddle():
    riddle = random.choice(RIDDLES)
    return riddle['q'], riddle['a']
