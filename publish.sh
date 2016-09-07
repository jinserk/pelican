#!/bin/bash

make html
make publish
git commit -a
git push
git subtree push --prefix=output jinserk master
