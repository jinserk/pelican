#!/bin/bash

echo "make html && make publish"
make html || exit 1;
make publish || exit 1;

echo -e "git commit"
git commit -a || exit 1;

echo -e "git push"
git push || exit 1;
git subtree push --prefix=output jinserk master || exit 1;
