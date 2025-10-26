"""
Script 3: Defuzificación por Método del Centroide
Cálculo del centroide para convertir valores difusos en valores precisos
Autor: Gabriel Carriel
Fecha: Octubre 2025
Inteligencia Artificial - Lógica Difusa
"""

import numpy as np

def calcular_centroide(valores, grados):
   
    if len(valores) != len(grados):
        raise ValueError("Las listas deben tener la misma longitud")
    
    if sum(grados) == 0:
        raise ValueError("La suma de grados no puede ser cero")
    
    numerador = sum(mu * x for mu, x in zip(grados, valores))
    denominador = sum(grados)
    centroide = numerador / denominador
    
    return centroide

def mostrar_calculo_detallado(valores, grados):
    
    print("\n📝 CÁLCULO DETALLADO:")
    print("=" * 60)
    print("\nFórmula del Centroide: C = Σ(μᵢ × xᵢ) / Σ(μᵢ)\n")
    
    print("Valores (xᵢ) y sus grados de pertenencia (μᵢ):")
    print("-" * 60)
    
    productos = []
    for i, (x, mu) in enumerate(zip(valores, grados), 1):
        producto = mu * x
        productos.append(producto)
        print(f"  {i}. μ = {mu:.2f}, x = {x:5.1f} → μ × x = {mu:.2f} × {x:5.1f} = {producto:6.2f}")
    
    print("-" * 60)
    
    numerador = sum(productos)
    denominador = sum(grados)
    
    print(f"\nNumerador   (Σ μᵢ × xᵢ) = {' + '.join(f'{p:.2f}' for p in productos)}")
    print(f"                          = {numerador:.2f}")
    
    print(f"\nDenominador (Σ μᵢ)       = {' + '.join(f'{g:.2f}' for g in grados)}")
    print(f"                          = {denominador:.2f}")
    
    centroide = numerador / denominador
    print(f"\nCentroide = {numerador:.2f} / {denominador:.2f} = {centroide:.2f}")
    print("=" * 60)
    
    return centroide

def ejemplo_ventilador(temperatura, humedad):
    
    # Grados de pertenencia según temperatura y humedad
    # Simulamos resultados de inferencia difusa
    
    if temperatura < 20:
        grados = [0.8, 0.2, 0.0]  # Bajo, Medio, Alto
    elif temperatura < 28:
        grados = [0.2, 0.7, 0.1]
    else:
        grados = [0.0, 0.3, 0.7]
    
    # Ajuste por humedad
    if humedad > 70:
        grados = [g * 1.2 if i == 2 else g for i, g in enumerate(grados)]
    
    # Normalizar para que sumen <= 1
    suma = sum(grados)
    if suma > 1:
        grados = [g / suma for g in grados]
    
    # Velocidades correspondientes
    velocidades = [20, 50, 80]  # Bajo, Medio, Alto
    
    return velocidades, grados

def main():
    print("=" * 60)
    print("DEFUZIFICACIÓN POR MÉTODO DEL CENTROIDE")
    print("=" * 60)
    
    # CASO 1: Ejemplo de la guía práctica
    print("\n📍 CASO 1: Ejemplo de la Guía Práctica")
    print("-" * 60)
    valores_guia = [10, 20, 30]
    grados_guia = [0.2, 0.5, 0.8]
    
    print(f"Valores:              {valores_guia}")
    print(f"Grados de pertenencia: {grados_guia}")
    
    centroide_guia = mostrar_calculo_detallado(valores_guia, grados_guia)
    
    print(f"\n✅ Resultado: El valor defuzificado es {centroide_guia:.2f}")
    
    # CASO 2: Control de ventilador
    print("\n\n📍 CASO 2: Sistema de Control de Ventilador")
    print("-" * 60)
    
    temp = 26
    hum = 65
    
    print(f"Condiciones ambientales:")
    print(f"  - Temperatura: {temp}°C")
    print(f"  - Humedad: {hum}%")
    
    velocidades, grados_ventilador = ejemplo_ventilador(temp, hum)
    
    print(f"\nVelocidades posibles: {velocidades} (Bajo, Medio, Alto)")
    print(f"Grados de activación: {[f'{g:.2f}' for g in grados_ventilador]}")
    
    velocidad_final = calcular_centroide(velocidades, grados_ventilador)
    
    print(f"\n🔧 Velocidad del ventilador calculada: {velocidad_final:.1f}%")
    
    # CASO 3: Múltiples escenarios
    print("\n\n📍 CASO 3: Análisis de Múltiples Escenarios")
    print("-" * 60)
    
    escenarios = [
        ([10, 20, 30], [0.9, 0.1, 0.0], "Frío"),
        ([10, 20, 30], [0.1, 0.8, 0.1], "Templado"),
        ([10, 20, 30], [0.0, 0.2, 0.8], "Caliente"),
        ([10, 20, 30], [0.3, 0.4, 0.3], "Moderado")
    ]
    
    print("\nEscenario     | Grados μ        | Centroide | Interpretación")
    print("-" * 60)
    
    for valores, grados, desc in escenarios:
        c = calcular_centroide(valores, grados)
        grados_str = str([f'{g:.1f}' for g in grados])
        print(f"{desc:13} | {grados_str:15} | {c:6.2f}    | Nivel: {c/30*100:.0f}%")
    
    # Interpretación
    print("\n💡 INTERPRETACIÓN:")
    print("-" * 60)
    print("""
El método del centroide permite convertir múltiples valores difusos
en una decisión numérica precisa. Es especialmente útil en:

• Sistemas de control automático (temperatura, velocidad, presión)
• Toma de decisiones con información imprecisa
• Regulación gradual de actuadores
• Sistemas expertos con salidas continuas

El valor resultante representa un "compromiso ponderado" entre
todas las posibles acciones, considerando sus grados de activación.
    """)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
