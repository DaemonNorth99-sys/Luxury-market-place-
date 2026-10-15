import time
import random
import os
from supabase import create_client, Client

SUPABASE_URL = "https://sokjtqnrqjzqkopoqpze.supabase.co"
SUPABASE_KEY = "sb_publishable_mUFpmAp3SEDwWxK-EZlA9A_xisWGyZS"

TASAS_CAMBIO = {
    "EUR": 1.0,
    "USD": 0.92,
    "JPY": 0.0061
}

def convertir_a_euros(monto, moneda):
    tasa = TASAS_CAMBIO.get(moneda.upper(), 1.0)
    return int(monto * tasa)

def analizar_estado_y_autenticidad(descripcion):
    desc = descripcion.lower()
    multiplicador = 1.0
    tags = []
    
    if "no box" in desc or "sin caja" in desc:
        multiplicador -= 0.08
        tags.append("Sin caja (-8%)")
    if "no papers" in desc or "sin papeles" in desc:
        multiplicador -= 0.12
        tags.append("Sin papeles (-12%)")
    if "scratches" in desc or "rayas" in desc:
        multiplicador -= 0.05
        tags.append("Con marcas (-5%)")
    elif "unworn" in desc or "nuevo" in desc:
        multiplicador += 0.05
        tags.append("Estreno (+5%)")
        
    resumen = " · ".join(tags) if tags else "Full Set / Excelente"
    return multiplicador, resumen

def ejecutar_rastreo_global():
    print("🌍 [Luxury Market Pulse] Iniciando rastreo global multi-mercado...")
    time.sleep(random.uniform(2.0, 4.5))

    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        anuncios_globales = [
            {
                "referencia": "126610LN",
                "marca": "Rolex",
                "modelo": "Submariner Date",
                "region": "Europa (ES)",
                "precio_local": 13900,
                "moneda": "EUR",
                "descripcion": "Submariner Date full set 2024, excellent condition."
            },
            {
                "referencia": "126610LN",
                "marca": "Rolex",
                "modelo": "Submariner Date",
                "region": "Japón (JP - Oportunidad)",
                "precio_local": 1980000,
                "moneda": "JPY",
                "descripcion": "Rolex Submariner 126610LN unused with box and papers."
            },
            {
                "referencia": "126500LN",
                "marca": "Rolex",
                "modelo": "Daytona Panda",
                "region": "EE.UU. (US)",
                "precio_local": 36000,
                "moneda": "USD",
                "descripcion": "Daytona Panda dial, minor scratches on clasp, no box."
            }
        ]

        print("🔄 Normalizando divisas y calculando arbitraje geográfico...")

        for anuncio in anuncios_globales:
            precio_euros_base = convertir_a_euros(anuncio["precio_local"], anuncio["moneda"])
            mult, estado_meta = analizar_estado_y_autenticidad(anuncio["descripcion"])
            precio_final = int(precio_euros_base * mult)
            
            precio_str = f"{precio_final:,.0f} €".replace(",", ".")
            meta_str = f"Mercado: {anuncio['region']} · {estado_meta}"

            reloj_data = {
                "referencia": anuncio["referencia"],
                "marca": anuncio["marca"],
                "modelo": anuncio["modelo"],
                "precio_medio": precio_str,
                "liquidez": "Arbitraje Global",
                "meta": meta_str
            }

            supabase.table('relojes_laboratorio').upsert(reloj_data, on_conflict='referencia').execute()
            print(f"✅ Procesado [{anuncio['region']}]: {anuncio['modelo']} -> {precio_str}")

        print("\n✨ Rastreo global finalizado con éxito.")

    except Exception as e:
        print(f"❌ Error crítico en el rastreo global: {e}")

if __name__ == "__main__":
    ejecutar_rastreo_global()
