"""
Simple individual test functions for each AI bot
Run specific bots with custom inputs for testing
"""

from src.Joe_ai_bot import joe
from src.Sara_ai_bot import sara  
from src.Blue_ai_bot import blue
from src.Red_ai_bot import red
from src.Yellow_ai_bot import yellow
from src.White_ai_bot import white


def test_joe():
    """Test Joe Bot - Structured Nordic mentor"""
    print("=== Testing Joe Bot (Structured Coach) ===")
    
    test_inputs = [
        "I don't know how to structure my day anymore",
        "I keep falling back into old patterns",
        "Help me build a healing routine",
        "I made progress but then had a setback",
        "How do I stay consistent with self-care?"
    ]
    
    for input_text in test_inputs:
        print(f"\nInput: {input_text}")
        print(f"Joe: {joe(input_text)}")
        print("-" * 50)


def test_sara():
    """Test Sara Bot - Sassy protective bestie"""
    print("=== Testing Sara Bot (Sassy Bestie) ===")
    
    test_inputs = [
        "I feel like I wasn't good enough for them",
        "Maybe I should change to win them back", 
        "They called me clingy and now I feel ashamed",
        "I keep blaming myself for everything",
        "Am I being too dramatic about this breakup?"
    ]
    
    for input_text in test_inputs:
        print(f"\nInput: {input_text}")
        print(f"Sara: {sara(input_text)}")
        print("-" * 50)


def test_blue():
    """Test Blue Bot - Reflective storyteller"""
    print("=== Testing Blue Bot (Reflective Storyteller) ===")
    
    test_inputs = [
        "I'm trying to understand what this relationship meant",
        "How do I find meaning in all this pain?",
        "What was this experience supposed to teach me?",
        "I feel like my story is just sadness now",
        "Help me see the bigger picture of my healing"
    ]
    
    for input_text in test_inputs:
        print(f"\nInput: {input_text}")
        print(f"Blue: {blue(input_text)}")
        print("-" * 50)


def test_red():
    """Test Red Bot - Direct truth-teller"""
    print("=== Testing Red Bot (Truth-Teller) ===")
    
    test_inputs = [
        "I want to text them right now",
        "Maybe I should drive by their house",
        "I've been stalking their social media all day",
        "What if I just call them once?",
        "I keep hoping they'll change their mind"
    ]
    
    for input_text in test_inputs:
        print(f"\nInput: {input_text}")
        print(f"Red: {red(input_text)}")
        print("-" * 50)


def test_yellow():
    """Test Yellow Bot - Upbeat energizer"""
    print("=== Testing Yellow Bot (Cheerleader) ===")
    
    test_inputs = [
        "I went an hour without thinking about them",
        "I managed to eat a full meal today",
        "I got out of bed and showered",
        "I'm not sure if I'm making any progress",
        "These small steps don't feel like enough"
    ]
    
    for input_text in test_inputs:
        print(f"\nInput: {input_text}")
        print(f"Yellow: {yellow(input_text)}")
        print("-" * 50)


def test_white():
    """Test White Bot - Peaceful grounding presence"""
    print("=== Testing White Bot (Grounding Presence) ===")
    
    test_inputs = [
        "I'm having a panic attack right now",
        "I can't breathe when I think about them",
        "Everything feels overwhelming and chaotic",
        "My heart is racing and I feel dizzy",
        "I need to calm down but don't know how"
    ]
    
    for input_text in test_inputs:
        print(f"\nInput: {input_text}")
        print(f"White: {white(input_text)}")
        print("-" * 50)


def test_custom_input():
    """Test all bots with custom user input"""
    user_input = input("Enter a message to test with all bots: ")
    
    print(f"\n=== Testing all bots with: '{user_input}' ===\n")
    
    bots = [
        ("Joe (Structured Coach)", joe),
        ("Sara (Sassy Bestie)", sara),
        ("Blue (Reflective Storyteller)", blue), 
        ("Red (Truth-Teller)", red),
        ("Yellow (Cheerleader)", yellow),
        ("White (Grounding Presence)", white)
    ]
    
    for name, bot_func in bots:
        try:
            response = bot_func(user_input)
            print(f"{name}: {response}\n")
        except Exception as e:
            print(f"{name} Error: {e}\n")


def interactive_test():
    """Interactive testing mode"""
    print("=== Interactive Bot Testing ===")
    print("Choose a bot to test:")
    print("1. Joe (Structured Coach)")
    print("2. Sara (Sassy Bestie)")  
    print("3. Blue (Reflective Storyteller)")
    print("4. Red (Truth-Teller)")
    print("5. Yellow (Cheerleader)")
    print("6. White (Grounding Presence)")
    print("7. Test all bots")
    print("0. Exit")
    
    while True:
        choice = input("\nEnter choice (0-7): ")
        
        if choice == "0":
            break
        elif choice == "1":
            msg = input("Enter message for Joe: ")
            print(f"Joe: {joe(msg)}")
        elif choice == "2":
            msg = input("Enter message for Sara: ")
            print(f"Sara: {sara(msg)}")
        elif choice == "3":
            msg = input("Enter message for Blue: ")
            print(f"Blue: {blue(msg)}")
        elif choice == "4":
            msg = input("Enter message for Red: ")
            print(f"Red: {red(msg)}")
        elif choice == "5":
            msg = input("Enter message for Yellow: ")
            print(f"Yellow: {yellow(msg)}")
        elif choice == "6":
            msg = input("Enter message for White: ")
            print(f"White: {white(msg)}")
        elif choice == "7":
            test_custom_input()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    print("Select test mode:")
    print("1. Test individual bots")
    print("2. Interactive testing")
    print("3. Custom input test")
    
    mode = input("Enter choice (1-3): ")
    
    if mode == "1":
        print("\nWhich bot to test?")
        print("1. Joe  2. Sara  3. Blue  4. Red  5. Yellow  6. White  7. All")
        bot_choice = input("Enter choice: ")
        
        if bot_choice == "1":
            test_joe()
        elif bot_choice == "2":
            test_sara()
        elif bot_choice == "3":
            test_blue()
        elif bot_choice == "4":
            test_red()
        elif bot_choice == "5":
            test_yellow()
        elif bot_choice == "6":
            test_white()
        elif bot_choice == "7":
            test_joe()
            test_sara()
            test_blue()
            test_red()
            test_yellow()
            test_white()
            
    elif mode == "2":
        interactive_test()
    elif mode == "3":
        test_custom_input()