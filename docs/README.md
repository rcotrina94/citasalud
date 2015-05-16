# Práctica 02: Gestión de citas y diagnósticos

Un hospital funciona con un sistema de cita previa. Cada vez que un paciente pide una cita, puede solicitarla él mismo vía web, por teléfono o personalmente en el centro hospitalario. En los dos últimos casos será atendido por un administrativo, independientemente de cómo se pida la cita, el sisema le asigna un día, una hora y su médico de cabecera. Para guardar esta información se utiliza un listado con el Nnúmero de Seguridad Social (NSS) del paciente, su nombre, apellidos, teléfono para comunicarle cualquier cambio en el día, hora y número de colegiado de su médico de cabecera.

Una vez que llega a la consulta, el médico tiene un historial (datos personales, fecha de visitas, diagnóstico, o visita a otros médicos especialista) y le indica un diagnóstico con su correspondiente tratamiento. Si es enfermedad común, el paciente puede recibir el tratamiento en casa y, si no lo es, debe ir al especialista. Si le manda al especialista, se tendrá en cuenta que hay muchos especialistas, según el problema presentado, y que de nuevo se pedirá cita previa (igual para el de cabecera).
Cuando llega el día, el paciente visita el especialista y éste realiza un diagnóstico que se anota en su ficha de diagnóstico, identificando al paciente, al ´médico en general que lo envió a su consulta, el diagnóstico y el tratamiento que se le va a aplicar.

En el tratamiento pueden ser necesarias la intervención de una o varias operaciones, que serán realizadas por el médico especialista, así como radiografías, ecografías, inyecciones, etc., que van a ser realizadas, por distintas personas no médicas del hospital: ATS (Ayudante Técnico Sanitaro: practicantes, enfermer@s) , técnicos, auxiliares, etc.)

Se sabe que en el hospital los médicos van identificados por su número de colegiado y el resto del personal por su número de registro personal.


## ACTORES

- PACIENTE
- PERSONAL (ADMINISTRATIVO)
- MEDICO
    * GENERAL
    * ESPECIALISTA


## PROCESOS PRINCIPALES

- REGISTRAR CITA SOLICITADA POR PACIENTE
- PACIENTE ASISTE A CONSULTA


## ACTIVIDADES POR PROCESO PRINCIPAL

### REGISTRO DE CITA SOLICITADA POR PACIENTE

- **PACIENTE SOLICITA CITA**
    - PACIENTE ======= SOLICITA CITA VIA WEB ======> SISTEMA
    - PACIENTE ==== SOLICITA CITA PERSONALMENTE ===> SISTEMA

- **CITA ES ASIGNADA A PACIENTE**
    - SISTEMA === ASIGNA CITA ==> PACIENTE

### PACIENTE ASISTE A CONSULTA

- **MEDICO ATIENDE PACIENTE**
    - MEDICO ===== CONSULTA HISTORIAL PACIENTE ====> SISTEMA
    - SISTEMA == RETORNA DATOS+HISTORIAL PACIENTE => MEDICO
    - MEDICO ============== ANALIZA ===============> PACIENTE
    - MEDICO ====== ACTUALIZA DATOS PACIENTE ======> SISTEMA
    - MEDICO =========== DIAGNOSTICA ==============> PACIENTE
    - MEDICO ====== ANOTA DIAGNOSTICO PACIENTE ====> SISTEMA

-


======
CLASES
======

Paciente

Personal
    Administrativo
    Medico
        General
        Especialista

Cita_médica

