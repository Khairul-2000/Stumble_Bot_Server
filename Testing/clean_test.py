"""
Clean test functions that extract only the response content
"""

from src.Joe_ai_bot import joe
from src.Sara_ai_bot import sara
from src.Blue_ai_bot import blue
from src.Red_ai_bot import red
from src.Yellow_ai_bot import yellow
from src.White_ai_bot import white


def clean_response(response):
    """Extract just the content from the bot response"""
    if hasattr(response, 'content'):
        return response.content
    return str(response)


def test_clean_responses():
    """Test all bots with clean response formatting"""
    
    test_input = "I miss my ex and I don't know how to move forward"
    
    print("=== CLEAN AI BOT RESPONSES ===")
    print(f"Input: '{test_input}'\n")
    
    bots = [
        ("🟠 Joe (Structured Coach)", joe),
        ("🟡 Sara (Sassy Bestie)", sara),
        ("🔵 Blue (Reflective Storyteller)", blue),
        ("🔴 Red (Truth-Teller)", red),
        ("💛 Yellow (Cheerleader)", yellow),
        ("⚪ White (Grounding Presence)", white)
    ]
    
    for name, bot_func in bots:
        try:
            response = bot_func(test_input)
            clean_text = clean_response(response)
            print(f"{name}:")
            print(f'"{clean_text}"\n')
        except Exception as e:
            print(f"{name}: Error - {e}\n")


def test_different_scenarios():
    """Test bots with different emotional scenarios"""
    
    scenarios = [
        {
            "title": "Fresh Heartbreak",
            "input": "They just broke up with me and I'm completely devastated"
        },
        {
            "title": "Anger Phase", 
            "input": "I'm so angry at them for wasting my time and lying to me"
        },
        {
            "title": "Seeking Closure",
            "input": "I keep wondering what I did wrong and if there's something I could have done differently"
        },
        {
            "title": "Moving Forward",
            "input": "I think I'm ready to start dating again but I'm scared of getting hurt"
        }
    ]
    
    print("=== SCENARIO-BASED TESTING ===\n")
    
    for scenario in scenarios:
        print(f"📖 SCENARIO: {scenario['title']}")
        print(f"Input: '{scenario['input']}'")
        print("-" * 60)
        
        # Test with most relevant bots for each scenario
        if "devastated" in scenario['input'] or "heartbreak" in scenario['title'].lower():
            # Fresh wounds - White, Blue, Sara
            relevant_bots = [("White", white), ("Blue", blue), ("Sara", sara)]
        elif "angry" in scenario['input']:
            # Anger phase - Sara, Red, Blue  
            relevant_bots = [("Sara", sara), ("Red", red), ("Blue", blue)]
        elif "wondering" in scenario['input'] or "closure" in scenario['title'].lower():
            # Seeking meaning - Blue, Joe, Sara
            relevant_bots = [("Blue", blue), ("Joe", joe), ("Sara", sara)]
        elif "ready" in scenario['input'] or "moving forward" in scenario['title'].lower():
            # Moving forward - Joe, Yellow, Blue
            relevant_bots = [("Joe", joe), ("Yellow", yellow), ("Blue", blue)]
        else:
            relevant_bots = [("Joe", joe), ("Sara", sara), ("Blue", blue)]
        
        for name, bot_func in relevant_bots:
            try:
                response = bot_func(scenario['input'])
                clean_text = clean_response(response)
                print(f"{name}: {clean_text}")
            except Exception as e:
                print(f"{name}: Error - {e}")
        
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    test_clean_responses()
    print("\n" + "=" * 60 + "\n")
    test_different_scenarios()