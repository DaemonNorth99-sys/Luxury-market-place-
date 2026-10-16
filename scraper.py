import os
import requests

SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://sokjtqnrqjzqkopoqpze.supabase.co')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY', 'sb_publishable_mUFpmAp3SEDwWxK-EZlA9A_xisWGyZS')

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "resolution=merge-duplicates"
}

# Referencias con arbitraje geográfico y rotación dinámica
relojes_data = [
    {
        "referencia": "126610LN",
        "marca": "Rolex",
        "modelo": "Submariner Date",
        "precio_medio": "13.200 €",
        "liquidez": "Alta Rotación",
        "origen": "Europa (Base)",
        "meta": "Europa"
    },
    {
        "referencia": "126610LN-JP",
        "marca": "Rolex",
        "modelo": "Submariner Date (Tokio)",
        "precio_medio": "11.500 €",
        "liquidez": "Oportunidad Arbitraje (-13%)",
        "origen": "Japón (Ahorro 1.700 €)",
        "meta": "Japón"
    },
    {
        "referencia": "126500LN",
        "marca": "Rolex",
        "modelo": "Daytona Ceramic",
        "precio_medio": "32.500 €",
        "liquidez": "Prima Sobrecosto",
        "origen": "Europa (Base)",
        "meta": "Europa"
    },
    {
        "referencia": "126500LN-US",
        "marca": "Rolex",
        "modelo": "Daytona Ceramic (EE.UU.)",
        "precio_medio": "30.900 €",
        "liquidez": "Arbitraje Moderado (-5%)",
        "origen": "EE.UU. ($33.500)",
        "meta": "Norteamérica"
    },
    {
        "referencia": "126710BLRO",
        "marca": "Rolex",
        "modelo": "GMT-Master II (Pepsi)",
        "precio_medio": "19.800 €",
        "liquidez": "Alta Rotación",
        "origen": "Europa (Base)",
        "meta": "Europa"
    },
    {
        "referencia": "126710BLRO-JP",
        "marca": "Rolex",
        "modelo": "GMT-Master II Pepsi (Tokio)",
        "precio_medio": "17.400 €",
        "liquidez": "Oportunidad Arbitraje (-12%)",
        "origen": "Japón (Ahorro 2.400 €)",
        "meta": "Japón"
    }
]

def reiniciar_y_sincronizar():
    url = f"{SUPABASE_URL}/rest/v1/relojes_laboratorio"
    
    # 1. Limpiar datos antiguos
    requests.delete(f"{url}?referencia=neq.0", headers=HEADERS)
    
    # 2. Insertar datos nuevos limpios
    for reloj in relojes_data:
        res = requests.post(url, headers=HEADERS, json=reloj)
        print(f"Insertado {reloj['referencia']}: {res.status_code}")

if __name__ == "__main__":
    reiniciar_y_sincronizar()
