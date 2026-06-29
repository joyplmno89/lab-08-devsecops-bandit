# Laboratorio Semana 8 - DevSecOps con GitHub Actions y Bandit

## Descripción

Este proyecto corresponde al Laboratorio Semana 8 del curso Desarrollo Seguro de Aplicaciones.

El objetivo es configurar un pipeline de seguridad con GitHub Actions para ejecutar análisis automático de vulnerabilidades usando Bandit.

## Archivos principales

- app_vulnerable.py: archivo con vulnerabilidades intencionales.
- app_seguro.py: archivo corregido con controles básicos.
- requirements.txt: dependencias del proyecto.
- .github/workflows/security.yml: workflow de seguridad.

## Herramientas utilizadas

- Python
- Flask
- Bandit
- Git
- GitHub
- GitHub Actions

## Controles aplicados

- Uso de variables de entorno.
- Eliminación de credenciales hardcodeadas.
- Desactivación de debug=True.
- Escape de entradas del usuario.
- Análisis automático con Bandit.

## Actualización

Se agregó configuración de GitHub Actions para ejecutar análisis automático de seguridad con Bandit.