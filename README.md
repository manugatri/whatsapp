# Envío Masivo de Mensajes Personalizados por WhatsApp

Este script en Python permite enviar mensajes personalizados por WhatsApp a una lista de contactos que se importa desde un archivo CSV.

---

## Requisitos

- Python 3.x instalado
- Librerías Python:
  - pandas
  - pyautogui
- Navegador web por defecto (se abrirá WhatsApp Web)

---

## Cómo usar

1. **Preparar el archivo CSV**  
   Debe tener al menos dos columnas:  
   - `Nombre`: Nombre del contacto  
   - `Telefono`: Número de teléfono con código internacional sin signos (+, espacios ni guiones)

   Ejemplo de contenido CSV:

   | Nombre  | Telefono        |
   |---------|-----------------|
   | Juan    | 34123456789     |
   | María   | 34987654321     |

2. **Configurar la ruta del CSV**  
   Cambia la ruta en el script en esta línea:  
   ```python
   df = pd.read_csv('/ruta/al/archivo/archivo.csv')
