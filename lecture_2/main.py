from datetime import datetime

def generate_profile(current_age):
    if 0 <= current_age <= 12:
        return "Child"
    elif 13 <= current_age <= 19:
        return "Teenager"
    elif current_age >= 20:
        return "Adult"
    return None


def input_info():
    user_name = input("Enter your full name: ")
    while True:
        birth_year_str = input("Enter your birth year: ")
        is_year_valid = str.isdigit(birth_year_str)
        if is_year_valid:
            birth_year = int(birth_year_str)
            if (birth_year < 1900) or (birth_year > datetime.now().year):
                print("Your birth year must be between 1900 and 2025")
            else: break
        else:
            print("Enter a valid birth year")
    current_age = datetime.now().year - birth_year
    hobbies = []
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish:")
        if hobby == 'stop':
            break
        hobbies.append(hobby)
    life_stage = generate_profile(current_age)
    return {'Name': user_name,'Age': current_age, 'LifeStage': life_stage, 'Hobby': hobbies}

def show_profile(user_profile):
    print("---","Profile Summary: ", sep='\n')
    for key in user_profile:
        if key == 'Hobby':
            if len(user_profile[key]) > 0:
                print(f'Favorite hobbies ({len(user_profile[key])}):')
                for hobby in user_profile[key]:
                    print(f'- {hobby}')
            else:
                print("You didn't mention any hobbies")
            continue
        print(f'{key}: {user_profile[key]}')
    print("---")

if __name__ == '__main__':
    show_profile(input_info())
