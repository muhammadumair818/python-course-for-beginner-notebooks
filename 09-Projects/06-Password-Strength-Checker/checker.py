"""
PASSWORD STRENGTH CHECKER

Analyze password strength and provide recommendations.

Features:
- Check password length
- Verify character diversity
- Detect common patterns
- Provide security score
- Give improvement suggestions
"""

import re

def check_password_strength(password):
    """
    Analyze password strength and return score + feedback.
    
    Returns a tuple of (score, feedback_list)
    """
    
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password too short (min 8 characters)")
    
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("⚠️ Consider using 12+ characters")
    
    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")
    
    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")
    
    # Check digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")
    
    # Check special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 1
    else:
        feedback.append("⚠️ Add special characters (!@#$%^&*)")
    
    # Check for common patterns
    if re.search(r'(.)\1{2,}', password):
        feedback.append("⚠️ Avoid repeating characters")
    
    if re.search(r'(123|234|345|456|567|678|789|890)', password):
        feedback.append("⚠️ Avoid sequential numbers")
    
    if re.search(r'(abc|bcd|cde|def)', password, re.IGNORECASE):
        feedback.append("⚠️ Avoid sequential letters")
    
    # Check for common weak passwords
    common_weak = ['password', '123456', 'qwerty', 'admin', 'letmein', 'welcome']
    if password.lower() in common_weak:
        feedback.append("❌ This is a commonly used weak password!")
        score = 0
    
    # Add positive feedback
    if score >= 5:
        feedback.append("✅ Strong password!")
    elif score >= 3:
        feedback.append("⚠️ Moderate password")
    
    return score, feedback

def get_strength_level(score):
    """Convert score to strength level"""
    
    max_score = 6
    
    if score == max_score:
        return "🔐 VERY STRONG"
    elif score >= 5:
        return "🔒 STRONG"
    elif score >= 3:
        return "🟡 MODERATE"
    elif score > 0:
        return "🔓 WEAK"
    else:
        return "❌ VERY WEAK"

def main():
    """Main application"""
    
    print("="*50)
    print("PASSWORD STRENGTH CHECKER")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("  1. Check password strength")
        print("  2. Get password tips")
        print("  3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            password = input("\nEnter password to check: ")
            
            if not password:
                print("❌ Password cannot be empty!")
                continue
            
            score, feedback = check_password_strength(password)
            strength = get_strength_level(score)
            
            print(f"\nPassword: {'*' * len(password)}")
            print(f"Strength: {strength}")
            print(f"Score: {score}/6")
            print("\nFeedback:")
            for item in feedback:
                print(f"  {item}")
        
        elif choice == '2':
            print("\n" + "="*50)
            print("PASSWORD SECURITY TIPS")
            print("="*50)
            print("""
1. LENGTH: Use 12+ characters for better security
2. VARIETY: Mix uppercase, lowercase, numbers, symbols
3. UNIQUE: Don't reuse passwords across sites
4. AVOID: Don't use personal info (name, birthdate)
5. AVOID: Don't use dictionary words
6. AVOID: Don't use sequential patterns (123, abc)
7. UPDATE: Change passwords periodically
8. MANAGER: Use a password manager for storage

Example Strong Password:
  MyDog@2024Coffee!
            """)
        
        elif choice == '3':
            print("Goodbye! 👋")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
