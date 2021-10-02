SUN, MON, TUE, WED, THU, FRI, SAT = 0, 1, 2, 3, 4, 5, 6

WEEK_DAY = (
    (SUN, "Domingo"),
    (MON, "Segunda-Feira"),
    (TUE, "Terça-Feira"),
    (WED, "Quarta-Feira"),
    (THU, "Quinta-Feira"),
    (FRI, "Sexta-Feira"),
    (SAT, "Sábado"),
)

DRINK, LUNCH, DESSERT, PORTION, ADDITIONAL = 0,1,2,3

TYPE_REVENUE_MENU = (
    (DRINK, "Bebida"),
    (LUNCH, "Lanche"),
    (DESSERT, "Sobremesa"),
    (PORTION, "Porção"),
)

DRINK_RESALE, INGREDIENT = 0, 1

TYPE_PRODUCT_MENU = (
    (DRINK_RESALE, "Revenda"),
    (INGREDIENT, "Ingrediente"),
)
