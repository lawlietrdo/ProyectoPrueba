
---

## **🎯 Propósito del Sistema**
El propósito del sistema es **agilizar el registro de nuevos clientes** y **gestionar eficientemente la información** tanto de clientes como de usuarios. 
Permite:
- Registrar y actualizar información de clientes.
- Crear fichas específicas para el análisis del cabello.
- Gestionar usuarios y generar reportes en formato PDF.

---

## **📜 Requisitos Funcionales**

### **👥 Roles y Autenticación**
1. **Autenticación**:
   - Todos los usuarios deben iniciar sesión para acceder al sistema.
   - Roles disponibles:
     - 🛠️ **Administrador**: Gestor de usuarios y generador de reportes.
     - ✂️ **Estilista**: Registra clientes y completa evaluaciones.

---

### **🛠️ Gestión de Usuarios (Administrador)**
- Crear, editar y eliminar usuarios con el rol de estilista.
- Consultar la información de los clientes registrados por los estilistas.
- Generar fichas en formato PDF basadas en la información almacenada.

---

### **✂️ Gestión de Clientes (Estilistas)**
- Registrar nuevos clientes con los siguientes datos obligatorios:
  - **Nombres.**
  - **Apellidos.**
  - **DNI (identificador único).**
  - **Número de celular.**
  - **Dirección.**
  - **Profesión.**
  - **Medio por el cual nos conoció.**

- Si el cliente ya existe:
  - Agregar una nueva ficha con información reciente al historial.

---

### **📝 Gestión de Fichas de Evaluación de Cabello (Estilistas)**
- Al registrar o actualizar un cliente:
  - Crear una ficha de análisis y evaluación del cabello.
  - La ficha incluye:
    - **Tipo de cabello.**
    - **Estado del cuero cabelludo.**
    - **Recomendaciones o tratamientos sugeridos.**

---

## **🔧 Tecnologías Utilizadas**
- **Backend**:
  - Python (Flask/Django).
  - Base de datos: MongoDB/MySQL.
- **Frontend**:
  - HTML5, CSS3, JavaScript (React.js o Vue.js).
- **Generación de PDFs**:
  - Librerías como `ReportLab` o `PyPDF2`.
- **Autenticación**:
  - Manejo de roles y permisos (JWT o Django Rest Framework).

---

## **🚀 Instalación**
1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
