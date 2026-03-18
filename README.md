# dsa_pre_midterm

Playlist de música implementada con una lista doblemente encadenada (doubly linked list) en Python. Cada nodo de la lista representa una canción y almacena su nombre, artista y álbum. La interfaz de consola permite navegar la playlist hacia adelante y hacia atrás.

## Estructura del proyecto

```
dsa_pre_midterm/
  simulacro/
    ll.py           # Definición de las clases Node y LinkedList
    playlist.py     # Datos de las 50 canciones y función para construir la playlist
    interface.py    # Interfaz de consola para navegar la playlist
    test.py         # Pruebas básicas de la linked list
  README.md
```

## Estructura de datos

Se implementó una **doubly linked list** donde cada `Node` contiene:
- `data`: diccionario con `song`, `artist` y `album`
- `next`: puntero al siguiente nodo
- `prev`: puntero al nodo anterior

Esto permite navegar la playlist en ambas direcciones en tiempo O(1).

## Requisitos

- Python 3.8 o superior

## Clonar y correr

```bash
git clone <url-del-repo>
cd dsa_pre_midterm/simulacro
python interface.py
```

## Controles

| Tecla | Acción |
|-------|--------|
| `n` | Siguiente canción |
| `p` | Canción anterior |
| `q` | Salir |

## Notas

- La playlist carga 50 canciones automáticamente al iniciar.
- Comienza reproduciendo la primera canción de la lista.
- No es circular: al llegar al inicio o al final, la navegación se detiene.
