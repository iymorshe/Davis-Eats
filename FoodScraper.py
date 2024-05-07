import requests
from bs4 import BeautifulSoup


# Returns the dictionarty {DAY:[Dishes{}]}
def getDCMenu(dining_common):
    # Fetch the page
    url = "https://housing.ucdavis.edu/dining/menus/dining-commons/"+dining_common+"/"
    response = requests.get(url)
    response_text = response.text

    # Parse the HTML content
    soup = BeautifulSoup(response_text, 'lxml')

    # Dictionary to hold all menu items grouped by days
    weekly_menu = {}

    day_sections = soup.find_all("div", class_="menu_maincontainer")  # Adjust class or tag as needed

    for section in day_sections:

        day_name = section.find("h3").text.strip() if section.find("h3") else "Unknown Day"
        
        # Initialize the day in the dictionary
        weekly_menu[day_name] = []
        
        # Extract dishes as before
        menu_items = section.find_all("li", class_="trigger")  # Adjust class or tag as needed
        
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

            # Append the collected data to the list under the correct day
            weekly_menu[day_name].append({
                "Dish Name": dish_name,
                "Description": dish_description,
                "Nutritional Information": nutritional_details
            })
        # # Output the weekly menu
        # for day, menu in weekly_menu.items():
        #     print(f"{day}:")
        #     for item in menu:
        #         print(item)
        #     print("\n")
        return weekly_menu
print(getDCMenu("segundo"))
