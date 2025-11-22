humming = {500,70,68,78}


favourite_chais = [
"masala chai","lemon tea","masala chai",
"lemon tea","green tea","elaichi chai"
]



unique_chai = {chai for chai in favourite_chais}
print(unique_chai)


recipes = {
    "masala chai":["ginger","cardamom","clove"],
    "ELAICHI chai": ["caradamom","milk"],
    "spicy chai":["ginger","black paper"],
    }


unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)