# AIBG
## Instalación la primera vez
**Primero necesito que me paséis vuestros usuarios de GitHub para autorizaros**

**Hay que instalarse git de [aquí](https://git-scm.com/downloads)**
```console
git config --global user.name "Tu nombre"
git config --global user.email "tuemail@example.com"
git config --global user.password "secret"
git clone https://github.com/rosalvio/AIBG.git
git checkout -b tu_nombre
python -m venv venv
venv/Scripts/activate (si no funciona probad con venv\Scripts\activate)
pip install -r requirements.txt
```

## ATENCIÓN
**CADA VEZ QUE ABRAMOS EL PROYECTO DEBEMOS EJECUTAR** 

*venv/Scripts/activate*

## Primer push
```console
git add .
git commit -m "mensaje detallando los cambios realizados"
git push origin tu_nombre
```

## Siguientes push
```console
git add .
git commit -m "mensaje detallando los cambios realizados"
git push
```

## Ejecución del juego
### En Pycharm
Abrir game.py y abajo donde pone main darle al botón de play que sale a la izquierda.

### En Visual Studio Code
Abrir game.py y dar al botón de play que sale arriba a la derecha.

### Por consola
```console
python game.py
```