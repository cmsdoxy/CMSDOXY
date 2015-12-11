#!/bin/sh

REPOSITORY_DIRECTORY="cms-bot"

if [ -d "$REPOSITORY_DIRECTORY" ]; then
	cd $REPOSITORY_DIRECTORY
	remote=$(
	    git ls-remote -h origin master |
	    awk '{print $1}'
	)
	local=$(git rev-parse HEAD)

	printf "Local : %s\nRemote: %s\n" $local $remote

	if [[ $local == $remote ]]; then
	    echo "Commits match."
	else
	    echo "Commits don't match."
	    git pull
	fi
else
	git clone https://github.com/cms-sw/cms-bot.git
fi
