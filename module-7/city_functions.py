# This function accepts a city, country, population and/or language as arguments
# and returns a formatted string with the required output.

def city_country(city, country, population=None, language=None):
    # If both population and language are provided
    if population and language:
        return f"{city.title()}, {country.title()} - {population}, {language.title()}"
    # If only population is provided
    elif population:
        return f"{city.title()}, {country.title()} - {population}"
    # If only language is provided
    elif language:
        return f"{city.title()}, {country.title()}, {language.title()}"
    # If neither is provided
    else:
        return f"{city.title()}, {country.title()}"
    
        
# Prints formatted city, country names, population and language

print(city_country("cartagena", "colombia"))
print(city_country("paris", "france", "2140526"))
print(city_country("tokyo", "japan", "13929286", "japanese"))
