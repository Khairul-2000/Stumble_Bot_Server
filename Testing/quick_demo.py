"""
Quick Demo - Test AI Bots with Sample Inputs
Run this to see how each bot responds to the same breakup scenario
"""

from src.Joe_ai_bot import joe
from src.Sara_ai_bot import sara
from src.Blue_ai_bot import blue
from src.Red_ai_bot import red
from src.Yellow_ai_bot import yellow
from src.White_ai_bot import white


def demo_all_bots():
    """Demo all bots with a common breakup scenario"""
    
    # Sample input that would trigger different bot personalities
    sample_input = "I saw my ex with someone new on social media and now I can't stop crying. I feel like I'll never get over this."
    
    print("=" * 60)
    print("AI BREAKUP SUPPORT BOTS DEMO")
    print("=" * 60)
    print(f"User Input: '{sample_input}'")
    print("=" * 60)
    
    # Test each bot
    bots = [
        ("🟠 JOE (Structured Coach)", joe, "Provides routine-based guidance and steady progress"),
        ("🟡 SARA (Sassy Bestie)", sara, "Protective friend with humor and sass"),  
        ("🔵 BLUE (Reflective Storyteller)", blue, "Finds meaning through reflection and metaphors"),
        ("🔴 RED (Truth-Teller)", red, "Direct tough love to break unhealthy loops"),
        ("💛 YELLOW (Cheerleader)", yellow, "Celebrates small wins with enthusiasm"),
        ("⚪ WHITE (Grounding Presence)", white, "Provides calm and mindfulness in distress")
    ]
    
    for name, bot_func, description in bots:
        print(f"\n{name}")
        print(f"Role: {description}")
        print("-" * 50)
        
        try:
            response = bot_func(sample_input)
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")
        
        print()


def demo_specific_scenarios():
    """Demo bots with their specialized scenarios"""
    
    scenarios = [
        {
            "title": "🚨 PANIC MOMENT",
            "input": "I'm having a panic attack thinking about being alone forever",
            "best_for": "White Bot (Grounding)",
            "test_bot": white
        },
        {
            "title": "💔 TEMPTATION TO CONTACT EX", 
            "input": "I really want to text my ex right now asking if we can try again",
            "best_for": "Red Bot (Truth-Telling)",
            "test_bot": red
        },
        {
            "title": "🎉 SMALL VICTORY",
            "input": "I actually went a whole day without checking their Instagram",
            "best_for": "Yellow Bot (Celebration)",
            "test_bot": yellow
        },
        {
            "title": "😢 SHAME SPIRAL",
            "input": "I feel so pathetic and embarrassing for how much I miss them",
            "best_for": "Sara Bot (Validation)",
            "test_bot": sara
        },
        {
            "title": "🔄 ROUTINE BREAKDOWN",
            "input": "My whole daily routine is messed up since the breakup, I can't focus on anything",
            "best_for": "Joe Bot (Structure)",
            "test_bot": joe
        },
        {
            "title": "🤔 SEEKING MEANING",
            "input": "I'm trying to understand what this painful experience is supposed to teach me",
            "best_for": "Blue Bot (Reflection)",
            "test_bot": blue
        }
    ]
    
    print("\n" + "=" * 60)
    print("SPECIALIZED SCENARIO DEMOS")
    print("=" * 60)
    
    for scenario in scenarios:
        print(f"\n{scenario['title']}")
        print(f"Scenario: {scenario['input']}")
        print(f"Best suited for: {scenario['best_for']}")
        print("-" * 50)
        
        try:
            response = scenario['test_bot'](scenario['input'])
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")
        
        print()


if __name__ == "__main__":
    # Run the main demo
    demo_all_bots()
    
    # Run specialized scenarios
    demo_specific_scenarios()
    
    print("=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)
    print("\nTo run more tests:")
    print("- python test_cases.py (comprehensive tests)")
    print("- python simple_tests.py (individual bot tests)")
    print("- python quick_demo.py (this demo)")