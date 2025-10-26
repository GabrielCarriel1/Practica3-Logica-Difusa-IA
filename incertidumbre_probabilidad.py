"""
Script 1: Incertidumbre y Probabilidad
Simulación de tiradas de dado y cálculo de probabilidades
Autor: Gabriel Carriel
Fecha: Octubre 2025
Inteligencia Artificial - Lógica Difusa
"""

import random

def simular_tiradas(num_tiradas=10):
    tiradas = [random.randint(1, 6) for _ in range(num_tiradas)]
    return tiradas

def calcular_probabilidad_mayor_4(tiradas):

    exitos = sum(1 for t in tiradas if t > 4)
    probabilidad = exitos / len(tiradas)
    return exitos, probabilidad

def main():
    print("=" * 60)
    print("SIMULACIÓN DE INCERTIDUMBRE Y PROBABILIDAD")
    print("=" * 60)
    
    # Configuración
    num_tiradas = 10
    
    # Simular tiradas
    print(f"\n🎲 Simulando {num_tiradas} tiradas de dado...\n")
    tiradas = simular_tiradas(num_tiradas)
    
    # Mostrar resultados
    print(f"Tiradas: {tiradas}")
    
    # Calcular estadísticas
    exitos, prob_empirica = calcular_probabilidad_mayor_4(tiradas)
    prob_teorica = 2/6  # Números 5 y 6
    
    print(f"\n📊 RESULTADOS:")
    print(f"   - Veces que salió > 4: {exitos}")
    print(f"   - Probabilidad empírica: {prob_empirica:.2%}")
    print(f"   - Probabilidad teórica: {prob_teorica:.2%}")
    print(f"   - Diferencia: {abs(prob_empirica - prob_teorica):.2%}")
    
    # Análisis
    print(f"\n💡 ANÁLISIS:")
    print(f"   La probabilidad teórica de obtener un número mayor a 4")
    print(f"   en un dado estándar es 33.33% (2 de 6 opciones).")
    print(f"   Con {num_tiradas} tiradas, obtuvimos {prob_empirica:.2%}.")
    
    # Simulación extendida
    print(f"\n🔬 SIMULACIÓN EXTENDIDA (1000 tiradas):")
    tiradas_ext = simular_tiradas(1000)
    exitos_ext, prob_ext = calcular_probabilidad_mayor_4(tiradas_ext)
    print(f"   - Probabilidad con 1000 tiradas: {prob_ext:.2%}")
    print(f"   - Convergencia hacia teórica: {abs(prob_ext - prob_teorica):.2%}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
