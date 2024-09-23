from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_view(request, recipe_name):
    # Получаем список ингредиентов для указанного блюда
    ingredients = DATA.get(recipe_name)
    #Получаем кол-во человек для приготовления блюда (1 = по умолчанию)
    servings = request.GET.get('servings', 1)
    if ingredients is None:
        # Если рецепт не найден, возвращаем пустой контекст
        context = {
            'recipe': {}, #благодаря шаблону html браузер отдаст "Такого рецепта не знаю :("
            'recipe_name': recipe_name  # Передаем название блюда в контекст
        }
    else:
        context = {
            'recipe': {ingredient: float(quantity) * int(servings) for ingredient, quantity in ingredients.items()},
            'recipe_name': recipe_name  # Передаем название блюда в контекст
        }
    return render(request, 'calculator/index.html', context)

