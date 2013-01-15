.PHONY: deploy.stonelinks deploy

# deploy to stonelinks.org
deploy.stonelinks:
	@cp -R js/physics ~/stonelinks/static/js/
	@cp js/frc-simulator.js ~/stonelinks/js/src/frc-simulator.js
	@cp -R frc-simulator ~/stonelinks/content/
	@cd ~/stonelinks && $(MAKE) site

deploy: deploy.stonelinks

.PHONY: all

all: deploy
