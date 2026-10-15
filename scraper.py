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

# Referencias con desglose de arbitraje internacional (Japón, EE.UU. vs Europa)
relojes_data = [
    {
        "referencia": "126610LN",
        "marca": "Rolex",
        "modelo": "Submariner Date",
        "precio_medio": "13.200 €",
        "liquidez": "Alta demanda",
        "origen": "Europa (Mercado Base)",
        "meta": "Europa"
    },
    {
        "referencia": "126610LN-JP",
        "marca": "Rolex",
        "modelo": "Submariner Date (Tokio)",
        "precio_medio": "11.500 €",
        "liquidez": "Oportunidad Arbitraje (-13%)",
        "origen": "Japón: 11.500 € (Ahorro 1.700 €)",
        "meta": "Japón"
    },
    {
        "referencia": "126500LN",
        "marca": "Rolex",
        "modelo": "Daytona Ceramic",
        "precio_medio": "32.500 €",
        "liquidez": "Alta demanda",
        "origen": "Europa (Mercado Base)",
        "meta": "Europa"
    },
    {
        "referencia": "126500LN-US",
        "marca": "Rolex",
        "modelo": "Daytona Ceramic (EE.UU.)",
        "precio_medio": "30.900 €",
        "liquidez": "Arbitraje Moderado (-5%)",
        "origen": "EE.UU.: 30.900 € ($33,500)",
        "meta": "Norteamérica"
    },
    {
        "referencia": "126710BLRO",
        "marca": "Rolex",
        "modelo": "GMT-Master II (Pepsi)",
        "precio_medio": "19.800 €",
        "liquidez": "Alta demanda",
        "origen": "Europa (Mercado Base)",
        "meta": "Europa"
    },
    {
        "referencia": "126710BLRO-JP",
        "marca": "Rolex",
        "modelo": "GMT-Master II Pepsi (Tokio)",
        "precio_medio": "17.400 €",
        "liquidez": "Oportunidad Arbitraje (-12%)",
        "origen": "Japón: 17.400 € (Ahorro 2.400 €)",
        "meta": "Japón"
    }
]

def actualizar_supabase():
    url = f"{SUPABASE_URL}/rest/v1/relojes_laboratorio"
    for reloj in relojes_data:
        response = requests.post(url, headers=HEADERS, json=reloj)
        print(f"Sincronizando {reloj['referencia']}: {response.status_code}")

if __name__ == "__main__":
    actualizar_supabase()
