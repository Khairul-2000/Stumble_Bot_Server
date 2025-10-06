"""
Test cases for AI Bots - Breakup/Healing Support System
Each bot has a specific role in the healing journey with unique personalities
"""

from src.Joe_ai_bot import joe
from src.Sara_ai_bot import sara
from src.Blue_ai_bot import blue
from src.Red_ai_bot import red
from src.Yellow_ai_bot import yellow
from src.White_ai_bot import white


def test_all_bots():
    """Test all bots with various scenarios"""
    
    # Test cases for different healing stages and emotional states
    test_cases = [
        # Fresh wounds / Initial heartbreak
        {
            "input": "I just found out my ex is dating someone new and I feel destroyed",
            "scenario": "Fresh heartbreak - seeing ex with someone new",
            "expected_bots": ["white", "blue", "sara"]
        },
        
        # Rumination and obsessive thoughts
        {
            "input": "I can't stop thinking about what went wrong. I keep replaying our last conversation over and over",
            "scenario": "Rumination and obsessive thinking",
            "expected_bots": ["red", "joe", "white"]
        },
        
        # Temptation to contact ex
        {
            "input": "I really want to text my ex right now. Should I reach out?",
            "scenario": "Temptation to contact ex",
            "expected_bots": ["red", "sara", "joe"]
        },
        
        # Small progress/wins
        {
            "input": "I went a whole day without checking their social media",
            "scenario": "Small win in healing process",
            "expected_bots": ["yellow", "joe", "sara"]
        },
        
        # Panic/anxiety moments
        {
            "input": "I'm having a panic attack thinking about being alone forever",
            "scenario": "Panic attack about future",
            "expected_bots": ["white", "blue", "sara"]
        },
        
        # Self-doubt and shame
        {
            "input": "Maybe I wasn't good enough for them. I feel like such a failure",
            "scenario": "Self-doubt and shame spirals",
            "expected_bots": ["sara", "blue", "yellow"]
        },
        
        # Practical daily struggles
        {
            "input": "I can't focus on work and my routine is completely messed up since the breakup",
            "scenario": "Daily routine disruption",
            "expected_bots": ["joe", "yellow", "red"]
        },
        
        # Looking for meaning/growth
        {
            "input": "I'm trying to understand what this relationship taught me",
            "scenario": "Seeking meaning and growth",
            "expected_bots": ["blue", "joe", "yellow"]
        },
        
        # Social media stalking
        {
            "input": "I've been scrolling through their Instagram for hours",
            "scenario": "Social media stalking behavior",
            "expected_bots": ["red", "sara", "joe"]
        },
        
        # Physical symptoms of heartbreak
        {
            "input": "My chest hurts so much, I can barely breathe when I think about them",
            "scenario": "Physical symptoms of heartbreak",
            "expected_bots": ["white", "blue", "sara"]
        },
        
        # Moving forward uncertainty
        {
            "input": "I don't know how to start dating again or if I even want to",
            "scenario": "Uncertainty about moving forward",
            "expected_bots": ["blue", "joe", "yellow"]
        },
        
        # Anger phase
        {
            "input": "I'm so angry at how they treated me. They wasted my time!",
            "scenario": "Anger phase of healing",
            "expected_bots": ["sara", "red", "blue"]
        }
    ]
    
    print("=== AI BOTS TEST CASES ===\n")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"TEST CASE {i}: {test_case['scenario']}")
        print(f"INPUT: '{test_case['input']}'")
        print("-" * 80)
        
        # Test each bot
        bots = {
            "Joe (🟠 Structured Coach)": joe,
            "Sara (🟡 Sassy Bestie)": sara,
            "Blue (🔵 Reflective Storyteller)": blue,
            "Red (🔴 Truth-Teller)": red,
            "Yellow (💛 Cheerleader)": yellow,
            "White (⚪ Grounding Presence)": white
        }
        
        for bot_name, bot_function in bots.items():
            try:
                print(f"\n{bot_name} Response:")
                response = bot_function(test_case['input'])
                print(f"'{response}'\n")
            except Exception as e:
                print(f"Error with {bot_name}: {e}\n")
        
        print("=" * 80)
        print()


def test_specific_scenarios():
    """Test specific scenarios for each bot's expertise"""
    
    print("\n=== SPECIFIC BOT SCENARIO TESTS ===\n")
    
    # Joe Bot - Routine and structure tests
    joe_tests = [
        "I don't know how to get back to normal after this breakup",
        "What should I do with my daily routine now that they're gone?",
        "I keep breaking down at work, how do I stay focused?"
    ]
    
    print("JOE BOT (Structured Coach) Tests:")
    for test in joe_tests:
        print(f"Input: {test}")
        try:
            response = joe(test)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
    # Sara Bot - Sassy validation tests  
    sara_tests = [
        "They told me I was 'too much' and now I feel ashamed",
        "Should I change myself to win them back?",
        "I feel so pathetic for missing them this much"
    ]
    
    print("\nSARA BOT (Sassy Bestie) Tests:")
    for test in sara_tests:
        print(f"Input: {test}")
        try:
            response = sara(test)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
    # White Bot - Panic/grounding tests
    white_tests = [
        "I can't breathe, everything feels overwhelming",
        "I'm having a complete meltdown right now",
        "My anxiety is through the roof thinking about them"
    ]
    
    print("\nWHITE BOT (Grounding Presence) Tests:")
    for test in white_tests:
        print(f"Input: {test}")
        try:
            response = white(test)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")
    
    # Red Bot - Tough love tests
    red_tests = [
        "Maybe if I just explain my feelings one more time they'll come back",
        "I've been checking their location all day",
        "What if I drive by their house just to see if they're home?"
    ]
    
    print("\nRED BOT (Truth-Teller) Tests:")
    for test in red_tests:
        print(f"Input: {test}")
        try:
            response = red(test)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


def quick_test():
    """Quick test with simple inputs for all bots"""
    
    simple_input = "I miss my ex so much it hurts"
    
    print("=== QUICK TEST - Same Input to All Bots ===")
    print(f"Input: '{simple_input}'\n")
    
    bots = [
        ("Joe", joe),
        ("Sara", sara), 
        ("Blue", blue),
        ("Red", red),
        ("Yellow", yellow),
        ("White", white)
    ]
    
    for name, bot_func in bots:
        try:
            print(f"{name} Bot: {bot_func(simple_input)}")
        except Exception as e:
            print(f"{name} Bot Error: {e}")
        print()


if __name__ == "__main__":
    # Run quick test first
    quick_test()
    
    # Run comprehensive tests
    test_all_bots()
    
    # Run specific scenario tests
    test_specific_scenarios()