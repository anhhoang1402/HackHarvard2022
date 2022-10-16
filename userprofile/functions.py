"""
Contains the functions needed in our main.py
"""
import http.client
import json

conn = http.client.HTTPSConnection("edamam-recipe-search.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "edamam-recipe-search.p.rapidapi.com",
    'x-rapidapi-key': "ce19d0164fmsh3d383efc0e85ce5p16dcb1jsnb1a4a3c79541"
    }

# Function definitions


def user_string():  # Function will be called in other function
    user_string = ''  # Will use to change their ' ' into %20
    userinput = input("Enter the foods/ingredients that you LOVE!: ")
    for i in userinput:
        if i == ' ':
            i = '%20'
        user_string = user_string + i
    return user_string


def search_data(): # User-based
    # Returns a dataset of the 10 top searches based on what the user typed in
    term = user_string()
    conn.request("GET", "/search?q=" + term, headers=headers)
    res = conn.getresponse()
    data = res.read()
    # Turns the api into a dictionary json file
    j_data = json.loads((data.decode("utf-8")))
    return j_data


def automatic_data(word):
    # Returns a dataset of the 10 top searches based on parameter
    conn.request("GET", "/search?q=" + word, headers=headers)
    res = conn.getresponse()
    data = res.read()
    # Turns the api into a dictionary json file
    j_data = json.loads((data.decode("utf-8")))
    return j_data

def attain(dataset, trait): # gets a chosen trait from dataset, trait is a string
    """
    Traits that you can chooose...
    label
    ingredientLines
    healthLabels
    mealType
    dishType
    calories
    image
    """
    final_list = []
    for i in dataset["hits"]:
        i = dataset["hits"].index(i)
        final_list.append(dataset["hits"][i]["recipe"][trait])
    return final_list


class meal(): # Each recipe will have all of these attributes
    def __init__(self, label, ingredientLines, healthLabels, mealType, dishType, cuisineType, calories, image):
        self.label = label # name
        self.ingredientLines = ingredientLines # ingredients
        self.healthLabels = healthLabels # health labels
        self.mealType = mealType # when to have meal
        self.dishType = dishType # what type of meal is it
        self.cuisineType = cuisineType # what culture is it from
        self.calories = calories # calories
        self.image = image # image


def create_classes(dataset): # Creates a list of class meal() objects
    object_list = []
    for i in dataset["hits"]:
        i = dataset["hits"].index(i)

        object_list.append(meal(attain(dataset, 'label')[i], attain(dataset, 'ingredientLines')[i],
                                 attain(dataset, 'healthLabels')[i], attain(dataset, 'mealType')[i],
                                 attain(dataset, 'dishType')[i], attain(dataset, 'cuisineType')[i],
                                 attain(dataset, 'calories')[i], attain(dataset, 'image')[i]))
    return object_list


def giant_list(keywords):
    biggo = []
    for i in keywords:
        data = automatic_data(i)
        temp_list = []
        temp_list.append(create_classes(data))
        for n in temp_list:
            biggo.append(n)
    return biggo


key_terms = ['raspberry', 'pineapple', 'chia']
full_list = giant_list(key_terms)

