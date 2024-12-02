def city_country(city, country, population=None, language=None):
    """Return a city, country string with optional population and language."""
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    elif language:
        return f"{city}, {country}, {language}"
    else:
        return f"{city}, {country}"

#Print function with different inputs
print(city_country("Santiago", "Chile"))
print(city_country("New York", "USA", 8000000))
print(city_country("Tokyo", "Japan", 14000000, "Japanese"))