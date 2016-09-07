#!/bin/bash

echo -e "\nmake html && make publish"
make html || exit 1;
make publish || exit 1;

echo -e "\ngit commit"
git commit -a || exit 1;

echo -e "\ngit push"
git push || exit 1;
git subtree push --prefix=output jinserk master || exit 1;
