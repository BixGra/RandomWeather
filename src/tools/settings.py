from enum import Enum


class WeatherImage(Enum):
    _0 = "sun.png"
    _1 = "sun_behind_small_cloud.png"
    _2 = "sun_behind_cloud.png"
    _3 = "sun_behind_large_cloud.png"
    _45 = "fog.png"
    _48 = "fog.png"
    _51 = "sun_behind_rain_cloud.png"
    _53 = "sun_behind_rain_cloud.png"
    _55 = "sun_behind_rain_cloud.png"
    _56 = "sun_behind_rain_cloud.png"
    _57 = "sun_behind_rain_cloud.png"
    _61 = "cloud_with_rain.png"
    _63 = "cloud_with_rain.png"
    _65 = "cloud_with_rain.png"
    _66 = "cloud_with_rain.png"
    _67 = "cloud_with_rain.png"
    _71 = "cloud_with_snow.png"
    _73 = "cloud_with_snow.png"
    _75 = "cloud_with_snow.png"
    _77 = "cloud_with_snow.png"
    _80 = "cloud_with_rain.png"
    _81 = "cloud_with_rain.png"
    _82 = "cloud_with_lightning_and_rain.png"
    _85 = "cloud_with_snow.png"
    _86 = "cloud_with_snow.png"
    _95 = "cloud_with_lightning_and_rain.png"
    _96 = "cloud_with_lightning_and_rain.png"
    _99 = "cloud_with_lightning_and_rain.png"


class WeatherType(Enum):
    _0 = "Ensoleillé"
    _1 = "Nuages clairsemés"
    _2 = "Partiellement nuageux"
    _3 = "Couvert"
    _45 = "Brouillard"
    _48 = "Brouillard givrant"
    _51 = "Légère bruine"
    _53 = "Bruine"
    _55 = "Bruine intense"
    _56 = "Légère bruine verglassante"
    _57 = "Bruine verglassante"
    _61 = "Pluie faible"
    _63 = "Pluie"
    _65 = "Pluie intense"
    _66 = "Pluie verglassante"
    _67 = "Pluie verglassante intense"
    _71 = "Légères chutes de neige"
    _73 = "Chutes de neige"
    _75 = "Fortes chutes de neige"
    _77 = "Fortes chutes de neige"
    _80 = "Averses légères"
    _81 = "Averses"
    _82 = "Fortes averses"
    _85 = "Tempête de neige"
    _86 = "Tempête de neige"
    _95 = "Orage"
    _96 = "Orage de grêle"
    _99 = "Orage de grêle"


class WeatherGradient(Enum):
    _0 = {"start": "225, 119, 40", "end": "255, 208, 61"}
    _1 = {"start": "242, 236, 255", "end": "255, 214, 67"}
    _2 = {"start": "242, 236, 255", "end": "255, 214, 67"}
    _3 = {"start": "242, 236, 255", "end": "255, 214, 67"}
    _45 = {"start": "228, 228, 232", "end": "254, 253, 255"}
    _48 = {"start": "228, 228, 232", "end": "254, 253, 255"}
    _51 = {"start": "255, 215, 70", "end": "100, 121, 255"}
    _53 = {"start": "255, 215, 70", "end": "100, 121, 255"}
    _55 = {"start": "255, 215, 70", "end": "100, 121, 255"}
    _56 = {"start": "255, 215, 70", "end": "100, 121, 255"}
    _57 = {"start": "255, 215, 70", "end": "100, 121, 255"}
    _61 = {"start": "55, 53, 255", "end": "184, 184, 255"}
    _63 = {"start": "55, 53, 255", "end": "184, 184, 255"}
    _65 = {"start": "55, 53, 255", "end": "184, 184, 255"}
    _66 = {"start": "55, 53, 255", "end": "184, 184, 255"}
    _67 = {"start": "55, 53, 255", "end": "184, 184, 255"}
    _71 = {"start": "240, 236, 255", "end": "186, 185, 255"}
    _73 = {"start": "240, 236, 255", "end": "186, 185, 255"}
    _75 = {"start": "240, 236, 255", "end": "186, 185, 255"}
    _77 = {"start": "240, 236, 255", "end": "186, 185, 255"}
    _80 = {"start": "55, 53, 255", "end": "184, 184, 255"}
    _81 = {"start": "55, 53, 255", "end": "184, 184, 255"}
    _82 = {"start": "71, 62, 239", "end": "255, 160, 75"}
    _85 = {"start": "240, 236, 255", "end": "186, 185, 255"}
    _86 = {"start": "240, 236, 255", "end": "186, 185, 255"}
    _95 = {"start": "71, 62, 239", "end": "255, 160, 75"}
    _96 = {"start": "71, 62, 239", "end": "255, 160, 75"}
    _99 = {"start": "71, 62, 239", "end": "255, 160, 75"}
