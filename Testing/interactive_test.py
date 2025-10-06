"""
Interactive Testing Console
Run this to test your bots interactively with custom inputs
"""

from src.Joe_ai_bot import joe
from src.Sara_ai_bot import sara
from src.Blue_ai_bot import blue
from src.Red_ai_bot import red
from src.Yellow_ai_bot import yellow
from src.White_ai_bot import white

def get_clean_response(response):
    """Extract clean text from bot response"""
    if hasattr(response, 'content'):
        return response.content
    return str(response)

def interactive_console():
    """Interactive testing console"""
    
    bots = {
        '1': ('🟠 Joe (Structured Coach)', joe),
        '2': ('🟡 Sara (Sassy Bestie)', sara), 
        '3': ('🔵 Blue (Reflective Storyteller)', blue),
        '4': ('🔴 Red (Truth-Teller)', red),
        '5': ('💛 Yellow (Cheerleader)', yellow),
        '6': ('⚪ White (Grounding Presence)', white),
        '7': ('All Bots', 'all')
    }
    
    print("=" * 60)
    print("🤖 AI BREAKUP SUPPORT BOTS - INTERACTIVE TESTING")
    print("=" * 60)
    print("Choose a bot to test:")
    for key, (name, _) in bots.items():
        print(f"{key}. {name}")
    print("0. Exit")
    print("-" * 60)
    
    while True:
        choice = input("\nEnter your choice (0-7): ").strip()
        
        if choice == '0':
            print("Goodbye! 👋")
            break
            
        if choice not in bots:
            print("❌ Invalid choice! Please select 0-7.")
            continue
            
        user_input = input("\n💬 Enter your message: ").strip()
        if not user_input:
            print("❌ Please enter a message.")
            continue
            
        print("\n" + "=" * 60)
        
        if choice == '7':  # All bots
            print(f"📝 Testing all bots with: '{user_input}'")
            print("-" * 60)
            
            for bot_name, bot_func in [
                ('🟠 Joe', joe),
                ('🟡 Sara', sara),
                ('🔵 Blue', blue), 
                ('🔴 Red', red),
                ('💛 Yellow', yellow),
                ('⚪ White', white)
            ]:
                try:
                    response = bot_func(user_input)
                    clean_response = get_clean_response(response)
                    print(f"\n{bot_name}: {clean_response}")
                except Exception as e:
                    print(f"\n{bot_name}: ❌ Error - {e}")
                    
        else:  # Single bot
            bot_name, bot_func = bots[choice]
            print(f"📝 Testing {bot_name}")
            print("-" * 60)
            
            try:
                response = bot_func(user_input)
                clean_response = get_clean_response(response)
                print(f"\n💬 Response: {clean_response}")
            except Exception as e:
                print(f"\n❌ Error: {e}")
        
        print("\n" + "=" * 60)
        
        # Ask if they want to continue
        continue_choice = input("\nTest another message? (y/n): ").strip().lower()
        if continue_choice not in ['y', 'yes']:
            print("Thanks for testing! 👋")
            break

def sample_tests():
    """Run some sample tests to demonstrate the bots"""
    
    sample_inputs = [
        "I just saw my ex with someone new and I'm heartbroken",
        "Should I text my ex to try to get back together?", 
        "I made it through the day without crying",
        "I feel like I'll never find love again",
        "I'm so angry at how they treated me"
    ]
    
    print("=" * 60)
    print("🧪 SAMPLE TEST DEMONSTRATIONS")
    print("=" * 60)
    
    for i, test_input in enumerate(sample_inputs, 1):
        print(f"\n📝 Sample {i}: '{test_input}'")
        print("-" * 60)
        
        # Test with 3 most relevant bots for variety
        test_bots = [
            ('🟠 Joe', joe),
            ('🟡 Sara', sara),
            ('🔵 Blue', blue)
        ]
        
        for bot_name, bot_func in test_bots:
            try:
                response = bot_func(test_input)
                clean_response = get_clean_response(response)
                print(f"{bot_name}: {clean_response}")
            except Exception as e:
                print(f"{bot_name}: ❌ Error - {e}")
            print()

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Interactive testing")
    print("2. Sample demonstrations")
    
    mode = input("Enter choice (1-2): ").strip()
    
    if mode == '1':
        interactive_console()
    elif mode == '2':
        sample_tests()
    else:
        print("Invalid choice. Running interactive mode...")
        interactive_console()