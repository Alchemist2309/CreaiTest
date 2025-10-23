# CreaiTest - Automation Testing Project

Este proyecto contiene pruebas automatizadas para la página web de Creai utilizando Selenium WebDriver con Python y el framework Behave para BDD (Behavior Driven Development).

## Requisitos Previos

- Python 3.12 o superior
- Google Chrome
- pip (gestor de paquetes de Python)

## Estructura del Proyecto

```
CreaiTest/
├── features/             # Archivos de features de Behave
│   ├── steps/           # Implementación de los pasos de las pruebas
│   └── *.feature        # Archivos de especificación de features
├── pages/               # Implementación del patrón Page Object
│   └── creai_page.py    # Página principal de Creai
├── utils/               # Utilidades y helpers
│   └── driver.py        # Configuración del WebDriver
├── requirements.txt     # Dependencias del proyecto
└── README.md           # Este archivo
```

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Alchemist2309/CreaiTest.git
cd CreaiTest
```

2. Crear y activar un entorno virtual (recomendado):
```bash
# En macOS/Linux:
python -m venv .venv
source .venv/bin/activate

# En Windows:
python -m venv .venv
.venv\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución de las Pruebas

Para ejecutar todas las pruebas:
```bash
behave
```

```

## Features Implementadas

- **Home Page Testing**:
  - Validación de carga de página
  - Verificación de elementos clave (logo, botón de contacto)
  - Navegación a sección About Us
  - Validación de secciones visibles



## Mejores Prácticas

- Las pruebas utilizan el patrón Page Object para mejor mantenibilidad
- Se implementa manejo de esperas explícitas para mejor estabilidad
- Los selectores están diseñados para ser robustos ante cambios en la UI
- Se incluye manejo de errores y logging para facilitar la depuración

## Notas Adicionales

- El proyecto está configurado para usar Chrome como navegador predeterminado
- Se recomienda mantener Chrome y ChromeDriver actualizados
- Las pruebas están diseñadas para ser independientes entre sí
