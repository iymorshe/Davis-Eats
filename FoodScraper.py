import requests
from bs4 import BeautifulSoup

# Returns the dictionary {DAY: {MEAL: [Dishes{}]}}
def getDCMenu(dining_common):
    url = f"https://housing.ucdavis.edu/dining/menus/dining-commons/{dining_common}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # Dictionary to hold all menu items grouped by days and meals
    weekly_menu = {}

    day_sections = soup.find_all("div", class_="menu_maincontainer")

    for section in day_sections:
        day_name = section.find("h3").text.strip() if section.find("h3") else "Unknown Day"
        weekly_menu[day_name] = {"Breakfast": [], "Lunch": [], "Dinner": []}

        # Further assumptions: each meal type is in a distinct section/class within the day's section
        meals = section.find_all("div", recursive=False)  # Adjust the tag and class based on actual structure
        for meal in meals:
            meal_name = meal.find("h4").text.strip() if meal.find("h4") else "No Meal Name"

            # Check meal name to decide where to place it
            if "breakfast" in meal_name.lower():
                meal_type = "Breakfast"
            elif "lunch" in meal_name.lower():
                meal_type = "Lunch"
            elif "dinner" in meal_name.lower():
                meal_type = "Dinner"
            else:
                continue  # If no valid meal type is found, skip to the next

            menu_items = meal.find_all("li", class_="trigger")  
            for item in menu_items:
                dish_name = item.find("span").text.strip() if item.find("span") else "No Dish Name"
                description = item.find("p")
                dish_description = description.text.strip() if description else "No Description"
                nutrition = item.find("ul", class_="nutrition")
                nutritional_details = {}
                if nutrition:
                    for detail in nutrition.find_all("p"):
                        text = detail.text.strip().split(":")
                        if len(text) == 2:
                            nutritional_details[text[0].strip()] = text[1].strip()

                # Append the collected data to the list under the correct meal and day
                weekly_menu[day_name][meal_type].append({
                    "Dish Name": dish_name,
                    "Description": dish_description,
                    "Nutritional Information": nutritional_details
                })

    return weekly_menu

# Example usage
def print_menu(weekly_menu):
    for day, meals in weekly_menu.items():
        print(f"Day: {day}")
        for meal_type, dishes in meals.items():
            print(f"  Meal: {meal_type}")
            for dish in dishes:
                print(f"    Dish Name: {dish['Dish Name']}")
                print(f"    Description: {dish['Description']}")
                print("    Nutritional Information:")
                for nutrient, value in dish['Nutritional Information'].items():
                    print(f"      {nutrient}: {value}")
            print()  # Blank line for better separation between meals
        print("="*40)  # Line to separate days for clarity

menu_data = getDCMenu("segundo")
print_menu(menu_data)
