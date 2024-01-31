# Unicorn Hat HD Space Invaders
By MarkW

Inspired by my old AstroWars hand held thing in the 80s, I know you can play space invaders on a few lights. 

## Pimoroni Unicorn Hat HD Space Invaders Game. 

Use the LEFT and RIGHT Arrow keys, UP or SPACEBAR is shoot. 


## Install Instructions 
You'll need PIL and it's an outdated version too. I'll try to fix that but it's not my dependency 
it's in the unicorn hat driver/handler somewhere. 

```shell
python -m venv venv
source venv/bin/activate
pip install Pillow==9.5.0
```

If when you run it it complains about anything else (numpy or curses or whatever), just pip install them like this:
```shell
pip install numpy
```


## How to run it? 
```shell
python ./spaceinvaders.py 
```

## What if it's sideways?
Pass the rotation in to the script, this will flip it 180 degrees
```shell
python ./spaceinvaders.py 180
```
Or this will make it sideways 
```shell
python ./spaceinvaders.py -90
```

