from math import radians, sin, cos, sqrt, atan2

COORDENADAS = {
    'Aveiro': [40.6405, -8.6538],
    'Beja': [38.0151, -7.8632],
    'Braga': [41.5452, -8.4265],
    'Bragança': [41.8060, -6.7567],
    'Castelo Branco': [39.8222, -7.4908],
    'Coimbra': [40.2118, -8.4295],
    'Évora': [38.5711, -7.9135],
    'Faro': [37.0194, -7.9304],
    'Guarda': [40.5373, -7.2676],
    'Leiria': [39.7436, -8.8070],
    'Lisboa': [38.7169, -9.1395],
    'Portalegre': [39.2967, -7.4280],
    'Porto': [41.1496, -8.611],
    'Santarém': [39.2362, -8.6859],
    'Setúbal': [38.5248, -8.8882],
    'Viana do Castelo': [41.6918, -8.8344],
    'Vila Real': [41.3006, -7.7441],
    'Viseu': [40.6610, -7.9097],
}

# Função para calcular distância em linha reta
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    lat1, lat2 = radians(lat1), radians(lat2)
    
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return round(R * c)

HEURISTICAS_MATRIZ = {}

for cidade1, (lat1, lon1) in COORDENADAS.items():
    HEURISTICAS_MATRIZ[cidade1] = {}
    for cidade2, (lat2, lon2) in COORDENADAS.items():
        dist = haversine(lat1, lon1, lat2, lon2)
        HEURISTICAS_MATRIZ[cidade1][cidade2] = dist
