#!/bin/bash

rm -fR deploy/*
make publish

cd deploy
git add .
git ci -m "Updated"
git push
