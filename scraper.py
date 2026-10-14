import time
import random
import os
from supabase import create_client, Client

# 1. Configuración de credenciales
SUPABASE_URL = "https://sokjtqnrqjzqkopoqpze.supabase.co"
SUPABASE_KEY = "sb_publishable_mUFpmAp3SEDwWxK-EZlA9A_xisWGyZS"

def simular_comportamiento_humano():
    """Simula lectura, desplazamientos aleatorios y pausas para evitar baneos de IP."""
    print("🤖 Iniciando rutina de simulación humana...")
    
    # Tiempos de espera aleatorios (time.sleep)
    espera_inicial = random.uniform(2.5, 6.0)
    print(f"⏱️ Pausa de entrada aleatoria: {espera_inicial:.2f} segundos")
    time.sleep(espera_inicial)

    # Simulación de scrolling por bloques
    pasos_scroll = random.randint(3, 6)
    for i in range(1, pasos_scroll + 1):
        pixels = random.randint(250, 600)
        pausa_scroll = random.uniform(1.2, 3.5)
        print(f"📜 [Scroll {i}/{pasos_scroll}] Desplazando {pixels}px — Pausa de {pausa_scroll:.2f}s")
        time.sleep(pausa_scroll)

def actualizar_mercado():
    """Conecta con Supabase y simula el cálculo/actualización de referencias."""
    simular_comportamiento_humano()

    print("\n⚡ Conectando con Supabase...")
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Referencias a monitorizar y actualizar
        referencias = [
            {"referencia": "126610LN", "marca": "Rolex", "modelo": "Submariner", "precio_medio": "13.200 €", "liquidez": "Alta demanda"},
            {"referencia": "126500LN", "marca": "Rolex", "modelo": "Daytona", "precio_medio": "32.500 €", "liquidez": "Alta demanda"},
            {"referencia": "126710BLRO", "marca": "Rolex", "modelo": "GMT Pepsi", "precio_medio": "22.800 €", "liquidez": "Buena rotación"}
        ]

        print("🔄 Actualizando laboratorio de referencias en tiempo real...")
        for reloj in referencias:
            # Upsert actualiza la fila si la referencia ya existe
            response = supabase.table('relojes_laboratorio').upsert(reloj, on_conflict='referencia').execute()
            print(f"✅ Sincronizado: {reloj['marca']} {reloj['modelo']} ({reloj['referencia']}) -> {reloj['precio_medio']}")

        print("\n✨ ¡Proceso completado con éxito! Supabase está al día.")

    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")

if __name__ == "__main__":
    actualizar_mercado()
