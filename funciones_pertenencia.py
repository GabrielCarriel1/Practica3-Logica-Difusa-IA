"""
Script 2: Funciones de Pertenencia en Lógica Difusa
Implementación de funciones de pertenencia triangular y trapezoidal
Autor: Gabriel Carriel
Fecha: Octubre 2025
Inteligencia Artificial - Lógica Difusa
"""

import numpy as np

def triangular(x, a, b, c):

    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    else:
        return 0

def trapezoidal(x, a, b, c, d):
   
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c)
    else:
        return 0

def evaluar_temperatura(temperatura):

    # Definir conjuntos difusos para temperatura
    fria = trapezoidal(temperatura, 0, 0, 10, 20)
    templada = triangular(temperatura, 10, 20, 30)
    calida = triangular(temperatura, 20, 30, 40)
    caliente = trapezoidal(temperatura, 30, 40, 50, 50)
    
    return {
        'Fría': fria,
        'Templada': templada,
        'Cálida': calida,
        'Caliente': caliente
    }

def mostrar_grafico_texto(temperatura, grados):
  
    print(f"\n📊 VISUALIZACIÓN para {temperatura}°C:")
    print("=" * 50)
    
    for categoria, grado in grados.items():
        barra_len = int(grado * 40)
        barra = "█" * barra_len
        print(f"{categoria:12} [{grado:.2f}] {barra}")
    
    print("=" * 50)

def main():
    print("=" * 60)
    print("FUNCIONES DE PERTENENCIA EN LÓGICA DIFUSA")
    print("=" * 60)
    
    # Caso 1: Temperatura cálida (ejemplo de la guía)
    print("\n📍 CASO 1: Temperatura Cálida")
    print("-" * 60)
    temperatura = 25
    grado_calida = triangular(temperatura, 15, 25, 35)
    print(f"Temperatura: {temperatura}°C")
    print(f"Parámetros función triangular: a=15, b=25, c=35")
    print(f"Grado de pertenencia a 'Cálida': {grado_calida:.2f}")
    
    # Caso 2: Evaluación completa
    print("\n📍 CASO 2: Evaluación Completa de Temperatura")
    print("-" * 60)
    temperatura_test = 25
    grados = evaluar_temperatura(temperatura_test)
    
    print(f"\nEvaluando temperatura: {temperatura_test}°C\n")
    for categoria, grado in grados.items():
        print(f"   {categoria:12} : {grado:.3f} ({grado*100:.1f}%)")
    
    mostrar_grafico_texto(temperatura_test, grados)
    
    # Caso 3: Múltiples temperaturas
    print("\n📍 CASO 3: Análisis de Múltiples Temperaturas")
    print("-" * 60)
    temperaturas_prueba = [5, 15, 25, 35, 45]
    
    print("\nTemperatura | Fría | Templada | Cálida | Caliente")
    print("-" * 60)
    
    for temp in temperaturas_prueba:
        grados = evaluar_temperatura(temp)
        print(f"    {temp:2d}°C    | {grados['Fría']:.2f} |   {grados['Templada']:.2f}   | {grados['Cálida']:.2f} |   {grados['Caliente']:.2f}")
    
    # Aplicación práctica
    print("\n💡 APLICACIÓN: Sistema de Aire Acondicionado")
    print("-" * 60)
    temp_ambiente = 28
    grados_ac = evaluar_temperatura(temp_ambiente)
    
    print(f"\nTemperatura ambiente: {temp_ambiente}°C")
    print(f"Membresía 'Cálida': {grados_ac['Cálida']:.2f}")
    print(f"Membresía 'Caliente': {grados_ac['Caliente']:.2f}")
    
    # Decisión del sistema
    max_categoria = max(grados_ac, key=grados_ac.get)
    print(f"\n🔧 Decisión: Temperatura clasificada como '{max_categoria}'")
    
    if grados_ac['Caliente'] > 0.5:
        print("   → Aire acondicionado a potencia ALTA")
    elif grados_ac['Cálida'] > 0.5:
        print("   → Aire acondicionado a potencia MEDIA")
    elif grados_ac['Templada'] > 0.5:
        print("   → Aire acondicionado a potencia BAJA")
    else:
        print("   → Aire acondicionado APAGADO")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
