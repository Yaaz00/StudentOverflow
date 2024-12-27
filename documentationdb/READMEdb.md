Entidades y Atributos
Usuario

Identificación (clave primaria)
Nombre
Correo electrónico
Contraseña (almacenada de forma segura)
Fecha de registro
Pregunta

Identificación (clave primaria)
Título
Contenido
ID del usuario (clave foránea que referencia a Usuario)
Fecha de publicación
Estado (abierto, cerrado)
Respuesta

Identificación (clave primaria)
Contenido
ID de la pregunta (clave foránea que referencia a Pregunta)
ID del usuario (clave foránea que referencia a Usuario)
Fecha de publicación
Etiqueta

Identificación (clave primaria)
Nombre
Comentario

Identificación (clave primaria)
Contenido
ID de la respuesta o pregunta (clave foránea que referencia a Respuesta o Pregunta)
ID del usuario (clave foránea que referencia a Usuario)
Fecha de publicación
Relaciones
Un usuario puede hacer muchas preguntas (1:N).
Un usuario puede dar muchas respuestas (1:N).
Una pregunta puede tener muchas respuestas (1:N).
Una pregunta puede tener muchas etiquetas (N:M).
Una respuesta puede tener muchos comentarios (1:N).
