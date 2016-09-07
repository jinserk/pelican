#!/bin/bash

make html || exit 1;
make publish || exit 1;
git commit -a || exit 1;
git push || exit 1;
git subtree push --prefix=output jinserk master || exit 1;
