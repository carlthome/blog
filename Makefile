build:
	echo "Build phase..."
	./strip-widgets.sh
	nikola build

install:
	echo "Install phase..."

run:
	echo "Run phase..."
	nikola auto
